# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #using binary search
        
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        
        left = 0
        right = len(nums) - 1
        
        while left<=right:
            if nums[left] != nums[right]:
                return False
            left += 1
            right -= 1
        return True
    
    #more sol) fast&slow alg.