class Solution(object):
    def prisonAfterNDays(self, cells, n):
        """
        :type cells: List[int]
        :type n: int
        :rtype: List[int]
        """
        seen = dict()       # init dictionary to stor cell states and their corresponding days to detect cycles
        has_cycle = False
        
        while n > 0:
            if not has_cycle:
                state_key = tuple(cells)
                if state_key in seen:
                    # the length of the cycle is seen[state_key] - n
                    n %= seen[state_key] - n
                    has_cycle = True
                    
                else:
                    seen[state_key] = n
                    
            # check if there is still some steps remained
            # with or w/o the fast-forwarding
            if n > 0:
                n -= 1
                next_state = self.nextDay(cells)
                cells = next_state
                
        return cells
    
    def nextDay(self, cells):
        res = [0]     #head
        for i in range(1, len(cells)-1):
            res.append(int(cells[i-1] == cells[i+1]))
        res.append(0)     #tail
        return res
                
                
                
                
        