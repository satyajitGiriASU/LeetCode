class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        if target is None:
            return False
        
        m = len(matrix)-1
        if m < 0:
            return False
        n = len(matrix[0])-1
        if n < 0:
            return False

        
        if target <matrix[0][0] or target > matrix[m][n]:
            return False
        
        #find which row
        i = 0 
        j = m
        
        rows_search = []
        while True:
            midrow = (i+j)/2
            if midrow in rows_search:
                return False
            else:
                rows_search.append(midrow)
            if matrix[midrow][0]>target:
                j = midrow-1
            elif matrix[midrow][n]<target:
                i = midrow+1
            else:
                break

        print(matrix[midrow][:])    
        i = 0 
        j = n
        exitFlag = False
        while not exitFlag:
            exitFlag = (i>=j)
            midcol = (i+j)/2
            print(matrix[midrow][midcol])
            if matrix[midrow][midcol]>target:
                j = midcol-1
            elif matrix[midrow][midcol]<target:
                i = midcol+1
            else:
                return True
            
            
        return False
    