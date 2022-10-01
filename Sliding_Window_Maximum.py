class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque()
        l = r = 0

        while r < len(nums):
            # remove smaller number
            while q and nums[q[-1]] < nums[r]:
                q.pop() 
            q.append(r)
     
            if r + 1 >= k:
                #remove left value from the window
                if l > q[0]:
                    q.popleft()
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output
