class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n=len(nums)
        left=0
        right=0
        for i in range(n):
            if nums[i]<nums[left]:
                left=i
            if nums[i]>nums[right]:
                right=i
        if left>right:
                left,right=right,left
        ans=n
        for i in range(n+1):
                extra=0
                if right>=i:
                    extra=n-right
                if left>=i:
                    extra=n-left
                ans=min(ans,i+extra)
        return ans