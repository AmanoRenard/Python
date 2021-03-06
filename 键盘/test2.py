import os
import playsound
import pygame
from tkinter import *
import keyboard
import time
import random

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

def mkdir(path):

	folder = os.path.exists(path)

	if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹
		os.makedirs(path)            #makedirs 创建文件时如果路径不存在会创建这个路径
		print("[错误] 检测到缺少资源文件。")
		print('请将资源文件放至Data文件夹中！')

	else:
		print("[系统] 初始化成功！")
file = Rei01_GetFilePath() + "Data"
mkdir(file)

pygame.init()
screen = pygame.display.set_mode((600,508))
pygame.display.set_caption('按键音                                                                                              Version 0.01Beta')
icon = pygame.image.load(file + '\\icon.png')
pygame.display.set_icon(icon)
bg_bc = pygame.image.load(file + '\\bg.png')

keysbc = 'aeimquy274].'
rtbc=0

keysbc2 = 'bfjnrvz48-[/'
rtbc2=0

keysbc3 = 'cgkosw36`;0'
rtbc3=0

keysbc4 = 'dhlptx=19,\\'
rtbc4=0

o = 0
o2 = 0
o3 = 0
o4 = 0
o5 = 0
o6 = 0
o7 = 0
o8 = 0
random_bcenter0 = random.randint(0,1)
random_bcenter1 = random.randint(0,3)
rd_s01 = random.randint(0,3)
rd_s11 = random.randint(0,2)
rd_end11 = 0

pygame.mixer.music.set_volume(0.5)
running = True
while running:
    screen.blit(bg_bc,(0,0))
    try:
        if keyboard.is_pressed(keysbc[rtbc]):#if key 'q' is pressed
            if o == 0:
                pygame.mixer.music.stop()
                pygame.mixer.music.load(file + '\\1.wav')
                pygame.mixer.music.play(loops = 0, start = 0.0)
                o = 1
        else:
            o = 0
            rtbc = rtbc + 1
            if rtbc >= 12:
                rtbc = 0
    except:
        break #if user pressed other than the given key the loop will break
    try:
        if keyboard.is_pressed(keysbc2[rtbc2]):#if key 'q' is pressed
            if o2 == 0:
                pygame.mixer.music.stop()
                pygame.mixer.music.load(file + '\\2.wav')
                pygame.mixer.music.play(loops = 0, start = 0.0)
                o2=1
        else:
            o2=0
            rtbc2 += 1
            if rtbc2 >= 12:
                rtbc2 = 0
    except:
        break #if user pressed other than the given key the loop will break
    try:
        if keyboard.is_pressed(keysbc3[rtbc3]):#if key 'q' is pressed
            if o3 == 0:
                pygame.mixer.music.stop()
                pygame.mixer.music.load(file + '\\3.wav')
                pygame.mixer.music.play(loops = 0, start = 0.0)
                o3=1
        else:
            o3=0
            rtbc3 += 1
            if rtbc3 >= 11:
                rtbc3 = 0
    except:
        break #if user pressed other than the given key the loop will break
    try:
        if keyboard.is_pressed(keysbc4[rtbc4]):#if key 'q' is pressed
            if o4 == 0:
                pygame.mixer.music.stop()
                pygame.mixer.music.load(file + '\\4.wav')
                pygame.mixer.music.play(loops = 0, start = 0.0)
                o4=1
        else:
            o4=0
            rtbc4 += 1
            if rtbc4 >= 11:
                rtbc4 = 0
    except:
        break #if user pressed other than the given key the loop will break
    try:
        if keyboard.is_pressed(' '):
            if o5 == 0:
                pygame.mixer.music.stop()
                if random_bcenter0 == 0:
	                random_bcenter = file + '\\space1.wav'
	                random_bcenter0 = random.randint(0,1)
                else:
                	random_bcenter = file + '\\space2.wav'
	                random_bcenter0 = random.randint(0,1)
                pygame.mixer.music.load(random_bcenter)
                pygame.mixer.music.play(loops = 0, start = 0.0)
                o5=1
        else:
            o5=0
    except:
        break
    try:
        if keyboard.is_pressed(' '):
            if o6 == 0:
                pygame.mixer.music.stop()
                if random_bcenter1 == 0:
	                random_bcenter_1 = file + '\\space1.wav'
	                random_bcenter1 = random.randint(0,3)
                elif random_bcenter1 == 1:
                	random_bcenter_1 = file + '\\space2.wav'
	                random_bcenter1 = random.randint(0,3)
                elif random_bcenter1 == 2:
                	random_bcenter_1 = file + '\\space3.wav'
	                random_bcenter1 = random.randint(0,3)
                else:
                	random_bcenter_1 = file + '\\space4.wav'
	                random_bcenter1 = random.randint(0,3)
                pygame.mixer.music.load(random_bcenter_1)
                pygame.mixer.music.play(loops = 0, start = 0.0)
                o6=1
        else:
            o6=0
    except:
        break
    try:
        if keyboard.is_pressed('\n'):
            if o7 == 0:
                pygame.mixer.music.stop()
                if rd_s01 == 0:
	                rd_s0 = file + '\\enter1.wav'
	                rd_s01 = random.randint(0,3)
                elif rd_s01 == 1:
                	rd_s0 = file + '\\enter2.wav'
	                rd_s01 = random.randint(0,3)
                elif rd_s01 == 2:
                	rd_s0 = file + '\\enter3.wav'
	                rd_s01 = random.randint(0,3)
                else:
                	rd_s0 = file + '\\enter4.wav'
	                rd_s01 = random.randint(0,3)
                pygame.mixer.music.load(rd_s0)
                pygame.mixer.music.play(loops = 0, start = 0.0)
                o7=1
        else:
            o7=0
    except:
        break
    try:
        if keyboard.is_pressed('\b'):
            if o8 == 0:
                pygame.mixer.music.stop()
                if rd_s11 == 0:
	                rd_s1 = file + '\\backspace1.wav'
	                rd_s11 = random.randint(0,2)
                elif rd_s11 == 1:
	                rd_s1 = file + '\\backspace2.wav'
	                rd_s11 = random.randint(0,2)
                else:
	                rd_s1 = file + '\\backspace3.wav'
	                rd_s11 = random.randint(0,2)
                pygame.mixer.music.load(rd_s1)
                pygame.mixer.music.play(loops = 0, start = 0.0)
                o8 = 1
                rd_end11 = -1
            elif rd_end11 <= -100:
	            rd_s11 = random.randint(0,2)
	            if rd_s11 == 0:
	                rd_s1 = file + '\\backspace1.wav'
	            elif rd_s11 == 1:
	                rd_s1 = file + '\\backspace2.wav'
	            else:
	                rd_s1 = file + '\\backspace3.wav'
	            pygame.mixer.music.stop()
	            pygame.mixer.music.load(rd_s1)
	            pygame.mixer.music.play(loops = 0, start = 0.0)
	            rd_end11 = -60
            else:
                rd_end11 = rd_end11 - 1
        else:
            o8 = 0
    except:
        break
    if o8 == 0 and rd_end11 <=-59:
        rd_end11 = rd_end11 - 1
        if rd_end11 <= -100:
            rd_s1 = file + '\\backspace_end.wav'
            pygame.mixer.music.load(rd_s1)
            pygame.mixer.music.play(loops = 0, start = 0.0)
            rd_end11 = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
