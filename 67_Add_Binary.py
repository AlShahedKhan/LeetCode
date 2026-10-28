class Solution(object):
    def addBinary(self, a, b):
        decimal_sum = int(a ,2) + int (b,2)
        # print(decimal_sum)
        return bin(decimal_sum)[2:]

a = "1010"
b = "1100"
solution = Solution()
print(solution.addBinary(a, b))
