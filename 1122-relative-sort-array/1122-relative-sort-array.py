class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        count = Counter(arr1)   #count = {2:3, 3:1, 1:1, 4:1, 6:1, 7:1, 9:1, 19:1} sort 안되어있음
        result = []
        for ele in arr2:
            result.extend([ele]*count[ele])  #list.extend(iterable)는 리스트 끝에 가장 바깥쪽 iterable의 모든 항목넣                    
            del count[ele]
                                            #2*3 -> result list = {2,2,2,3,1,4, ... } 사용하고 난 거는 삭제
                
        for key in sorted(count.keys()):        #keys: 위에 for에서 삭제하고 남은 7:1, 19:1
            result.extend([key]*count[key])     #result list 뒤에 이어줌
        
        return result
    
    #O(n) time