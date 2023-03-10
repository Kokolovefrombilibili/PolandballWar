import pygame
import sys
from Data.State import *
import Data.Mode.Teenager

# 初始化
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("波了个波")
# 开始游戏界面
state = 0
# 青少年模式计时开始
Data.Mode.Teenager.Execute_01()

while True:
    # 执行计时
    Data.Mode.Teenager.Execute_03()

    # 事件监听
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
            # 进入游戏
            elif state == 0 and 245 <= x <= 537 and 262 <= y <= 344:
                state = 2
            # 退出游戏界面
            elif state == 2 and 30 <= x <= 176 and 30 <= y <= 71:
                state = 0
            # 进入章节选择
            elif state == 2 and 206 <= x <= 352 and 30 <= y <= 71:
                state = 3
            # 退出章节选择
            elif state == 3 and 50 <= x <= 196 and 30 <= y <= 71:
                state = 2

    # 进行页面切换
    if state == 0:
        state_00(screen=screen)
    elif state == 1:
        state_01(screen=screen)
    elif state == 2:
        state_02(screen=screen)
    elif state == 3:
        state_03(screen=screen)

    pygame.display.update()
