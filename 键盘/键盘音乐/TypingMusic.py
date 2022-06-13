import os
from typing_extensions import runtime
import pygame
from pymusicplayer import MusicPlayer
mp = MusicPlayer()
pygame.init

def Rei01_GetFilePath():
    Rei01_Path = [__file__,]
    # 初始化
    Rei01_Int = int(-1)
    # 开始循环，检测是否有\号
    for Rei01_i, Rei01_e  in enumerate(Rei01_Path):
        for Rei01_x in range(1,64):
            if Rei01_e[Rei01_Int] != '\\':
                Rei01_Path[Rei01_i] = Rei01_Path[Rei01_i][:-1]
                Rei01_Int = Rei01_Int - 1
                Rei01_GetPath = str(Rei01_Path[Rei01_i])
        return Rei01_GetPath

file_data = Rei01_GetFilePath() + 'Data\\'
file_music = Rei01_GetFilePath() + 'Music\\'

screen = pygame.display.set_mode((600,508))
pygame.display.set_caption('键盘音乐                                                                                             Version 0.01Beta')
icon = pygame.image.load(file_data + 'icon.png')
pygame.display.set_icon(icon)
bg_bc = pygame.image.load(file_data + 'bg.png')
yl_bc = 0.050
mp.add_song(file_music + '1.mp3', 1)
mp.play()


running = True
while running:
    screen.blit(bg_bc,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()