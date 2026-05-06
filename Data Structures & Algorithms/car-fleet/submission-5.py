class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # (target - current_position) / speed
        cars = sorted(zip(position, speed), reverse=True)
        fleets, cur_time = 0, 0
        
        for p, s in cars:
            time = float((target-p)/s)
            print(time)
            if cur_time < time:
                fleets += 1
                cur_time = time
        
        return fleets