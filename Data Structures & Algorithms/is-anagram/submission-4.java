class Solution {
    public boolean isAnagram(String s, String t) {
       HashMap<Character, Integer> mapS = new HashMap<>();
       HashMap<Character, Integer> mapT = new HashMap<>();

        if (s.length() != t.length()) {
            return false;
        }

        for (int i = 0; i < s.length(); i++) {
            mapS.put(s.charAt(i), mapS.getOrDefault(s.charAt(i),0)+1);
            mapT.put(t.charAt(i), mapT.getOrDefault(t.charAt(i),0)+1);
        }



        return mapS.equals(mapT);
    }
}
