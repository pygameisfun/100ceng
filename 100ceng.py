import pygame
import sys
from pygame.locals import KEYDOWN, QUIT
import generate_plank as gp

game_over = False
planks = []
man_position = [0, 15]
speed = int(5)
score = 0

pygame.init()
screen_size = (600, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('是男人就下100层')
# screen.fill((0,0,0))

#游戏主程序
def game_start():
    pygame.time.delay(10)
    # 初始化屏幕背景
    screen.fill((0, 0, 0))
    # 如果板子为空就添加初始化板子(游戏杠开始)
    if len(planks) < 10:
        newborder = gp.generate_plank(planks)
        planks.append(newborder)

    gp.up_plank(planks)
    gp.draw_planks(screen, planks)

    # 人物左右移动,下面的方法可以实现连续按键
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_LEFT]:
        man_position[0] = man_position[0] - 3
    if key_pressed[pygame.K_RIGHT]:
        man_position[0] = man_position[0] + 3

    # 判断人物脚下高度是否有板子上边缘高度
    # 生成新的板子高度数组
    top_border = []
    planks_l_r = []
    for i in planks:
        top_border.append(i[1])
        border_l_r = [i[0], i[0] + 100]
        planks_l_r.append(border_l_r)
    man_bottom = man_position[1] + 20 - 1
    man_left = man_position[0]
    man_center = man_position[0] + 20
    man_right = man_position[0] + 60
    # print("当前人物的中心横坐标" + str(man_center))
    # 如果人物脚下没有板子就往下掉
    # print(top_border)
    if man_bottom not in top_border:
        # print("脚下没板")
        # print(top_border)
        #预期位置
        prepare = man_position[1] + speed
        # 如果人底部正好是板子上边缘列表
        if prepare in top_border:
            man_position[1] = prepare
            print(prepare)
            print(top_border)
        # elif int(prepare + int(speed)) -1 in top_border:
        #     man_position[1] = man_position[1] + 4
        # elif int(prepare + int(speed)) -2 in top_border:
        #     man_position[1] = man_position[1] + 3
        # elif int(prepare + int(speed)) -3 in top_border:
        #     man_position[1] = man_position[1] + 2
        # elif int(prepare + int(speed)) -4 in top_border:
        #     man_position[1] = man_position[1] + 1
        else:
            man_position[1] = man_position[1] + speed


        # print(man_position)
    else:
        # 脚下有板子
        left = 0
        right = 0
        for i in planks:
            # 找到和人物当前高度一致的板子
            if i[1] == man_bottom:
                left = i[0]
                right = i[0] + 100
        if man_center < left or man_center > right:
            man_position[1] = man_position[1] + speed
    draw_a_man()
    draw_score(score)

# add a man
def draw_a_man():
    drawcolor = (255, 255, 255)  # 这一行很重要。。。
    left = 50
    top = 550
    if len(planks) == 1:
        man_position[0] = planks[0][0] + 50 - 15
        man_position[1] = planks[0][1] - 20
    else:
        man_position[1] = man_position[1] - 1
    pygame.draw.circle(screen, drawcolor, man_position, 20)


def draw_score(score):
    text = "score: " + str(score)
    score_font = pygame.font.SysFont('arial', 32)
    score_screen = score_font.render(text, True, (255, 255, 255))
    score_over_rect = score_screen.get_rect()
    score_over_rect.midtop = (500, 10)
    screen.blit(score_screen, score_over_rect)

def tend():
    # game_over_font = pygame.font.Font('msyh.ttc', 45)
    game_over_font = pygame.font.SysFont('arial', 45)

    game_over_screen = game_over_font.render('Game Over', True, (255, 255, 255))
    restart_screen = game_over_font.render('Press Space to Restart', True, (255, 255, 255))
    game_over_rect = game_over_screen.get_rect()
    restart_rect = restart_screen.get_rect()
    game_over_rect.midtop = (600 / 2, 10)
    restart_rect.midtop = (600 / 2, 100)
    screen.blit(game_over_screen, game_over_rect)
    screen.blit(restart_screen, restart_rect)
    # pygame.display.update()




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if man_position[1] < 15:
        game_over = True

    if man_position[1] > 600:
        game_over = True

    if game_over is False:
        game_start()
        pygame.display.flip()
    else:
        screen.fill((0, 0, 0))

        tend()
        pygame.display.flip()  # 渲染
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        if pygame.key.get_pressed()[pygame.K_SPACE]:
            game_over = False
            planks = []
            man_position = [0, 15]
            score = 0
            # pygame.time.wait(500)