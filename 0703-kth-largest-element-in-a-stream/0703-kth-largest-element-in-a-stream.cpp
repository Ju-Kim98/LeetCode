class KthLargest {
public:
    KthLargest(int k, std::vector<int>& nums) :k(k) {
        for (int num : nums) {
            add(num);
        }
    }
    
    int add(int val) {
        if (minHeap.size() < k){
            minHeap.push(val);
        } else if (val > minHeap.top()) {
            minHeap.push(val);
            minHeap.pop();
        }
        
        return minHeap.top();
    }
    
    int k;
    std::priority_queue<int, std::vector<int>, std::greater<int>> minHeap;
    
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */