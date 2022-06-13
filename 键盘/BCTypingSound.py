import os
import playsound
import pygame
from tkinter import *

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

def mkdir(path):

	folder = os.path.exists(path)

	if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹
		os.makedirs(path)            #makedirs 创建文件时如果路径不存在会创建这个路径
		print("---  new folder...  ---")
		print('---  OK  ---')

	else:
		print("---  There is this folder!  ---")
file = Rei01_GetFilePath() + "Data"
mkdir(file)

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('NB')
icon = pygame.image.load(file + '\\bird.png')
pygame.display.set_icon(icon)

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			playsound.playsound('C:\\AppData\\Roaming\\test\\1.wav')

root = Tk()
root.mainloop() 