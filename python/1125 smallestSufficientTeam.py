class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        """
            #dfs #bitmask
        """
        def dfs(i,state,persons):
            nonlocal res,curr
            cnt = persons.bit_count()
            if cnt >= curr:
                return float("inf")
            if state == target:
                res = persons
                curr = cnt
                return 0
            if i == m:
                return float("inf")
            return min(1 + dfs(i+1, skills[i] | state,persons | 1 << i) if skills[i]|state > state else float("inf"), dfs(i+1,state,persons))

        n = len(req_skills)
        m = len(people)
        skillMap = {s:i for i,s in enumerate(req_skills)}
        target = (1 << n) - 1

        # filter out useless people, store people's skill in bitmask
        skills = []
        for i,p in enumerate(people):
            s = 0
            for i in range(len(p)):
                if p[i] in skillMap:
                    s |= 1 << skillMap[p[i]]
            skills.append(s)
        
        peopleFilter = 0
        for i in range(m):
            keep = True
            for j in range(i+1,m):
                if skills[i] & skills[j] == skills[i]:
                    keep = False
                    break
            if keep:
                peopleFilter |= 1<<i
        skills = [x for i,x in enumerate(skills) if peopleFilter & 1<<i]
        m = len(skills)

        res = None
        curr = float("inf")
        dfs(0,0,0)

        j = 0
        ans = []
        for i in range(len(people)):
            if peopleFilter & 1 << i:
                if res & 1 << j:
                    ans.append(i)
                j += 1

        return ans