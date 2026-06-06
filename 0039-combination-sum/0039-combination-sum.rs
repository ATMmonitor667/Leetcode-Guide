impl Solution {
    pub fn combination_sum(candidates: Vec<i32>, target: i32) -> Vec<Vec<i32>> {
        let mut result: Vec<Vec<i32>> = Vec::new();
        let mut path: Vec<i32> = Vec::new();

        fn dfs(
            index: usize,
            remaining: i32,
            candidates: &Vec<i32>,
            path: &mut Vec<i32>,
            result: &mut Vec<Vec<i32>>,
        ) {
            if remaining == 0 {
                result.push(path.clone());
                return;
            }

            if index == candidates.len() || remaining < 0 {
                return;
            }

            path.push(candidates[index]);

            dfs(index, remaining - candidates[index], candidates, path, result);

            path.pop();

            dfs(index + 1, remaining, candidates, path, result);
        }

        dfs(0, target, &candidates, &mut path, &mut result);

        result
    }
}