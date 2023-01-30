import unittest
import pygame
import sys
from Data.State import *

class TestUI(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        print("以下是测试UI界面的部分")

    def setUp(self):
        global screen
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("测试窗口")

    def test_state_00(self):
        state_00(screen=screen)

    def tearDown(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    unittest.main()
