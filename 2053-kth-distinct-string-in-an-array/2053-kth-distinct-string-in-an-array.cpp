class Solution {
public:
    string kthDistinct(vector<string>& arr, int k) {
        unordered_map<string, int> freqMap;
        
        for(string& str:arr) {
            freqMap[str]++;
        }
        
        for(string& str:arr) {
            if(freqMap[str]==1) {
                k--;
            }
            if(k==0) {
                return str;
            }
        }
        
        return "";
    }
};