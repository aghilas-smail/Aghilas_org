# Link : https://leetcode.com/problems/merge-k-sorted-lists/

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    '''
    The idea is we save the value of the list in a array ,
    and we soted in the end , after we transformet to a linklist
    '''
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]: # type: ignore
        
        arr = []
        # If the list is none
        if not lists:
            return None
        # We append the val of the list
        for i in range(len(lists)):
            while lists[i]:
                arr.append(lists[i].val)
                lists[i] = lists[i].next
        # if the array is null (content nothing)
        if not arr:
            return None
        # sorted the array
        arr.sort()

        # declared the first value of the list
        head = ListNode(arr[0])
        currNode = head
        
        for i in range(1, len(arr)):
            newNode = ListNode(arr[i])
            currNode.next = newNode
            currNode = newNode
        return head

solution = Solution()
list1 = ListNode(1,ListNode(2,ListNode(3)))
list2 = ListNode(1,ListNode(3,ListNode(4)))
list3 = ListNode(2,ListNode(6))

merge_list = solution.mergeKLists([list1, list2, list3])

def printList(head):
    current = head
    while current:
        print(current.val, end='')
        current = current.next
    print()

printList(merge_list)