impl Solution {
    pub fn generate_parenthesis(n: i32) -> Vec<String> {
        fn valid(s: &str) -> bool {
            let mut count = 0;

            for c in s.chars() {
                if c == '(' {
                    count += 1;
                } else {
                    count -= 1;
                }

                if count < 0 {
                    return false;
                }
            }

            count == 0
        }

        fn dfs(
            index: i32,
            n: i32,
            path: &mut String,
            result: &mut Vec<String>,
        ) {
            if index == 2 * n {
                if valid(path) {
                    result.push(path.clone());
                }
                return;
            }

            path.push('(');
            dfs(index + 1, n, path, result);
            path.pop();

            path.push(')');
            dfs(index + 1, n, path, result);
            path.pop();
        }

        let mut result = Vec::new();
        let mut path = String::new();

        dfs(0, n, &mut path, &mut result);

        result
    }
}