# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        prev = head
        curr = head.next

        res = [-1,-1]
        pos = 1
        leftMostCp = -1
        prevCp = -1
        while curr.next:

            if (curr.val > prev.val and curr.val > curr.next.val) or (curr.val <prev.val and curr.val<curr.next.val):
                if prevCp == -1:
                    prevCp = pos
                    leftMostCp = pos
                else:
                    res[0] = min(res[0],pos-prevCp) if res[0] != -1 else pos-prevCp
                    res[1] = max(res[1],pos-leftMostCp) 
                    prevCp = pos
            prev = curr
            curr = curr.next
            pos += 1
        return res
            
                

        