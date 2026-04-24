class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> newSet = new HashSet<>();
        for(int number : nums){
            newSet.add(number);
        }
        return !(newSet.size() == nums.length);
    }
    
}