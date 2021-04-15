class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tmap = collections.Counter(t)
        tcount = len(t)
        cmap = {}
        for x in tmap.keys():
            cmap[x] = 0
        ccount = 0
        l,r = 0,0
        ans = s + '!'
        while r < len(s):
            c = s[r]
            if c in tmap:
                cmap[c] +=1
                if cmap[c] <=tmap[c]:
                    ccount +=1
                while l<r and (s[l] not in tmap or cmap[s[l]])>tmap[s[l]]:
                    if tmap[s[l]]:
                        cmap[s[l]] -=1
                    l+=1
                if tcount == ccount:
                    ans = ans if len(ans) <= r-l+1 else s[l:r+1]
            r +=1
        return ans if len(ans) <= len(s) else ''