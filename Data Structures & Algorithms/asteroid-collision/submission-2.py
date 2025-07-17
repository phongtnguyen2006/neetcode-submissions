class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        s = []

        for i in range(len(asteroids)):
            while asteroids[i] < 0 and s and s[-1] > 0:
                curr = s[-1]
                if abs(asteroids[i]) > curr:
                    s.pop()
                elif abs(asteroids[i]) == curr:
                    s.pop()
                    break
                elif abs(asteroids[i]) < curr:
                    break
            else:
                s.append(asteroids[i])

        return s