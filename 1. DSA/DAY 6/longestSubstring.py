class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        ans = []
        for l in range(N, 0, -1):
            found = False
            for i in range(N-l+1):
                target = s[i:i+l]
                if target == target[::-1]:
                    ans.append(s[i:i+l])
                    found = True
            if found:
                break
        return ans[0] if s else ['']