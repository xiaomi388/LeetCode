# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """

        visited = set()
        dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))

        def dfs(r, c, dir):
            if (r, c) in visited:
                return
            visited.add((r, c))
            robot.clean()
            for i in range(4):
                dr, dc = dirs[(dir+i)%4]
                for q in range(i):
                    robot.turnRight()
                if robot.move():
                    dfs(r+dr, c+dc, (dir+i)%4)
                    robot.turnRight()
                    robot.turnRight()
                    robot.move()
                    robot.turnRight()
                    robot.turnRight()
                for q in range(i):
                    robot.turnLeft()
        dfs(0, 0, 0)
