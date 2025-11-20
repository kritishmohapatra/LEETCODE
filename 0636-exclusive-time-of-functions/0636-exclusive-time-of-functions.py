class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n
        stack = []   # each element = [startTime, timeTakenByOthers]

        for log in logs:
            funcId_str, direction, timestamp_str = log.split(":")
            funcId = int(funcId_str)
            timestamp = int(timestamp_str)

            if direction == "start":
                # Push [startTime, timeTakenByOthers]
                stack.append([timestamp, 0])

            else:  # "end"
                startTime, timeTakenByOthers = stack.pop()

                # total runtime including children
                funcRunTime = timestamp - startTime + 1

                # exclusive time = total time - children time
                ans[funcId] += funcRunTime - timeTakenByOthers

                # Add this runtime to its parent (if exists)
                if stack:
                    stack[-1][1] += funcRunTime

        return ans