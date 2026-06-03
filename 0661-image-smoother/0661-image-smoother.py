class Solution(object):
    def imageSmoother(self, img):
        n = len(img)
        m = len(img[0])
        direction = [
            (-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)
        ]
        ans = [[0] * m for i in range(n)]
        avg = 0
        for i in range(n):
            for j in range(m):
                c = 1
                sum1 = 0
                for x,y in direction:
                    nx,ny = i + x,j + y
                    if nx >= 0 and nx < n and ny >= 0 and ny <m:
                        sum1 += img[nx][ny]
                        c += 1
                avg = (sum1 + img[i][j]) // c
                ans[i][j] = avg
        return ans

        