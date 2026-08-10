class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        num1 = version1.split(".")
        num1 = [str(i) for i in num1]

        num2 = version2.split(".")
        num2 = [str(i) for i in num2]
        length = min(len(num1), len(num2))
        print(int("001"))
        for i in range(length):
            n1 = int(num1[i])
            n2 = int(num2[i])
            if n1 > n2:
                return 1
            elif n2 > n1:
                return -1
                
        if len(num2) > len(num1):
            for i in range(length, len(num2)):
                if int(num2[i]) != 0:
                    return -1
        if len(num1) > len(num2):
            for i in range(length, len(num1)):
                if int(num1[i]) != 0:
                    return 1
        return 0 