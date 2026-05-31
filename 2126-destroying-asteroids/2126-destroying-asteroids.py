class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        asteroids.sort()
        for aster in asteroids:
            if mass < aster:
                return False
            mass += aster
        return True