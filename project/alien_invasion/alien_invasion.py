import sys
import pygame
from settings import Settings
from game_stats import GameStats
from scoreboard import ScoreBoard
from button import Button
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建Play按钮
    play_button = Button(ai_settings,screen,"Play")

    # 创建存储游戏统计信息的实例，并创建记分牌
    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    sb = ScoreBoard(ai_settings,screen,stats)

    #创建一艘飞船、一个子弹编组和一个外星人编组
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)

    #bg_color = (100,200,230)

    # 创建一个外星人
    #alien = Alien(ai_settings,screen)

    # 开始游戏的主循环
    while True:

        # 监视键盘和鼠标事件

        """
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()

                因为重构了这段代码到相应文件，所以直接调用函数即可
        """

        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)

        if stats.game_active:
            ship.update()

            '''
            bullets.update()
            # 删除已消失的子弹
            for bullet in bullets.copy():
                if bullet.rect.bottom <= 0:
                    bullets.remove(bullet)
            #print(len(bullets))
            '''
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,sb,screen,ship,aliens,bullets)

        '''
                # 每次循环都会重绘屏幕，这次添加有背景颜色
                screen.fill(ai_settings.bg_color)
                ship.blitme()

                # 让最近绘制的屏幕可见
                #screen.fill(bg_color)
                pygame.display.flip()
                '''
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,
                    play_button)

if __name__ == '__main__':
    run_game()



