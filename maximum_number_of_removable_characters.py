class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def isSubseq(string1, string2):
            i, j = 0, 0
            while i < len(string1) and j < len(string2):
                if i in remove or string1[i] != string2[j]:
                    i += 1
                    continue
                i += 1
                j += 1
            return j == len(string2)

        l, r = 0, len(removable) - 1
        res = 0
        while l <= r:
            m = (l + r) // 2
            remove = set(removable[:m + 1])
            if isSubseq(s, p):
                res = max(res, m + 1)
                l = m + 1
            else:
                r = m - 1
        return res