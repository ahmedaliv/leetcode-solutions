class Solution:
    def compress(self, chars) -> int:
        cnt = 1
        newLen = 0 
        st_idx = 0 
        for i in range(len(chars)):
            if  i < len(chars) - 1 and chars[i]==chars[i+1]: 
                cnt+=1
            else:
                chars[st_idx] = chars[i]
                st_idx +=1
                
                if cnt == 1:
                    newLen +=1
                else:
                    newLen += len(str(cnt)) + 1
                    digits = list(map(int, str(cnt)))
                    for digit in digits:
                        chars[st_idx] = str(digit)
                        st_idx+=1
                cnt = 1
        return newLen