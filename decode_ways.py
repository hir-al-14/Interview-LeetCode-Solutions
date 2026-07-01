class Solution:
    def numDecodings(self, s: str) -> int:

        # Base case- as 0 is not a valid decosde and 01 or any other num is also not valid
        if s[0] == '0':
            return 0
        
        # everytime we need to keep track of the previous and previous-1 character's ways
        # second_last = ways to decode up to 2 positions before current
        # last = ways to decode up to 1 position before current
        second_last = 1
        last = 1

        for i in range(2, len(s)+1):
            current = 0

            # j is the length - either 1 or 2 length can be decoded
            for j in [1,2]:
                one = s[i:i+j]
                if i + j > len(s):
                    continue

                part = s[i-j:i]

                if (j == 1) and (part!='0'):
                    current += last
                elif (j == 2) and (10 <= int(part) <= 26):
                    current += second_last
                
            second_last = last
            last = current

        return last # Total ways to decode the entire string