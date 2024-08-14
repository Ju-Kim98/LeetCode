class Solution {
public:
    int smallestDistancePair(vector<int>& nums, int k) {
        std::sort(nums.begin(), nums.end());
        
        auto helper = [&](int dist) -> int {
            int left = 0, res = 0;
            for (int right = 0; right < nums.size(); ++right) {
                while (nums[right] - nums[left] > dist) {
                    ++left;
                }
                res += right -left;
            }
            return res;
        };
        
        // binary search for the kth smallest distance
        int left = 0, right = nums.back() - nums.front();
        while (left < right) {
            int mid = left+(right-left)/2;
            int pairs = helper(mid);
            if (pairs >= k) {
                right = mid;
            } else {
                left = mid+1;
            }
        }
        return left;
    }
};