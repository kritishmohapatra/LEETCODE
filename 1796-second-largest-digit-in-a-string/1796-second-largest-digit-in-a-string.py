class Solution:
    def secondHighest(self, arr: str) -> int:
        sl=-1
        l=-1
        for i in range(len(arr)):
            if arr[i].isdigit():
                if int(arr[i])>l:
                    sl=l
                    l=int(arr[i])
                elif int(arr[i])<l and int(arr[i])>sl:
                    sl=int(arr[i])
        return sl