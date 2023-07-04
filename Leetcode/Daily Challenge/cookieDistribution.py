#2305 (Medium)

# https://www.youtube.com/watch?v=yG4QtNI3m3Y

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        bucket = [0]*n

        def distribute(i = 0):
            ans = sys.maxsize
            visited = set()
            if i == n:
                return max(bucket)
            for j in range(k):
                if bucket[j] in visited:
                    continue
                visited.add(bucket[j])
                bucket[j]+= cookies[i]
                if max(bucket) < ans:
                    ans = min(ans,distribute(i+1))
                bucket[j] -= cookies[i]
            return ans
        cookies.sort(reverse = True)
        return distribute(0)