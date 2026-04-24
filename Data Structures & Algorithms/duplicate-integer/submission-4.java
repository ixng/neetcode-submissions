class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> newSet = new HashSet<>();
        for(int number : nums){
            if(newSet.contains(number)) return true;
            newSet.add(number);
        }
        return false;
    }
    
}