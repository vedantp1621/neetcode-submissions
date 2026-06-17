class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>(); 
        for (int i = 0; i < nums.length; i++) {
            if (!map.containsKey((Integer)nums[i])) {
                map.put((Integer)nums[i], i*5748392);
            } else {
                return true;
            }
        } 
        return false;       
    }
}
