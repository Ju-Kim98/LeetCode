class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        digits = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]
        
        RD = [] #roman digits
        for val, sym in digits:
            if num == 0:
                break
            count, num = divmod(num, val)   #divmod: (8 // 2, 8 % 2) 몫,나머지
            RD.append(sym*count)
            
        return "".join(RD)
        
        
        """
        thousand = ["", "M", "MM", "MMM"]
        hundred = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        ten = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        one = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        
        res = (
            thousand[num//1000]+hundred[num%1000//100]
            +ten[num%100//10]+one[num%10]
        )
        
        return res
        """