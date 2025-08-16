class Solution:
    def maximum69Number (self, num: int) -> int:
        num=list(str(num))
        k=-1
        if "6" in num:
            k=num.index("6")
        if k==-1:
            return int("".join(num))
        else:
            num[k]="9"
            return int("".join(num))

        