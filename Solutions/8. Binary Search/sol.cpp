class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0 , r = nums.size() - 1 ;
        while(l < r)
        {
            int m = (l + r)>>1 ;
            if(nums[m] < target)
            {
                l = m + 1 ;
            }
            else
            {
                r = m ;
            }
        }
        if(nums[l] != target)
        {
            return -1 ;
        }
        return l ;
    }
};