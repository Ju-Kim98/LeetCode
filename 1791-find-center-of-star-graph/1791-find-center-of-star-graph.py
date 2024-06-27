class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        # degree count O(n) time, O(n) space
        
        degree = {}

        for edge in edges:
            degree[edge[0]] = degree.get(edge[0], 0) + 1
            degree[edge[1]] = degree.get(edge[1], 0) + 1

        for node, count in degree.items():
            if count == len(edges):
                return node

        return -1
    
         # greedy O(1) time, O(1) space
        
#         first_edge, second_edge = edges[0], edges[1]

#         return first_edge[0] if first_edge[0] in second_edge else first_edge[1]