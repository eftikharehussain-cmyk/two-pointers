# stack mode
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if k >= len(s):
            return s[::-1]
        else:
            stack = []
            cnt = 0
            _chr = ''
            for i in s:
                if len(stack) < k:
                    stack.append(i)
                else:
                    if cnt % 2 == 0:
                        _chr += "".join(stack)[::-1]
                        stack = []
                        stack.append(i)
                        cnt += 1
                    else:
                        _chr += "".join(stack)
                        stack = []
                        stack.append(i)
                        cnt += 1
            if cnt % 2 == 0:
                _chr += "".join(stack)[::-1]
            else:
                _chr += "".join(stack)
            return _chr
        
        
# slicing mode
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        for i in range(0, len(s), 2 * k):
            s[i:i+k] = s[i:i+k][::-1]
        return "".join(s)