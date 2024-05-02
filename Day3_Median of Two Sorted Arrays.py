#Median of Two Sorted Arrays

class Solution:
    def findMedianSortedArrays(self, list1: List[int], list2: List[int]) -> float:
        finalist = list1+list2 # concate two lists
        for limit in range(len(finalist)-1):
            for index in range(limit+1,len(finalist)): 
                if finalist[limit]>finalist[index]:
                    finalist[limit],finalist[index]=finalist[index],finalist[limit] #sort the finalList
        index = len(finalist)//2
        if len(finalist)%2==0:
            return (finalist[index-1]+finalist[index])/2 # median for the list with even length
        else:
            return finalist[index] # median for the list with odd length
            