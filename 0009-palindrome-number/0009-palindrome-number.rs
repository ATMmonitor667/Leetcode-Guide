impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        if x < 0
        {
            return false
        }
        let mut  num: i32= x;
            if num < 10 {
        return true;  // Single digit numbers are palindromes
    }

    let original = num;
    let mut reversed = 0;

    while num > 0 {
        reversed = reversed * 10 + num % 10;
        num /= 10;
    }

    original == reversed

    }
}