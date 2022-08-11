class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        """
            #heap #important #islice

            related 1439
        """
        streams = map(lambda u: ([u+v,u,v] for v in nums2),nums1)
        stream = heapq.merge(*streams)
        return [x[1:] for x in itertools.islice(stream,k)]

    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        def push(i, j):
            if i < len(nums1) and j < len(nums2):
                heapq.heappush(heap, [nums1[i] + nums2[j], i, j])
        heap = []
        push(0, 0)
        ans = []
        while heap and len(ans) < k:
            _, i, j = heapq.heappop(heap)
            ans.append([nums1[i], nums2[j]])
            push(i, j + 1)
            if j == 0:
                push(i + 1, 0)
        return ans