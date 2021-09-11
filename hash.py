
class GetHashCode:
 
    def convert_n_bytes(self,n, b):
        bits = b*8
        return (n + 2**(bits-1)) % 2**bits - 2**(bits-1)
 
    def convert_4_bytes(self,n):
        return self.convert_n_bytes(n, 4)
    @classmethod
    def getHashCode(cls,s):
        h = 0
        n = len(s)
        for i, c in enumerate(s):
            h = h + ord(c)*31**(n-1-i)
        return cls().convert_4_bytes(h)
 
if __name__ == "__main__":
    ## 替换成对应活动的盐值
    salt = 'salt'
    deviceID = '130'
    text = deviceID + '_' + salt
    hashCode = GetHashCode.getHashCode(text)
    print(hashCode)
