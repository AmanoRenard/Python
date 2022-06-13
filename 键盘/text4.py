import pygame, sys
import keyboard
import playsound

def Rei01_GetFilePath():
    Rei01_Path = [__file__,]
    # 初始化
    Rei01_Int = int(-1)
    Rei01_GetPath = 1
    # 开始循环，检测是否有\号
    for Rei01_i, Rei01_e  in enumerate(Rei01_Path):
        for Rei01_x in range(1,64):
            if Rei01_e[Rei01_Int] != '\\':
                Rei01_Path[Rei01_i] = Rei01_Path[Rei01_i][:-1]
                Rei01_Int = Rei01_Int - 1
                Rei01_GetPath = str(Rei01_Path[Rei01_i])
        return Rei01_GetPath

file = Rei01_GetFilePath()
print(file)

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('NB')
icon = pygame.image.load(file + 'bird.png')
pygame.display.set_icon(icon)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if keyboard.is_pressed:
        print('1')