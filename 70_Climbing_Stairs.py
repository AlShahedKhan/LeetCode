class Solution(object):
    def climbingStairs(self, n) -> int:
        if n < 2:
            return 1
        if n == 2:
            return 2
        if n > 2:
            return self.climbingStairs(n -1) + self.climbingStairs(n -2)
            
solution = Solution()
print(solution.climbingStairs(5))