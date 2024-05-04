class Solution:
    def myAtoi(self, s1: str) -> int:
        s= s1.lstrip()
        integer = 0
        try:
            integer =int(s) 
        except:
            for index in range(len(s)-1):       
                try :
                    integer = int(s[:index+1]) # convert string to int if possible
                except:
                     pass
        if integer<(-2**31):
            return (-2**31)
        elif integer>(2**31-1):
            return (2**31-1)
        else:
            return integer
        