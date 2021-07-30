class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        output = []
        for i in range(len(asteroids)):
            current_asteroid_exploded = False
            while len(output) != 0 and asteroids[i] < 0 and output[-1] > 0:
                if -asteroids[i] > output[-1]:
                    output.pop()
                elif -asteroids[i] == output[-1]:
                    output.pop()
                    current_asteroid_exploded = True
                    break
                elif -asteroids[i] < output[-1]:
                    current_asteroid_exploded = True
                    break
            if not current_asteroid_exploded:
                output.append(asteroids[i])
        return output

