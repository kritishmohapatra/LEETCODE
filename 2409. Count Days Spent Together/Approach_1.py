class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days=[31, 28, 31, 30,31, 30, 31, 31, 30, 31, 30,31]
        def conv(date):
            m, d=map(int, date.split("-"))
            return sum(days[:m-1])+d
        a1=conv(arriveAlice)
        a2=conv(leaveAlice)
        b1=conv(arriveBob)
        b2=conv(leaveBob)

        s=max(a1, b1)
        e=min(a2, b2)

        return max(0, e-s+1)