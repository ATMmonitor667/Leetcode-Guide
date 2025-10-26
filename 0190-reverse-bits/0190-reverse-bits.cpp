class Solution {
public:
    int reverseBits(int n) {
        unsigned int rev = 0;  

        for (int i = 0; i < 32; i++) {
            int bit = n & 1;      
            rev = (rev << 1) | bit; 
            n >>= 1;             
        }
        return rev;
        
    }
};