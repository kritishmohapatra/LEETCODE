class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def rightgreater(nums):
            stack=[]
            result=[]
            for i in range(len(nums2)-1, -1, -1):
                while(len(stack)>0 and nums2[i]>=stack[-1]):
                    stack.pop()
                if len(stack)==0:
                    result.append(-1)
                    stack.append(nums2[i])
                else:
                    result.append(stack[-1])
                    stack.append(nums2[i])
            return result[::-1]
        res=rightgreater(nums2)
        output=[]
        for i in nums1:
            if i in nums2:
                ind=nums2.index(i)
                output.append(res[ind])
        return output




