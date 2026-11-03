class Solution(object):
    def climbingStairs(self, n) -> int:
       prev, curr = 1, 1

       for _ in range(n):
           prev, curr = curr, prev + curr
       return prev
    # This is a fibonacci sequence pattern. It's a recurrence relation
    # ways(n) = ways(n - 1) + ways(n - 2)
            
solution = Solution()
print(solution.climbingStairs(5))