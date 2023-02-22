import re

def validateIPaddress(queryIP):
    ipv4 = r"(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])"
    ipv4_pattern = re.compile(r'^(' + ipv4 + r'\.){3}' + ipv4 + r'$')
    
    ipv6 = r'([a-zA-Z0-9]){1,4}'
    ipv6_pattern = re.compile(r'^(' + ipv6 +'\:){7}' + ipv6 + r'$')
    
    if re.search(ipv4_pattern, queryIP):
        return "IPv4"
    elif re.search(ipv6_pattern, queryIP):
        return "IPv6"
    else:
        return "Nothing"


def main():
    testcases = ["172.16.254.1", "2001:0db8:85a3:0:0:8A2E:0370:7334", "256.256.256.256"]
    for testcase in testcases:
        returnValue = validateIPaddress(testcase)
        print("For testcase {} the return value is {}".format(testcase, returnValue))

if __name__ == "__main__":
    main()