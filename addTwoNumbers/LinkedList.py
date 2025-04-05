
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0 
        sum_list = ListNode(0)
        head = sum_list
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            if l1:
                l1 = l1.next 
            if l2:
                l2 = l2.next
            sum = val1 + val2 + carry
            carry = sum // 10
            sum_list.val = sum % 10
            if l1 or l2 or carry:
                sum_list.next = ListNode(0)
                sum_list = sum_list.next
        return head
    

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


solution = Solution()
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
result = solution.addTwoNumbers(l1, l2)
while result:
    print(result.val, end=" -> ")
    result = result.next