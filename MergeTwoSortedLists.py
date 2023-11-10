#Merge two sorted lists
"""
ou are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Strategy:
- create new listnode named head and a pointer called current.
- while list1 and list2 are not none, if the list1<list2 we point with the head pointer to it and move the list1 pointer to the next value.
- else we point with the head pointer to list2 and move the list2 pointer to the next value.
- we move the head pointer to the next value.
- add the rest of list1 or list2 if any values are left after iterations.
"""
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head=ListNode()//new list node
        current=head//list node pointer
        while list1 and list2:
            if list1.val<list2.val:
                current.next=list1
                list1=list1.next
            else:
                current.next=list2
                list2=list2.next
            current=current.next
        current.next= list1 or list2
        return head.next