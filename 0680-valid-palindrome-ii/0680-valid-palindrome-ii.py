class Solution(object):
    def validPalindrome(self, s):
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                # Try deleting s[l]
                left = l + 1
                right = r

                while left < right and s[left] == s[right]:
                    left += 1
                    right -= 1

                if left >= right:
                    return True

                # Try deleting s[r]
                left = l
                right = r - 1

                while left < right and s[left] == s[right]:
                    left += 1
                    right -= 1

                return left >= right

        return True

        