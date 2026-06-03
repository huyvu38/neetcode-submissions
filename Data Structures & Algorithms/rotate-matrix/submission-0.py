class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        l = 0
        r = len(matrix) - 1
        #Flip row
        while l < r:
            matrix[l], matrix[r] = matrix[r], matrix[l]
            l = l + 1
            r = r - 1

        #Flip column
        for i in range(len(matrix)):
            for j in range (i):
              matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        