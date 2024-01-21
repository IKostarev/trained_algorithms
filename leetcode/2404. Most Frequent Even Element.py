class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        maxx = 0
        even_element = -1
        d={}

        for i in nums:
            if i % 2 == 0:
                if i not in d:d[i] = 1 
                else:
                    d[i] += 1
        
        for val,count in d.items():
            if count > maxx:
                maxx = count
                even_element = val 
            elif count == maxx:
                if even_element > val:
                    even_element = val
        return even_element