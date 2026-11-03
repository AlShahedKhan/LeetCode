class Solution(object):
    def climbingStairs(self, n) -> int:
       prev, curr = 1, 1

       for _ in range(n):
           prev, curr = curr, prev + curr
       return prev
            
solution = Solution()
print(solution.climbingStairs(5))