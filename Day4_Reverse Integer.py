class Solution:
    def reverse(self, x: int) -> int:
        num=abs(x)
        rev=0
        if x!=0:
            while num>0:
                digit=num%10 #find the last digit
                rev=rev*10+digit #create reverse number
                num//=10 #update the original number
            if x>0 and rev<=(2**31-1):
                return rev
            elif x<0 and -rev>=-(2**31):
                return -rev
            else:
                return 0
        else:
            return 0
        