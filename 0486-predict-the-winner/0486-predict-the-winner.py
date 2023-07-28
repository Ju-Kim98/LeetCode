class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        temp = {}
        def maxscore(i,j):
            if (i,j) in temp:
                return temp[i,j]
            if i>j:
                return 0

            #pick nums[i] + min of the 2 possible upcoming turns 
            sA = nums[i] + min(maxscore(i+1,j-1), maxscore(i+2,j)) 
            sB = nums[j] + min(maxscore(i,j-2), maxscore(i+1,j-1))
            score = max(sA,sB)
            temp[i,j] = score
            return score

        p1 = maxscore(0, len(nums)-1)  #Player1's Score
        return p1 >= (sum(nums)-p1)   # p1>=p2