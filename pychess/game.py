import pygame

x = 800
y = 800

screencolor = pygame.Color(200 , 200 , 200)
z = pygame.Color(250 , 250 , 0)

colorWhite = pygame.Color(250 , 250 , 250)
colorBrown = pygame.Color(150 , 150 , 100)

Y = pygame.display.set_mode([x , y])

def drawSquare(x , y , size, color):
    pygame.draw.rect(Y , color , [x , y , size , size])

def drawChessboard(sx, sy, size, n):
    boardColors = [colorWhite, colorBrown]
    counter = 0
    #n = n + 1
    for c in range(0 , n):
        for r in range(0, n):
            x = sx + c * size
            y = sy + r * size
            currencolor = boardColors[counter % 2]
            counter = counter + 1
            drawSquare(x, y, size, currencolor)
            pygame.display.flip()
        counter = counter + ((n + 1) % 2)

drawChessboard(10, 10, 80, 8)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()

    