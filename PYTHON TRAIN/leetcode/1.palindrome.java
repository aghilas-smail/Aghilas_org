public class Solution {
    public int removePalindromeSub(String s) {
        if (s.isEmpty()) {
            return 0; 
        } else if (isPalindrome(s)) {
            return 1; 
        } else {
            return 2; 
        }
    }
    
    private boolean isPalindrome(String s) {
        int left = 0;
        int right = s.length() - 1;
        
        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        
        return true;
    }
    
    public static void main(String[] args) {
        Solution solution = new Solution();
        
        System.out.println(solution.removePalindromeSub("ababa")); 
        System.out.println(solution.removePalindromeSub("abb")); 
        System.out.println(solution.removePalindromeSub("baabb")); 
    }
}