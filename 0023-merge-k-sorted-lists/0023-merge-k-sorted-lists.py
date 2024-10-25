# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        if not lists:
            return None
        
        def mergeTwoList(self, list1, list2):
            head = ListNode()
            curr = head
            
            while list1 and list2:
                if list1.val < list2.val:
                    curr.next = list1
                    list1 = list1.next
                else: 
                    curr.next = list2
                    list2 = list2.next
                curr = curr.next
                
            curr.next = list1 or list2
            
            return head.next
        
        # interatively merge lists using divide and conquer
        while len(lists) > 1:
            merge_list = []
            
            # merge lists in pairs
            for i in range(0, len(lists),2):
                list1 = lists[i]
                list2 = lists[i+1] if i+1 < len(lists) else None
                merge_list.append(mergeTwoList(self,list1,list2))
                
            lists = merge_list  #replace original lists with the merged lists
            
            
        return lists[0]
            
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    