# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot(object):
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

class Solution(object):
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        # Direction vectors for moving: up, right, down, left (clockwise)
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # (dx, dy)
        visited = set()
        
        def go_back():
            # Makes the robot move back to the previous cell it was in
            robot.turnLeft()
            robot.turnLeft()
            robot.move()
            robot.turnLeft()
            robot.turnLeft()

        def dfs(x, y, d):
            # Mark the current cell as visited and clean it
            visited.add((x, y))
            robot.clean()
            
            # Explore all four directions
            for i in range(4):
                new_d = (d + i) % 4
                new_x = x + directions[new_d][0]
                new_y = y + directions[new_d][1]
                
                if (new_x, new_y) not in visited:
                    # Try to move in the current facing direction
                    if robot.move():
                        dfs(new_x, new_y, new_d)
                        # Backtrack to the previous position and orientation
                        go_back()
                
                # Turn the robot to the next direction
                robot.turnRight()

        # Start the DFS from the initial robot position and orientation 0 (facing up)
        dfs(0, 0, 0)