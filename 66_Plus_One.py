class Solution(object):
    def plusOne(self, digits):
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                print(digits)
            else:
                digits[i] = 0
        digits.insert(0,1)
        print(digits)

solution = Solution()
solution.plusOne([2,5,9,9,9,9])