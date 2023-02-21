# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head== None or head.next == None:
            return head
        if head== None or head.next == None:
            return head

        temp1 = head
        temp2 = head.next
        temp3 = head
        
        while temp2 and temp3:
            if temp2.val == temp3.val:
                if temp3 == head:
                    dup = head.val
                    while head and head.val == dup:
                        head = head.next
                    if head== None or head.next == None:
                        return head
                    temp1 = head
                    temp3 = head
                    temp2 = head.next
                else:
                    while temp2 and temp2.val == temp3.val:
                        temp2 = temp2.next
                    while temp1 and temp1.next != temp3:
                        temp1 = temp1.next
                    if temp2 == None:
                        temp1.next = None
                        break
                    temp1.next = temp2
                    temp2 = temp2.next
                    temp3 = temp1.next
            else:
                temp3 = temp3.next
                temp2 = temp2.next
        return head
