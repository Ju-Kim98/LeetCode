class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # time complexity must be better than O(nlogn) -> sort쓰지 말고
        #Array, Hash Table O(1) hash table을 쓰려면 sorting을 무조건 써야하나?
        
    
#         hash_set = set()
#         l = len(nums)
                
#         for n in range(0,l):
#             #fre = nums.count(k)
#             counts = nums.count(nums[n])  
#             if counts >= k:
#                 hash_set.add(nums[n])
                       
#         return hash_set
            
                
        #counter function 써도 됨
        #bucket sort  (key value가 반복 횟수, value가 array value값)  O(n) time
        
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        bucket_list = []
        
        for num in nums:
            count[num] = 1 + count.get(num, 0)
            
        for key, v in count.items():
            freq[v].append(key)
        
        for i in range(len(freq)-1, 0, -1):
            for j in freq[i]:
                bucket_list.append(j)
                if len(bucket_list) == k:
                    return bucket_list
                
                
    # 예시 코드
    # def insertion_sort(bucket):
    # for i in range (1, len (bucket)):
    #     var = bucket[i]
    #     j = i - 1
    #     while (j >= 0 and var < bucket[j]):
    #         bucket[j + 1] = bucket[j]
    #         j = j - 1
    #     bucket[j + 1] = var
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
            
        