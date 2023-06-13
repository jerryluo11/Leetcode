# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        list3 = ListNode()
        while list1.next != None and list2.next != None:
            if list1.val < list2.val:
                list3.next = list1.next
            else:
                list3.next = list2.next
        return(list3)

s = Solution()

list1 = [1,2,4]
list2 = [1,3,4] 
print(s.mergeTwoLists(list1, list2))
