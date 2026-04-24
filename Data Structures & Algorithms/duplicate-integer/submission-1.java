class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> newNums = new HashSet<>();
        for(int i = 0; i < nums.length ; i++){
            if(newNums.contains(nums[i])){
                return true;
            }
            newNums.add(nums[i]);
        
        }
        return false;
        
        
    }
    
}