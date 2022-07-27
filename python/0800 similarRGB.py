class Solution:
    def similarRGB(self, color: str) -> str:
        """
            #hex #int #min #lambda
        """
        sim_hex = ["00","11","22","33","44","55","66","77","88","99","aa","bb","cc","dd","ee","ff"]
        def sim(h):
            return min(sim_hex,key = lambda x : abs(int(h,16) - int(x,16)))
        
        res = "#"+sim(color[1:3])+sim(color[3:5])+sim(color[5:])
        
        return "#" if res == "#000000" else res
        