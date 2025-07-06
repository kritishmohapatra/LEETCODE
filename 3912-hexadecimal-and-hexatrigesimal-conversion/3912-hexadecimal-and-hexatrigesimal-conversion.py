class Solution:
    def concatHex36(self, n: int) -> str:
        def to_base(x, b):
            if x == 0: return "0"
            d, res = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ", []
            while x: res.append(d[x % b]); x //= b
            return "".join(res[::-1])
        return to_base(n * n, 16) + to_base(n * n * n, 36)