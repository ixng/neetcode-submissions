class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> newNums = new HashSet<>();
        for(int i = 0; i < nums.length ; i++){
            newNums.add(nums[i]);
        }
        if( newNums.size() == nums.length){
            return false;
        }
        return true; 
    }
    
}