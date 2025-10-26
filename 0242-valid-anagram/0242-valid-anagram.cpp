class Solution {
public:
    bool isAnagram(string s, string t) {
        string s1 = s;
        string s2 = t;
         if(s1.length() != s2.length()) return false;
  unordered_map<char,int>mp;
  for(char c : s1)
  {
    mp[c]++;
  }
  for(char c : s2)
  {
    if(mp.find(c) == mp.end() || mp[c] == 0)
    {
      return false;
    }
    mp[c]--;
  }
  return true;
    }
};