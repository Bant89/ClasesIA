

def initialize():
  size = 10
  blockedCells = {
    3: [2, 3, 4, 5, 6],
    4: [1],
    5: [2, 6]
  }
  origin_point = [5, 3]
  destination_point = [2, 2]

  matrix = [[0 for i in range(size)] for j in range(size)]


  for i in range(size):
    for j in range(size):
      matrix[i][j] = 0

  for k in blockedCells:
    for v in blockedCells[k]:
      matrix[k][v] = -1


  matrix[origin_point[0]][origin_point[1]] = 1
  matrix[destination_point[0]][destination_point[1]] = 2

  return matrix

initial_matrix = initialize()

print(initial_matrix)