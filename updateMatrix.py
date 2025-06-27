# Time Complexity : O(m * n), where m and n are the dimensions of the matrix
# Space Complexity : O(m * n), for the queue and the output matrix
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Your code here along with comments explaining your approach

# I used multi-source BFS by adding all 0s to the queue initially and expanding outward to update distances

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        queue = deque()

        # Initialize matrix and queue with positions of all 0s
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r, c))
                else:
                    mat[r][c] = -1  # Mark unvisited 1s as -1

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # BFS traversal to update distances
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and mat[nr][nc] == -1:
                    mat[nr][nc] = mat[r][c] + 1
                    queue.append((nr, nc))

        return mat
