# import math
# class Solution(object):
#     def mySqrt(self, x):      
#         print(math.isqrt(x))
# solution = Solution()
# solution.mySqrt(8)
class Solution(object):
    def mySqrt(self, x) -> int:
        if(x < 0):
            print("Not a number")
        if(x == 0):
            return 0
        guess = x / 2.0

        while True:
            better_guess = 0.5 * (guess + (x / guess))

            if abs(better_guess - guess) < 0.000001:
                break

            guess = better_guess
            
        print(int(better_guess))

solution = Solution()
solution.mySqrt(12)
