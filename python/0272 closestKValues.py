# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        """
            #google #bst #quickselect

            O(nlogk)
        """
        def dfs(node):
            nonlocal heap
            if node:
                if len(heap) == k:
                    heapq.heappushpop(heap,(-abs(target-node.val),node.val))
                else:
                    heapq.heappush(heap,(-abs(target-node.val),node.val))

                dfs(node.left)
                dfs(node.right)

        heap = []
        dfs(root)
        return [x[1] for x in heap]

    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        """
            O(n)
        """
        def dfs(node):
            nonlocal nums
            if node:
                nums.append(node.val)
                dfs(node.left)
                dfs(node.right)

        def quick_select(nums,k):
            lo, hi = 0, len(nums) - 1
            pivotIndex = len(nums)
            while pivotIndex != k:
                pivotIndex = partition(nums, lo, hi)
                if pivotIndex < k:
                    lo = pivotIndex
                else:
                    hi = pivotIndex - 1
            
            return nums[:k]
        
        def partition(nums, lo, hi) -> int:
            pivot = abs(nums[random.randrange(lo,hi+1)]-target)
            while lo < hi:
                if abs(nums[lo]-target) > pivot:
                    nums[lo], nums[hi] = nums[hi], nums[lo]
                    hi -= 1
                else:
                    lo += 1
            
            # Ensure the lo pointer is just past the end of
            # the lo range then return it as the new pivotIndex
            if abs(nums[lo]-target) < pivot:
                lo += 1
            return lo

        nums = []
        dfs(root)
        return quick_select(nums,k)
        