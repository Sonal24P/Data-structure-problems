#Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring =""
        wordcountList =list()
        if s=="":
            return 0
        elif len(s)==1:
            return 1
        else:
            for limit in range(len(s)-1): 
                for index in range(limit,len(s)):
                    if s[index] not in substring: #create the sbstrings with non-repeative characters
                        substring+=s[index]
                    else:
                        wordcountList.append(len(substring))
                        substring=""
                        break
            wordcountList.append(len(substring))
            return max(wordcountList)
            
        