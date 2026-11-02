class Solution(object):
    def climbingStairs(self, n) -> int:
        if n == 0 or n == 1:
            return 1

        result = self.climbingStairs(n -1) + self.climbingStairs(n -2)

        return result
solution = Solution()
print(solution.climbingStairs(10))