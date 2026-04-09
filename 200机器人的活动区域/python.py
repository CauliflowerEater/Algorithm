"""
染色求最大同色区域；

"""

def paint(grid, colorGrid, x, y, color, prevValue, colorMap):
    if x<0 or x>=len(grid) or y<0 or y>=len(grid[0]):
        return
    if colorGrid[x][y]!=0:
        return
    if abs(grid[x][y]-prevValue)>1:
        return
    colorGrid[x][y]=color
    colorMap[color]+=1;
    paint(grid, colorGrid, x+1, y, color, grid[x][y], colorMap)
    paint(grid, colorGrid, x-1, y, color, grid[x][y], colorMap)
    paint(grid, colorGrid, x, y+1, color, grid[x][y], colorMap)
    paint(grid, colorGrid, x, y-1, color, grid[x][y], colorMap)

def main():
    grid=[[1, 2, 3], [3, 2, 1], [1, 2, 3]]
    colorGrid=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    colorMap={}
    color=1
    maxColor=0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if colorGrid[i][j]!=0:
                continue
            colorMap[color]=0
            paint(grid, colorGrid, i, j, color, grid[i][j], colorMap)
            maxColor=max(maxColor, colorMap[color])
            color+=1
    print(maxColor)


if __name__ == "__main__":
    main()