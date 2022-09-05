from typing import List
class Solution:
    """
    optimization:
        1. move pointer for duplicate adjacent numbers
        2. first element in the answer tuple cannot be positive

    take-away:
        1. list slicing does not create copies of the list, for both immutable and mutable
        2. When slicing, the references to elements are copied so that change to the original does not affect the sliced list

        https://stackoverflow.com/questions/5131538/slicing-a-list-in-python-without-generating-a-copy
    """
    def twoSum(self, numbers, lo,hi,target: int):
        """
        numbers is sorted
        """

        ans = []
        i = lo
        j = hi
        while i < j:
            if numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                ans.append((-target,numbers[i],numbers[j]))
                while i < hi and numbers[i] == numbers[i+1]:
                    i += 1
                while j > lo and numbers[j] == numbers[j-1]:
                    j -= 1
                i += 1
                j -= 1
        return ans

    def threeSum(self, numbers: List[int]) -> List[int]:
        numbers.sort()
        ans = []
        i = 0
        while i < len(numbers) - 2:
            if numbers[i] > 0: break
            ans += self.twoSum(numbers,i+1,len(numbers) - 1,0-numbers[i])
            while i < len(numbers) - 2 and numbers[i] == numbers[i+1]:
                i+=1
            i += 1
        return ans

    def threeSum_hash(self, numbers: List[int]) -> List[int]:
        """
        use set to eliminate dup and avoid sorting
        use dict for the seen complement to avoid re-creating set in the loop
        """
        dup = set()
        ans = set()

        for i,num1 in enumerate(numbers):
            if num1 not in dup:
                dup.add(num1)
                seen = set()
                for num2 in numbers[i+1:]:
                    complement = -num1-num2
                    if complement in seen:
                        ans.add(tuple(sorted([num1,num2,complement])))
                    seen.add(num2)
        return ans
s = Solution()
print(s.threeSum([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]))
print(s.threeSum_hash([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]))
