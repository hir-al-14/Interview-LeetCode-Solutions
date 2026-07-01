class Solution:
    def numDecodings(self, s: str) -> int:

        # Base case- as 0 is not a valid decosde and 01 or any other num is also not valid
        if s[0] == '0':
            return 0
        
        # decode_ways- number of ways to decode the first i characters of the string
        decode_ways = [0]*(len(s) + 1)
        decode_ways[0] = 1

        for i in range(2, len(s)+1):
            if decode_ways[i] == 0:
                continue

            # j is the length - either 1 or 2 length can be decoded
            for j in [1,2]:
                one = s[i:i+j]
                if i + j > len(s):
                    continue

                part = s[i:i+j]

                if (j == 1) and (part!='0'):
                    decode_ways[i+j] += decode_ways[i]
                elif (j == 2) and (10 <= int(part) <= 26):
                    decode_ways[i+j] += decode_ways[i]

        return decode_ways[len(s)] # Total ways to decode the entire string