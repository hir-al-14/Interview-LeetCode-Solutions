class Solution:
    def numDecodings(self, s: str) -> int:
        count = 0
        is_valid = True

        # Base case- as 0 is not a valid decosde and 01 or any other num is also not valid
        if s[0] == '0':
            return 0
        for i in range(len(s)):
            for j in [0,1]:
                if i + j < len(s):
                    if (s[i] == '0'):
                        is_valid = True
                    elif (s[i+j] == '0'):
                        is_valid = True
                    else:
                        is_valid = True
            if is_valid:
                count += 1
        return count