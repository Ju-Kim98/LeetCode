class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<std::vector<int>> res;
        vector<int> current;
        dfs(candidates, target, 0, current, res);
        return res;
    }
    
private:
    void dfs(const std::vector<int>& candidates, int target, int index, std::vector<int>& current, std::vector<std::vector<int>>& res) {
            if (target == 0) {
                res.push_back(current);
                return;
            }

            if (target < 0 || index >= candidates.size()) {
                return;
            }

            for (int i = index; i < candidates.size(); ++i) {
                // Skip duplicates
                if (i > index && candidates[i] == candidates[i - 1]) {
                    continue;
                }

                current.push_back(candidates[i]);
                dfs(candidates, target - candidates[i], i + 1, current, res);
                current.pop_back();
            }
        }
};