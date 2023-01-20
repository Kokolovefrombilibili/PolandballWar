import pygame

# 编写游戏开头布局
def state0(screen):
    # 显示浅绿背景
    bg1 = pygame.image.load("Pic/Bg/Bg1.png")
    screen.blit(bg1, (0, 0))
    # 显示logo
    my_font = pygame.font.Font("Font/Xiaowei.otf", 64)
    Title = my_font.render("波兰球大战", True, (0, 0, 0))
    screen.blit(Title, (240, 30))
    # 显示青少年模式按钮
    teenager = pygame.image.load("Pic/Mode/Teenager.png")
    screen.blit(teenager, (245, 150))

def state1(screen):
    # 显示浅黄背景
    bg2 = pygame.image.load("Pic/Bg/Bg2.png")
    screen.blit(bg2, (0, 0))
    # 显示青少年模式logo
    my_font = pygame.font.Font("Font/Xiaowei.otf", 64)
    Title = my_font.render("青少年模式", True, (0, 0, 0))
    screen.blit(Title, (240, 30))
    # 显示返回按钮
    back = pygame.image.load("Pic/Mode/Back.png")
    screen.blit(back, (245, 150))
    # 显示设置按钮
    setup = pygame.image.load("Pic/Mode/Setup.png")
    screen.blit(setup, (245, 262))
