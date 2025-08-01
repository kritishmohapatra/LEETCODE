class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        mat=[]
        for r in range(numRows):
            arr=[]
            for i in range(r+1):
                if r==i or i==0:
                    arr.append(1)
                else:
                    arr.append(mat[r-1][i-1]+mat[r-1][i])
            mat.append(arr)
        return mat
        