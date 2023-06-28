class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #method 1 - sort string
        #return sorted(s) == sorted(t)

        #method 2 - this function automatically count frequency
        #return Counter(s) == Counter(t)

        #method 3 - Using HashMap Count Frequency
        if len(s) != len(t):
            return False
        mapS , mapT = {}, {}

        for i in range(len(s)):
            mapS[s[i]] = 1 + mapS.get(s[i],0)
            mapT[t[i]] = 1 + mapT.get(t[i],0)
        
        for c in mapS:
            if mapS[c] != mapT.get(c, 0):
                return False
        return True

solution = Solution()
s = "anagram"
t = "nagaram"
print(solution.isAnagram(s,t))