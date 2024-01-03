#Minimum Time to Visit all Points
"""
On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi]. Return the minimum time in seconds to visit all the points in the order given by points.
You can move according to these rules:
In 1 second, you can either:
move vertically by one unit,
move horizontally by one unit, or
move diagonally sqrt(2) units (in other words, move one unit vertically then one unit horizontally in 1 second).
You have to visit the points in the same order as they appear in the array.
You are allowed to pass through points that appear later in the order, but these do not count as visits.

Strategy:
- initiate the steps value as zero.
- since we can only move one step at a time the steps we need to take is the substraction between the start and the end point.
- since we need to move in the x and the y axis the steps we need to perform is the maximum between the substraction in the x and y axis. 
"""
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        steps=0
        for n in range(len(points)-1):
            point1=points[n]
            point2=points[n+1]
            steps+=max(abs(point1[0]-point2[0]),abs(point1[1]-point2[1]))
        return steps