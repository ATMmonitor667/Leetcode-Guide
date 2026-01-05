class Solution {
public:
    int hammingWeight(int n) {
        int bitCount = 0;
        while(n)
        {
            if(n%2 == 1)
            {
                bitCount+=1;
            }
            n = n/2;
        }
        return bitCount;
        
    }
};