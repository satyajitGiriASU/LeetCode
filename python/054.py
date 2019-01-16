class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix in [[],[[]]]:
            return []
        m = len(matrix)
        n = len(matrix[0])
        i_visited = [-1,m]
        j_visited = [-1,n]
        
        i =0
        j = 0
        direction = 'right'
        
        output = []
        for l in range(m*n):
            output.append(matrix[i][j])
            if direction == 'right':
                if (j+1) not in j_visited:
                    j = j+1
                else:
                    direction = 'down'
                    i_visited.append(i)
            if direction == 'down':
                if (i+1) not in i_visited:
                    i = i+1
                else:
                    direction = 'left'
                    j_visited.append(j)
            if direction == 'left':
                if (j-1) not in j_visited:
                    j = j-1
                else:
                    direction = 'up'
                    i_visited.append(i)
            if direction == 'up':
                if (i-1) not in i_visited:
                    i = i-1
                else:
                    direction = 'right'
                    j_visited.append(j)
                    if (j+1) not in j_visited:
                        j = j+1
                    else:
                        direction = 'down'
                        i_visited.append(i)
        return output