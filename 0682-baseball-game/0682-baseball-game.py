class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        
        record = []
        for op in operations:
            if op == 'C':                       # remove the last score
                record.pop()
            elif op == 'D':                     # double the last score and add to the record
                record.append(2 * record[-1])
            elif op == '+':                     # sum the last two scores and add to the record
                record.append(record[-1] + record[-2])
            else:
                record.append(int(op))          # add the new score
        return sum(record)