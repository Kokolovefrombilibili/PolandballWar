import pygame

# 编写游戏开头布局
def state_00(screen) -> None:
    # 显示浅绿背景
    bg1 = pygame.image.load("Pic/Bg/Bg1.png")
    screen.blit(bg1, (0, 0))
    # 显示logo
    my_font = pygame.font.Font("Font/Xiaowei.otf", 64)
    Title = my_font.render("波了个波", True, (0, 0, 0))
    screen.blit(Title, (260, 30))
    # 显示青少年模式按钮
    teenager = pygame.image.load("Pic/Mode/Teenager.png")
    screen.blit(teenager, (245, 150))
    # 显示开始游戏按钮
    start_game = pygame.image.load("Pic/Mode/StartGame.png")
    screen.blit(start_game, (245, 262))

# 编写青少年模式页面
def state_01(screen) -> None:
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

# 编写游戏首页
def state_02(screen) -> None:
    # 显示黄绿背景
    bg3 = pygame.image.load("Pic/Bg/Bg3.png")
    screen.blit(bg3, (0, 0))
    # 显示返回按钮
    back = pygame.image.load("Pic/Mode/Back.png")
    back = pygame.transform.scale(back, (146, 41))
    screen.blit(back, (30, 30))
    # 显示进入关卡按钮
    opengame = pygame.image.load("Pic/Mode/OpenGame.png")
    opengame = pygame.transform.scale(opengame, (146, 41))
    screen.blit(opengame, (206, 30))

# 进入章节选择界面
def state_03(screen) -> None:
    # 显示蓝紫背景
    bg4 = pygame.image.load("Pic/Bg/Bg4.png")
    screen.blit(bg4, (0, 0))
    # 显示标题
    my_font = pygame.font.Font("Font/Xiaowei.otf", 64)
    Title = my_font.render("章节选择", True, (0, 0, 0))
    screen.blit(Title, (260, 30))
    # 显示返回按钮
    back = pygame.image.load("Pic/Mode/Back.png")
    back = pygame.transform.scale(back, (146, 41))
    screen.blit(back, (50, 30))
