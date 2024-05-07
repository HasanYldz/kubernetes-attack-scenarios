## CVE-2022-35411
https://nvd.nist.gov/vuln/detail/CVE-2022-35411 \
Target Application: rpc.py \
Software Link: https://github.com/abersheeran/rpc.py \
Version: 0.6.0 \
Writeup: https://medium.com/@elias.hohl/remote-code-execution-0-day-in-rpc-py-709c76690c30 \
Used PoCs: 
* https://github.com/ehtec/rpcpy-exploit

### Steps to Reproduce

1- `pip install server/rpc.py-0.6.0` \
2- `nc -l 127.0.0.1 1234` \
3- `python server/rpc.py-0.6.0/examples/async_server.py` \
4- `python poc.py` \