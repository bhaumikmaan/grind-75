class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2:
            return False
        stack = [None]
        closed = {'(' : ')' , '{' : '}' , '[' : ']'}
        
        for bracket in s:
            if bracket in closed.keys():
                stack.append(closed[bracket])
            else:
                if bracket != stack.pop():
                    return False
                
        return stack == [None]