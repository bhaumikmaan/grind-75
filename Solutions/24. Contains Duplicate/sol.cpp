class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        map<int,int> m ;
        for(auto i:nums)
        {
            m[i]++ ;
        }
        for(auto i:m)
        {
            if(i.second > 1)
            {
                return true ;
            }
        }
        return false ;
    }
};