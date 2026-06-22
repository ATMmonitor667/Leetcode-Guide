class Solution(object):
    def totalWaviness(self, num1, num2):
        def waveyCount(num):
            count = 0
            while num >= 100:
                digit1 = num % 10
                digit2 = (num % 100) // 10
                digit3 = (num % 1000) // 100

                if (digit2 > digit1 and digit2 > digit3) or \
                   (digit2 < digit1 and digit2 < digit3):
                    count += 1

                num //= 10

            return count

        count = 0
        for i in range(num1, num2 + 1):
            count += waveyCount(i)

        return count


