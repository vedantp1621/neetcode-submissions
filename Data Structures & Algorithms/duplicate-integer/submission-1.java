class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap map = new HashMap();
        for (int i = 0; i < nums.length; i++) {
            if (!map.containsKey((Integer)nums[i])) {
                map.put((Integer)nums[i], i);
            }
        }
        return map.size() != nums.length;
    }
}
