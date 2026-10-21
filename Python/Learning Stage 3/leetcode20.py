
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        elements = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for i in s:
            if i in "([{":
                stack.append(i)
            else:
                if stack and elements[i] == stack[-1]:
                    stack.pop()
                else:
                    return False

        return not stack
                    


sol = Solution()

print(sol.isValid("()"))        # Expected: True
print(sol.isValid("()[]{}"))    # Expected: True
print(sol.isValid("(]"))        # Expected: False
print(sol.isValid("([)]"))      # Expected: False
print(sol.isValid("{[]}"))     # Expected: True
print(sol.isValid("["))         # Expected: False
print(sol.isValid(""))          # Expected: True
print(sol.isValid("((()))"))    # Expected: True
print(sol.isValid("({[}])"))    # Expected: False
print(sol.isValid("(()"))       # Expected: False
print(sol.isValid("())"))       # Expected: False
