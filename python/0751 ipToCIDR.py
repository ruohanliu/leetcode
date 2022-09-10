from typing import List
import math
class Solution:
    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        """
            #math #bitwise #ipaddress #two'scomplement

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

    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        def ipToInt(ip):
            ans = 0
            for i,block in enumerate(ip.split(".")):
                ans += int(block) << (8 * (3-i))
            return ans
        def intToIP(i):
            ans = []
            for _ in range(4):
                i,m = divmod(i,256)
                ans.append(str(m))
            return ".".join(ans[::-1])

        ans = []
        ip_start = ipToInt(ip)
        while n > 0:
            rbit = ip_start & (-ip_start)
            # edge case when input ip is 0, max n is 1000
            if rbit == 0:
                rbit = 1024
            while rbit > n:
                rbit >>= 1
            n -= rbit
            # r is the length of masked bits
            r = rbit.bit_length()-1
            l = 32-r
            ans.append(intToIP(ip_start >> r << r)+f"/{l}")
            ip_start += rbit
        return ans