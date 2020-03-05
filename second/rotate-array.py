class Solution(object):
    def rotate1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 第一中解法，每次移动一步
        length = len(nums)
        if length == 0 or length == 1:
            return nums
        for t in range(0, k):
            tmp = nums[0]
            for i in range(0, length-1):
                nums[(length-i)%length] = nums[length - 1 -i]
            nums[1] = tmp
        return nums
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(nums)

        if length == 0 or k == 0:
            return

        k = k % length

        self.reverse(nums, 0, length -1)
        self.reverse(nums, 0, k -1)
        self.reverse(nums, k, length -1)

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
