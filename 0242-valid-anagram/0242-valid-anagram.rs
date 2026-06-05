use std::collections::HashMap;

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        let mut map = HashMap::new();

        for letter in s.chars() {
            *map.entry(letter).or_insert(0) += 1;
        }

        for letter in t.chars() {
            *map.entry(letter).or_insert(0) -= 1;
        }

        for (_, v) in map {
            if v != 0 {
                return false;
            }
        }

        true
    }
}