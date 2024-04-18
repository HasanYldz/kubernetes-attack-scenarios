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

1- Install requirements \
2- `npm start` Server starts on port `4242` \
3- Listen on port `1234` for TCP connections with `nc -l 127.0.0.1 1234` \
4- Run poc.py \
5- You are in!

### Kubernetes
Check https://learnk8s.io/deploying-nodejs-kubernetes for deployment tutorial