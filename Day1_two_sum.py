class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.num_list =nums
        self.target = target
        terms =None
        # add the current term with all the sbusequent terms without repetition
        for first_term in range(len(self.num_list)-1):
            for second_term in range(first_term+1,len(self.num_list)):
                if self.num_list[first_term]+self.num_list[second_term] == self.target:
                    terms = [first_term,second_term]
        return terms
                    

        