from typing import List,Optional
import random
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
            #linkedlist
        """
        def merge(l1,l2):
            sentinel = ListNode()
            prev = sentinel
            while l1 and l2:
                if l1.val <= l2.val:
                    prev.next = l1
                    l1 = l1.next
                else:
                    prev.next = l2
                    l2 = l2.next
                prev = prev.next

            if not l1:
                prev.next = l2
            else:
                prev.next = l1
            return sentinel.next
        
        n = len(lists)
        while n > 1:
            if n % 2:
                k = random.randrange(0,n-1)
                lists[k] = merge(lists[k],lists[n-1])
            
            for i in range(n//2):
                lists[i] = merge(lists[i],lists[n//2+i])
            
            n //= 2
        return lists[0] if lists else None
            