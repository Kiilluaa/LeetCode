class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.prefix = []
        running_sum = 0

        for i in nums:
            running_sum += i
            self.prefix.append(running_sum)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        
        if left == 0:
            return self.prefix[right]
        return self.prefix[right] - self.prefix[left - 1]