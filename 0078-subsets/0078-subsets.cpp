class Solution {
public:
    template <typename T>
    class SuperVector {
    private:
        std::vector<T> data;

    public:
        SuperVector() = default;

        SuperVector(const std::vector<T>& vec)
            : data(vec) {}

        SuperVector(std::initializer_list<T> vals)
            : data(vals) {}

        void append(const T& value) {
            data.push_back(value);
        }

        void pop() {
            if (!data.empty())
                data.pop_back();
        }

        SuperVector& operator+=(const SuperVector& other) {
            for (const auto& v : other.data) {
                data.push_back(v);
            }
            return *this;
        }

        SuperVector operator+(const SuperVector& other) const {
            SuperVector result = *this;
            result += other;
            return result;
        }

        size_t size() const {
            return data.size();
        }

        std::vector<T> getData() const {
            return data;
        }
    };

    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> result;

        auto dfs = [&](auto&& dfs, int index, SuperVector<int> path) -> void {
            if (index == nums.size()) {
                auto value = path.getData();
                result.push_back(value);
                return;}

            dfs(dfs,index + 1,path + SuperVector<int>{nums[index]});
            dfs(dfs,index + 1,path);
        };

        dfs(dfs, 0, SuperVector<int>{});

        
      

        return result;
    }
};