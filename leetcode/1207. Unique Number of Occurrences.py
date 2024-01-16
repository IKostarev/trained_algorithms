class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = []
        for i in arr:
            c.append(arr.count(i))
        return len(set(c)) == len(set(arr))