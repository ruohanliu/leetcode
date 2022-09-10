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

        def quickselect(nums,lo,hi,k):
            def partition(lo,hi):
                pivot = abs(target-nums[random.randrange(lo,hi+1)])
                i = lo
                while i <= hi:
                    if abs(target - nums[i]) < pivot:
                        nums[i],nums[lo] = nums[lo],nums[i]
                        lo += 1
                        i += 1
                    elif abs(target - nums[i]) > pivot:
                        nums[i],nums[hi] = nums[hi],nums[i]
                        hi -= 1
                    else:
                        i += 1
                return lo,hi

            if hi <= lo:
                return
            lt,gt = partition(lo,hi)
            if lt<=k<=gt:
                return
            if k>gt:
                quickselect(nums,gt+1,hi,k)
            else:
                quickselect(nums,lo,lt-1,k)
            return


        nums = []
        dfs(root)
        quickselect(nums,0,len(nums)-1,k)
        return nums[:k]