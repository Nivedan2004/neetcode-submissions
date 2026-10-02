# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
# Dummy node gives us a fixed starting point so we don't
# have to special-case the head of the merged list
        dummy = ListNode()
        tail = dummy # tail always points to the last node of the merged list

# Keep going while both lists still have nodes
        while list1 and list2:
            # Pick the smaller value of the two current nodes
            if list1.val < list2.val:
                tail.next = list1 # attach list1's node to the merged list
                list1 = list1.next # Move list1 forward
            else:
                tail.next = list2 # attach list2's node to the merged list
                list2 = list2.next # Move list2 forward
            tail = tail.next #move tail to the node we just attached
# One list ran out. The other is already sorted, so just attach the rest
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
# dummy itself is a placeholder, so the real head is dummy.next
        return dummy.next
        