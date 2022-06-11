import re
class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        """
            #re
        """
        m = re.match("(([1-9]?[0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([1-9]?[0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\Z",queryIP)
        if m:
            return "IPv4"
        else:
            m = re.match("([0-9a-fA-F]{1,4}\:){7}[0-9a-fA-F]{1,4}\Z",queryIP)
            if m:
                return "IPv6"
        return "Neither"

    def validIPAddress(self, queryIP: str) -> str:
        def isIPv4(s):
            try: return str(int(s)) == s and 0 <= int(s) <= 255
            except: return False

        def isIPv6(s):
            try: return len(s) <= 4 and int(s, 16) >= 0
            except: return False

        if IP.count(".") == 3 and all(isIPv4(i) for i in IP.split(".")):
            return "IPv4"
        if IP.count(":") == 7 and all(isIPv6(i) for i in IP.split(":")):
            return "IPv6"
        return "Neither"