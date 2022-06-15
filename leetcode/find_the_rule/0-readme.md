Group of problems that doesn't belong to any technique or pattern to solve. To solve it, you need to **find the rule**
Steps:
- Describe/Run the example by hand
- Find the rule, common pattern

Example: In zigzag conversion, the rule is: 
- row 0 or row last: index for next char is rows*2 - 2
- row in between: (row - row_index) * 2