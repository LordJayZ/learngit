import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('抓蝴蝶')
screen.fill((255, 255, 255))
# pg.display.flip()
image = pygame.image.load('music.png')
size = image.get_size()
screen.blit(image, (0, 0))
pygame.display.update()
while True:
    # 获取事件
    for event in pygame.event.get():
        # 1.点击关闭按钮对应的事件
        if event.type == pygame.QUIT:
            exit()

        # 2.鼠标按下对应的事件
        if event.type == pygame.MOUSEBUTTONDOWN:
            # 获取鼠标按下的坐标
            print(event.pos)
            print('mouse button down')

        if event.type == pygame.MOUSEBUTTONUP:
            # 获取鼠标按下后弹起的坐标
            print(event.pos)
            print('mouse button up')

        # 3.键盘相关的事件
        if event.type == pygame.KEYDOWN:
            print(chr(event.key))
            print('key down')
            if chr(event.key) == 'ē':
                print('右')

        if event.type == pygame.KEYUP:
            print(chr(event.key))
            print('key up')
