val_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000 
        }

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = val_dict.get(s[-1])   #s[-1]last char
        for i in reversed(range(len(s)-1)):
            if val_dict[s[i]] < val_dict[s[i+1]]:
                total -= val_dict[s[i]]
            else:
                total += val_dict[s[i]]
        return total
        