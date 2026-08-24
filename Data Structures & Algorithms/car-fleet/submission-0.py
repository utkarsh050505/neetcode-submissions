class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stk = []

        cars = sorted(zip(position, speed), reverse=True)

        sorted_pos, sorted_speed = zip(*cars)

        for i in range(len(sorted_pos)):
            final_time = (target - sorted_pos[i]) / sorted_speed[i]
            if stk and stk[-1] >= final_time:
                continue
            else:
                stk.append(final_time)

        return len(stk)