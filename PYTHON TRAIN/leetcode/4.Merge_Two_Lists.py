class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        s = ListNode(0)
        current = s

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
            else:
                current.next = list2
                list2 = list2.next
            
            current = current.next
        
        if list1:
            current.next = list1
        else:
            current.next = list2
        
        return s.next
    
test1 = ListNode(1,ListNode(2,ListNode(4)))
test2 = ListNode(1,ListNode(3,ListNode(4)))

solution = Solution()
result1 = solution.mergeTwoLists(test1,test2)

def print_linked_list(head):
    current = head
    while current:
        print(current.val) 
        current = current.next
    print()

# Print the results
# print(result1)
print_linked_list(result1)  