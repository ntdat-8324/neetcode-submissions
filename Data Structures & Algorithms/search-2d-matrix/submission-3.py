class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col_n = len(matrix)

        for c in range(col_n):
            l = 0
            r = len(matrix[0])-1

            if target > matrix[c][r]:
                continue
            elif target < matrix[c][l]:
                return False
            
            while l <= r:
                m = int(l + (r-l)/2)

                if  matrix[c][m] == target:
                    return True
                elif target > matrix[c][m]:
                    l = m+1
                else: r = m - 1
        return False