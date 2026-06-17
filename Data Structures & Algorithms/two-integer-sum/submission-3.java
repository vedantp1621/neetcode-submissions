class Solution {
    public int[] twoSum(int[] nums, int target) {
        //hashmap with all numbers
        //iterate through nums
        //check if target-nums[i] = any number in hashmap
        int[] result = new int[2];
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            map.put(nums[i], i);
        }
        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(target-nums[i]) && map.get(target-nums[i]) != i) {
                if (map.get(target-nums[i]) < i) {
                    result[0] = map.get(target-nums[i]);
                    result[1] = i;
                } else {
                    result[1] = map.get(target-nums[i]);
                    result[0] = i;
                }
             
                return result;
            }
        }
        return result;
    }
    
}
