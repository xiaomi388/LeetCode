# position = [10, 8, 0, 5, 3]
# position = []
# speed    = [2,  4, 1, 1, 3]
# arr_time = [1,  1,12, 7, 3]

# position = [0,|3, 5,|8, 10]
# arr_time = [12,| 3, 7,| 1,  1]
# ans = 3


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        times = [ (target - pos) / spd for pos, spd  in cars]
        i = len(cars) - 1
        counter = 0
        while i >= 0:
            q = i - 1
            while q >= 0 and times[q] <= times[i]:
                q -= 1
            counter += 1
            i = q
        return counter


