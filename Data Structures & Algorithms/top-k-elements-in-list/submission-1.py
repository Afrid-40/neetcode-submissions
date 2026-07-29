class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for key in nums:
            freq[key]= freq.get(key,0)+1

        arr=[]
        for key,fr in freq.items():
            arr.append([fr,key])
        arr.sort()

        total=[]
        while len(total) <k:
            total.append(arr.pop()[1])
        return total