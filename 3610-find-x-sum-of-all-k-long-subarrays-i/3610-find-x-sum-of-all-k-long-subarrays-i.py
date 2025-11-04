from collections import Counter
import heapq
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        ans=[]
        l=0
        r=k
        while r<=len(nums):
            c=Counter(nums[l:r])
            t=x
            q=[]
            s=0
            frequency_list = [(key, frequency) for key, frequency in c.items()]

    # Sort the list by frequency in descending order, breaking ties by comparing keys
            sorted_frequency_list = sorted(frequency_list, key=lambda r: (r[1], r[0]))
            t=0
            for i in range(len(sorted_frequency_list)-1, -1,-1):
                if t>=x:
                    break
                s+=sorted_frequency_list[i][0]*sorted_frequency_list[i][1]
                t+=1
            ans.append(s)
                    
            
            l+=1
            r+=1
        return ans
            
            