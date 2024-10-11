# use doubly linked list. therefore, when we remove ta node, we have prev pointer to reference the node before it. O(1) time
class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.hm = {}
        self.head = ListNode(-1,-1)
        self.tail = ListNode(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.hm:
            return -1
        
        node = self.hm[key]     #get the node associated w/ key from hm
        self.remove(node)       # move it to the back of the linked list
        self.add(node)
        
        return node.val
        
        
    # updates key: value if it already exists, and insert otherwise.
    # if inserting, the size to exceed capacity, we need to remove the least recently used key(which is head of linked list)
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.hm:
            old_node = self.hm[key]
            self.remove(old_node)
            
        node = ListNode(key, value)
        self.hm[key] = node
        self.add(node)
        
        if len(self.hm) > self.capacity:
            remove_node = self.head.next
            self.remove(remove_node)
            del self.hm[remove_node.key]
        
        
    # takes a node and puts it at the end of the linked list    
    def add(self, node):
        prev_end = self.tail.prev   # get curr node at the end of the linked list
        prev_end.next = node        # node is being inserted after prev_end
        node.prev = prev_end        # set the pointers of node
        node.next = self.tail       # set the pointers to real tail
        self.tail.prev = node       # update the tail
        
    #removes node from the linked list
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        


        
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)