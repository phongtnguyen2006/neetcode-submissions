class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        import math
        #make a list of tuples and sort by position
        cars = list(zip(position, speed))
        cars.sort()
        ct = 0

        while cars:
            ct += 1
            curr = cars.pop()
            time = (target - curr[0]) / curr[1]
            while cars:
                prior_car = cars[-1]
                if ((target - prior_car[0]) / prior_car[1]) <= time:
                    cars.pop()
                else:
                    break

        return ct

