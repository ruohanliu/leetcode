from typing import List
import math
import ipaddress
class Solution:
    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        ans = []
        divisor = 2**10
        ip_dec = sum(int(x)*256**(3-i) for i,x in enumerate(ip.split(".")))
        while ip_dec % divisor > 0:
            print(divisor,ip_dec % divisor,)
            divisor //= 2

        mask = 32-int(math.log(divisor,2))-1

        if n >= divisor:
            ans.append(str(ipaddress.IPv4Address(ip_dec & (1 << mask)))+f"/{mask}")
        print(ip_dec,mask,ans)

s = Solution()
print(s.ipToCIDR("255.0.0.8",12))