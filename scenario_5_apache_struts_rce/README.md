## CVE-2017-12611
Target Application: Apache Struts 2 \
Used PoCs: 
* https://github.com/Medicean/VulApps/tree/master/s/struts2/s2-053

### Steps to Reproduce

1- `minikube start` \
2- `kubectl apply -f scenario-1-server.yaml` \
3- `kubectl apply -f role.yaml` \
4- `kubectl apply -f rolebinding.yaml` \
5- Forward port `kubectl port-forward pods/struts.... 8080:8080` \
6- Run poc.py `python poc.py` \
7- poc.py opens a pseudo reverse shell
8- Because the pod is in the apps api group and can view and delete deployments the attacker deletes the pod he/she is in it.
