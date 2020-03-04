class Solution(object):
    def removeDuplicates(self, nums):
        """
        思路：设定两个游标，一个是指向当前读取列表的游标，一个指向去重重复数据后的游标。就是每次遇到不重复的值直接复制到第二个游标指向的位置。
        :type nums: List[int]
        :rtype: int
        """
        # 初始化两个游标
        cursor_1 = 0
        cursor_2 = 1
        length = len(nums)
        while cursor_1 < length:
            while cursor_1 + 1 < length and nums[cursor_1] == nums[cursor_1 + 1]:
                cursor_1 += 1
            if cursor_1 + 1 < length:
                nums[cursor_2] = nums[cursor_1 + 1]
                cursor_1 += 1
                cursor_2 += 1
            else:
                cursor_1 += 1

        return cursor_2


if __name__ == '__main__':
    nums = [0,1,1]
    length = Solution().removeDuplicates(nums)
    print(length)