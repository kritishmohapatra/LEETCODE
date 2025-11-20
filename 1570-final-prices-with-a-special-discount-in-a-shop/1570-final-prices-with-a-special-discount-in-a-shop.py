class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans=prices.copy()
        st=[]
        for i, p in enumerate(prices):
            while st and prices[st[-1]]>=p:
                ans[st.pop()]-=p
            st.append(i)
        return ans