import sys, pygame
pygame.init()

size = width, height = 1100, 700
speed = [2, 2]

# background
black = 0, 150, 0
studend ="assets/stud1/"
screen = pygame.display.set_mode(size)

bg = pygame.image.load("assets/classtop.jpg")
student1 = pygame.image.load(studend + "student_1photo1.png")

# transforming
bg = pygame.transform.scale(bg, (500, 550))
student1 = pygame.transform.scale(student1, (100, 100))

bgrect = bg.get_rect()
studrect = student1.get_rect()

x = 50
y = 50
studloc = (x,y)


vel = 10

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x>0:
            x -= vel
        if keys[pygame.K_RIGHT]:
            x += vel
        if keys[pygame.K_UP]:
            y -= vel
        if keys[pygame.K_DOWN]:
            y += vel



    screen.fill(black)

    screen.blit(bg, bgrect)
    screen.blit(student1,(x,y))
    pygame.display.flip()
