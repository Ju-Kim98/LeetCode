class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        #m: input 단어 수 
        #각 단어들을 sort해서 같은것끼리 묶기 ->O(mnlogn)         
        #O(mn)  count(n), m: 단어수
        #collections.defaultdict는 값(value)에 초기값을 지정해서 딕셔너리 생성하는 모듈
        #사용한 문자(key), 해당 문자의 사용횟수(value)
        
        #strs = {"ate","eat","tea","bat"}
  
        
        result = collections.defaultdict(list)  # default hashmap:[eat,tea,ate] O(mn26)

        #23ms      
        for st in strs:
             s = ''.join(sorted(st))
             result[s].append(st)

    	return result.values()
        
        
        
        """
        #17ms
        for s in strs:
            count = [0]*26  #count the char a - z, 각 단어에 있는 알파벳 개수 e:1, a:1, t:1  <- 이게 key가 됨,e,a,t가 하나씩 있는 단어들을 분별해서 hashlist에 집어넣기
            for c in s: 
                count[ord(c)-ord("a")] += 1  #current aski value from c, a(80), b(81)    b-a = 81-80=1
            result[tuple(count)].append(s)  #count is the list, in python list can't be key so use tuple.
        return result.values()
    """