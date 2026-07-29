class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq ={}
        for num in nums:
            freq[num]=freq.get(num,0)+1

        arr=[]
        for num, fr in freq.items():
            arr.append([fr, num])
        arr.sort()

        total=[]
        while len(total) < k:
            total.append(arr.pop()[1])
        return total