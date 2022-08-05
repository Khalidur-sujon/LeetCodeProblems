class solution:
    def encode(self, str):
        res = ''
        for c in str:
            res += str(len(c))+ '#' + c
        return res

    def decode(self, str):
        res, i = [], 0
        
        while i < len(str):
            j = i
            while str[j] != '#':
                j += 1
            length = int(str[i:j])
            res.append(str[j+1 : j + 1 + length])
            i = j + 1 + length
        return res
