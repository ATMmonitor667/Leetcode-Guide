class KthLargest {
private:
    int k;
    std::priority_queue<int, std::vector<int>, std::greater<int>> pq; // min-heap
public:
    KthLargest(int k, std::vector<int>& nums) : k(k) {
        for (int x : nums) {
            pq.push(x);
            if ((int)pq.size() > k) pq.pop();
        }
    }

    int add(int val) {
        pq.push(val);
        if ((int)pq.size() > k) pq.pop();
        return pq.top(); // kth largest
    }
};
/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */