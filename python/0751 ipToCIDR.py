from typing import List
import math
class Solution:
    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        """
            #math #bitwise #ipaddress #two'scomplement #important

            value of least significan 1 in binary can be computed as x & (-x)
            corner case: x = 0   0&0 = 0
        """
        import ipaddress
        ans = []
        ip_start = int(ipaddress.IPv4Address(ip))
        while n > 0:
            cap = ip_start & (-ip_start)
            if cap == 0:
                cap = 1024
            while cap > n:
                cap >>= 1
            n -= cap
            r = int(math.log(cap, 2))
            l = 32-r
            ans.append(str(ipaddress.IPv4Address(ip_start >> r << r))+f"/{l}")
            ip_start += cap
        return ans
            
s = Solution()
print(s.ipToCIDR("0.0.0.0",10))