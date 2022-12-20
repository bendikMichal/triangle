import pygame, time, sys
from pygame.locals import *
from random import *

pygame.init()

width, height = 640, 480
win = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()
fps = 60

class Triangle:
    def __init__ (self, x, y, z, width, height):
        self.points = [x.copy(), y.copy(), z.copy()]
        self.next = self.points[0].copy()# [(y[0] - x[0]) / 2, (x[1] - z[1]) / 2]
        self.precision = 10

        self.triangle = pygame.Surface((width, height))
        self.triangle.set_colorkey((0, 0, 0))
        pygame.draw.lines(self.triangle, (255, 255, 255), True, self.points)

    def drawNext (self, i = 0):
        point = self.points[randint(0, len(self.points) - 1)].copy()
        nextP = [self.next[0] + (point[0] - self.next[0]) / 2, self.next[1] + (point[1] - self.next[1]) / 2]
        self.next = nextP.copy()

        pygame.draw.rect(self.triangle, (255, 255, 255), (nextP[0], nextP[1], 1, 1))

        if i < self.precision:
            self.drawNext(i + 1)

    def clear (self):
        self.triangle.fill((0, 0, 0))
        pygame.draw.lines(self.triangle, (255, 255, 255), True, self.points)

t = Triangle([200, 200], [400, 200], [300, 0], width, height)
main = True

while main:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main = False

    t.drawNext()

    win.fill((0, 0, 0))
    win.blit(t.triangle, (0, 0))
    pygame.display.update()


pygame.quit()
sys.exit()
