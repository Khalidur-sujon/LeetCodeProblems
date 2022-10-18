class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        total = len(a) + len(b)
        half = total // 2

        if len(b) < len(a):
            a, b = b, a
        
        l, r = 0, len(a) - 1
        while True:
            mid = (l + r) // 2
            j = half - mid - 2

            aleft = a[mid] if mid >= 0 else float('-infinity')
            aright = a[mid + 1] if (mid + 1) < len(a) else float('infinity')
            bleft = b[j] if j >= 0 else float('-infinity')
            bright = b[j + 1] if (j + 1) < len(b) else float('infinity')

            # partition is correct
            if aleft <= bright and bleft <= aright:
                # odd
                if total % 2:
                    return min(aright, bright)
                # even
                return (max(aleft, bleft) + min(aright, bright)) / 2
            elif aleft > bright:
                r = mid - 1
            else:
                l = mid + 1
