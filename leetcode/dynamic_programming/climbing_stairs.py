'''
Problem:
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Solution:
- Dynamic programming because can calculate ways of n = climbs(n-1) + climbs(n-2)
'''
class Solution:
	def climbStairs(self, n: int) -> int:
		climbs = {
			"0": 0, 
			"1": 1,
			"2": 2
		}
		if n <= 2:
			return climbs[f"{n}"]

		for i in range(3, n+1):
			n1 = climbs[f"{i-1}"]
			n2 = climbs[f"{i-2}"]
			climbs[f"{i}"] = n1 + n2
		
		return climbs[f"{n}"]
