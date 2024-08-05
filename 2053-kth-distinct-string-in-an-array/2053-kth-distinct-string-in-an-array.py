class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        # hash map
        freq_map = {}
        
        for s in arr:
            freq_map[s] = freq_map.get(s,0)+1
            
        for s in arr:
            if freq_map[s] == 1:
                k -= 1
            if k == 0:
                return s
            
        return ""
        