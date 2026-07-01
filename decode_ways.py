class Solution:
    def numDecodings(self, s: str) -> int:
        count = 0
        is_valid = True

        # Base case- as 0 is not a valid decosde and 01 or any other num is also not valid
        if s[0] == '0':
            return 0

        for i in range(len(s)):
            # j is the length - either 1 or 2 length can be decoded
            for j in [1,2]:
                if i + j > len(s):
                    continue

                part = s[i:i+j]

                if (j == 1) and (part!='0'):
                    is_valid = True
                elif (j == 2) and (10 <= int(part) <= 26):
                    is_valid = True

            if is_valid:
                count += 1
        return count