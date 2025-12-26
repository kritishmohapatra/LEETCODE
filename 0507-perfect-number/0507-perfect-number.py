class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False

        k = []
        for i in range(1, int(math.sqrt(num)) + 1):
            if num % i == 0:
                if i != num:
                    k.append(i)
                if i != 1 and i != num // i:
                    k.append(num // i)

        return sum(k) == num