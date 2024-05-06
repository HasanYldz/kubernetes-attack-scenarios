#include <drogon/drogon.h>
#include <iostream>
#include <fstream>
#include <json/json.h>
#include <cstdlib>
#include <signal.h>
#include <sys/inotify.h>
#include <thread>
#include <unistd.h>

using namespace drogon;

volatile sig_atomic_t terminateServer = 0;

void signalHandler(int signum) {
    std::cout << "Signal (" << signum << ") received, stopping server." << std::endl;
    terminateServer = 1;
    exit(signum);
}

void loadConfiguration(const std::string& filename, Json::Value& config) {
    std::ifstream config_file(filename, std::ifstream::binary);
    if (config_file.is_open()) {
        config_file >> config;
    } else {
        std::cerr << "Unable to open config file." << std::endl;
        exit(1);
    }
}

void watchConfigFile(const std::string& filename) {
    int fd = inotify_init();
    if (fd < 0) {
        perror("inotify_init");
        exit(1);
    }

    int wd = inotify_add_watch(fd, filename.c_str(), IN_MODIFY);
    char buffer[1024];
    while (!terminateServer) {
        int length = read(fd, buffer, sizeof(buffer));
        if (length < 0) {
            perror("read");
            exit(1);
        }

        for (int i = 0; i < length;) {
            struct inotify_event* event = (struct inotify_event*)&buffer[i];
            if (event->mask & IN_MODIFY) {
                std::cout << "Configuration file modified, please restart the server to apply changes." << std::endl;
                // Optionally send a signal or handle internally to shut down

                // If you want to restart the server automatically, uncomment the following line
                raise(SIGUSR1);

            }
            i += sizeof(struct inotify_event) + event->len;
        }
    }

    inotify_rm_watch(fd, wd);
    close(fd);
}

int main() {
    signal(SIGINT, signalHandler); // Handle Ctrl-C for graceful shutdown
    signal(SIGUSR1, signalHandler); // Handle custom signal to restart

    std::cout << "Starting the server" << std::endl;
    Json::Value config;
    loadConfiguration("config.json", config);

    std::thread configWatcher(watchConfigFile, "config.json");


    app().registerHandler("/", [](const HttpRequestPtr &, std::function<void(const HttpResponsePtr &)> &&callback) {
        auto resp = HttpResponse::newHttpViewResponse("FileUpload");
        callback(resp);
    });

    app().registerHandler("/health", [](const HttpRequestPtr &, std::function<void(const HttpResponsePtr &)> &&callback) {
        auto resp = HttpResponse::newHttpResponse();
        resp->setStatusCode(HttpStatusCode::k200OK);
        resp->setBody("OK");
        callback(resp);
    }, {Get});

    app().registerHandler("/upload_endpoint", [](const HttpRequestPtr &req, std::function<void(const HttpResponsePtr &)> &&callback) {
        MultiPartParser fileUpload;
        if (fileUpload.parse(req) != 0 || fileUpload.getFiles().size() != 1) {
            auto resp = HttpResponse::newHttpResponse();
            resp->setBody("Must only be one file");
            resp->setStatusCode(k403Forbidden);
            callback(resp);
            return;
        }

        auto &file = fileUpload.getFiles()[0];
        auto md5 = file.getMd5();
        auto resp = HttpResponse::newHttpResponse();
        resp->setBody("The server has calculated the file's MD5 hash to be " + md5);
        file.save();
        LOG_INFO << "The uploaded file has been saved to the ./uploads directory";
        callback(resp);
    }, {Post});

    std::cout << "Server running on " << config["serverIP"].asString() << ":" << config["serverPort"].asUInt() << std::endl;

    app().setClientMaxBodySize(20 * 2000 * 2000);
    app().setUploadPath("./uploads");

    app().addListener(config["serverIP"].asString(), config["serverPort"].asUInt());

    app().run();

    configWatcher.join();
    return 0;
}
