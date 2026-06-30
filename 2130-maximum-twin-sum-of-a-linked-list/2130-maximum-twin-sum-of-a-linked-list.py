# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        while fast.next.next:
            slow = slow.next
            fast = fast.next.next
        temp = slow.next
        slow.next = None

        #reversing
        rcurr = temp
        prev = None
        while rcurr:
            next = rcurr.next
            rcurr.next = prev 
            prev = rcurr
            rcurr = next
        
        #sum of twins
        p1= head
        p2 = prev
        mx = 0
        while p1:
            mx = max(mx,p1.val+p2.val)
            p1 = p1.next
            p2 = p2.next
        return mx


        # idxs = {}
        # length = 0
        # curr = head
        # while curr:
        #     idxs[length] = curr.val
        #     curr = curr.next
        #     length+=1
        
        # mx = 0
        # for i in range(length//2):
        #     mx = max(mx,idxs[i]+idxs[length-i-1])
        # return mx
        