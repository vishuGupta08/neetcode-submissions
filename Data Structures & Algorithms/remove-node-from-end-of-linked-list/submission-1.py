# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        prev= dummy
        count = head
        el = head
        totalLength = 0
        while count:
            totalLength +=1
            count = count.next
        length = totalLength - n
        if length == 0:
            return head.next
        counter = 1
        while counter <= length:
            prev = el
            el = el.next
            counter +=1
        
        prev.next = el.next
        return head


        