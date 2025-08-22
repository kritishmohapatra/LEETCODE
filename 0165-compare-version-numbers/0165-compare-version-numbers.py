class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        arr1=version1.split(".")
        arr2=version2.split(".")
        n=len(arr1)
        m=len(arr2)
        arr1=[int(i) for i in arr1]
        arr2=[int(i) for i in arr2]
        if n>m:
            for i in range(m, n):
                arr2.append(0)
        elif m>n:
            for i in range(n, m):
                arr1.append(0)
        for i in range(len(arr1)):
            if arr1[i]>arr2[i]:
                return 1
            elif arr2[i]>arr1[i]:
                return -1
        return 0