import random
import pygame


def generate_plank(border_list):
    left = random.randint(0, 550)
    top = 600
    width = 100
    height = 20
    # 生成第一块板子
    if len(border_list) == 0:
        return [left, top, width, height]
    else:
        # 根据最后一个板子的高度来决定自己的高度
        num = len(border_list) - 1
        last_border_top = border_list[num][1]
        top = last_border_top + 80
        return [left, top, width, height]



def up_plank(planks):
    for i in planks:
        i[1] = i[1] - 1
    # 如果第一个板子的高度坐标已经到了-20，也就是下边缘跑出窗口上边缘了，就把第一个板子从数组里移除，避免内存爆炸
    if planks[0][1] <= -20:
        planks.remove(planks[0])


def draw_planks(screen, planks):
    for i in planks:
        drawcolor = (255, 255, 255) # 这一行很重要。。。
        left = i[0]
        top = i[1]
        rectwidth = i[2]
        rectheight = i[3]
        pygame.draw.rect(screen, drawcolor, [left, top, rectwidth, rectheight])