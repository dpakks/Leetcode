class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        output = []
        for i,v in enumerate(nums):
            if v not in d:
                d[v] = 1
            else:
                d[v] += 1
        while k > 0:
            top = max(d, key=d.get)
            output.append(top)
            d.pop(top)
            k -= 1
        return output
        