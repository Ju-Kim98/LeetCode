#Danamic Programming

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==0:
            return []
        
        triple = [[1]]
        
        for i in range(1, numRows):
            front_row = triple[-1]
            next_row = [1]
            
            for j in range(1, len(front_row)):
                next_row.append(front_row[j-1] + front_row[j])
                
            next_row.append(1)
            triple.append(next_row)
            
        return triple
        
        
        
 