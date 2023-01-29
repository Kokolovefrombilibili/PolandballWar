import pygame
import sys
import Data.State
import Data.Mode.Teenager
import json

# 初始化
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("波兰球大战")
# 开始游戏界面
state = 0
# 青少年模式计时开始
Data.Mode.Teenager.Execute_01()

while True:
    # 执行计时
    Data.Mode.Teenager.Execute_03()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Data.Mode.Teenager.Execute_02()
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x = event.pos[0]
            y = event.pos[1]
            # 点击青少年模式按钮后
            if state == 0 and 245 <= x <= 537 and 150 <= y <= 232:
                state = 1
            # 点击返回按钮后(青少年模式)
            elif state == 1 and 245 <= x <= 537 and 150 <= y <= 232:
                state = 0
            # 点击青少年模式设置按钮后
            elif state == 1 and 245 <= x <= 537 and 262 <= y <= 344:
                Data.Mode.Teenager.TeenagerSetup()

    # 进行页面切换
    if state == 0:
        Data.State.state_00(screen=screen)
    elif state == 1:
        Data.State.state_01(screen=screen)

    pygame.display.update()
