class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #[1,2,3,3]
        i=0
        while i < len(nums):
            print('i', i)
            if i == len(nums)-1:
                break
            elif nums[i] == nums[i+1]:
                del(nums[i])
                i-=1
            i+=1
        print(nums)
        return len(nums)


s = Solution()
list = [1,1,2,2,2,3,5,6]
print('list',list)
print('number of unique numbers', s.removeDuplicates(list))

