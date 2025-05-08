class Solution:
    
    def compress(self, chars) -> int:
        def extract_digits(count:int):
            str_int = str(count)
            output = []
            for i in range(len(str_int)):
                output.append(str_int[i])
            return output
        read = 0
        write = 0
        while read < len(chars):
            c = chars[read]
            count = 0
            while read <len(chars) and c == chars[read]:
                read +=1
                count +=1
            chars[write] = c
            write +=1
            if count>1:
                for d in extract_digits(count):
                    chars[write] = d
                    write +=1
        return write