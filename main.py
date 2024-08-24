import pygame
from pygame_screen_record import ScreenRecorder
import os

pygame.init()
WIDTH, HEIGHT = 480, 854
win = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
clock = pygame.time.Clock()

sortable = []
if os.path.exists("random_num.txt"):
    with open("random_num.txt", "r") as file:
        for line in file:
            sortable.append(int(file.readline()))
        file.close()

    print(sortable)

max_sort = 0
for i in sortable:
    if i > max_sort:
        max_sort = i
tiles = []

recorder = ScreenRecorder(10)


class Tile:
    def __init__(self, list, value, pos, gap):
        self.list = list
        self.value = value
        self.pos = pos
        self.gap = gap
        self.surf = pygame.Surface((50, 720 / max_sort * value))
        self.px_per = 720 / max_sort
        self.width = (720 - gap * (len(list) + 1)) / len(list)

    def draw(self):
        rect = [self.pos*self.width + (self.pos + 1) * self.gap, 720-self.value * self.px_per, self.width, self.value * self.px_per]
        pygame.draw.rect(win, (100, 255, 100), rect)

gap = 0
for i in sortable:
    tiles.append(Tile(sortable, i, sortable.index(i), gap))

# Create the Tile objects before the main loop
tiles = [Tile(sortable, i, index, gap) for index, i in enumerate(sortable)]

running = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = not running
                recorder.start_rec()
            if event.type == pygame.K_ESCAPE:
                pygame.quit()
                quit()
                running = False

    if sortable == sorted(sortable):
        print("Sorted!")
        running = False
        recorder.stop_rec()
        recorder.save_recording("recording.mp4")

    if running:
        win.fill((0, 0, 0))
        clock.tick(20)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Update the positions of the Tile objects based on the current state of the sortable list
        for i, value in enumerate(sortable):
            tiles[i].pos = i

        for i in range(len(sortable) - 1):
            if sortable[i] > sortable[i + 1]:
                sortable[i], sortable[i + 1] = sortable[i + 1], sortable[i]
                tiles[i].value, tiles[i + 1].value = tiles[i + 1].value, tiles[i].value

        for tile in tiles:
            tile.draw()

    pygame.display.update()


