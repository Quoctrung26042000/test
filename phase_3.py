from typing import List

class IslandCounter:
    def __init__(self):
        self.visited = set()

    def count_islands(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if (i, j) in self.visited or i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
                return
            self.visited.add((i, j))
            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(i + x, j + y)

        if not grid:
            return 0

        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in self.visited:
                    num_islands += 1
                    dfs(i, j)
        return num_islands

# Convert input data to integers
image = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]


image = [[int(pixel) for pixel in row] for row in image]

island_counter = IslandCounter()
print("Number of islands:", island_counter.count_islands(image))
