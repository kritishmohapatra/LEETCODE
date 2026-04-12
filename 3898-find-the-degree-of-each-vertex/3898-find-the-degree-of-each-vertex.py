class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        vertex_degrees = []
        total_nodes = len(matrix)
        
        for i in range(total_nodes):
            connections = 0
            for j in range(total_nodes):
                if matrix[i][j] == 1:
                    connections += 1
            vertex_degrees.append(connections)
            
        return vertex_degrees