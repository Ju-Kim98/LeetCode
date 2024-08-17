# The read4 API is already defined for you.
# @param buf4, List[str]
# @return an integer
# def read4(buf4):

class Solution(object):
    def __init__(self):
        self.buf4 = [None]*4
    
    def read(self, buf, n):
        """
        :type buf: List[str]
        :type n: int
        :rtype: int
        """
        i = 0
        while n>0:
            if not any(self.buf4):
                #if buf4 is empty, reload it
                read4(self.buf4)
            c = self.buf4.pop(0)
            self.buf4.append(None)
            if c:
                buf[i] = c
            else: 
                buf[i] = ''
            i += 1
            n -= 1
        return i