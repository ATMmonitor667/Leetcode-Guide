class Solution {
public:
    int largestAltitude(vector<int>& gain) {
       vector <int> prefix(gain.size()+1, 0);
       int max = INT_MIN;
        prefix[0] = 0;
        for(int i = 0 ; i < gain.size(); i++)
        {
            prefix[i+1] = prefix[i]+gain[i];
            if(prefix[i]> max)
            {
                max = prefix[i];
            }
        }
        if(max < prefix[prefix.size()-1])
        {
            max = prefix[prefix.size()-1];
        }
        
        return max;
    }
};