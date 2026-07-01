class Solution:
    def numDecodings(self, s: str) -> int:
        all_encoding=[]
        def decode(c):
            char = chr(ord('a')+int(c)-1)
        for i in range(len(s)):
            for j in [1,2]:
                if (s[i] == 0):
                    all_encoding[i] = decode(s[i+j])
                elif (s[i+j] == 0):
                    all_encoding[i] = decode(s[i])
                else:
                    all_encoding[i] = decode(s[i:(i+j)])
        return len(all_encoding)