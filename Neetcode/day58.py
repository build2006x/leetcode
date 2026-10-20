### hey hi today i am working on K-th Symbol in Grammar
n=30
k=536870912
# number = "0"
# pointer = 0
# res = ""

# while pointer < n-1:
#         for i in number:
#                 if int(i) == 0:
#                     res +="01"
#                 else:
#                     res +="10"
#         number = res
#         res = ""
#         pointer +=1


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # Base Case: The first row always starts with 0
        if n == 1:
            return 0
        
        # Find the parent's value in the previous row
        parent = self.kthGrammar(n - 1, (k + 1) // 2)
        
        # If k is odd, it's a left child (same as parent)
        if k % 2 != 0:
            return parent
        # If k is even, it's a right child (flipped parent value)
        else:
            return 1 - parent

Sol = Solution()

i = Sol.kthGrammar(4,5)
print(i)













