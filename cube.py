import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
    )

colors_default = (
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (0, 1, 0),
    (1, 1, 1),
    (0, 1, 1)
)

colors_new = (
    (1, 0, 0),
    (0, 0, 1),
    (1, 0, 0),
    (0, 0, 1),
    (1, 0, 0),
    (1, 0, 0)
)

surfaces = (
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6)
)
def Cube(col):
    glBegin(GL_QUADS)
    for surface in surfaces:
        x=0
        for vertex in surface:
            x+=1
            glColor3fv(col[x])
            glVertex3fv(verticies[vertex])
    glEnd()
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -5)

    run = True
    cube_color = colors_default
    rotation = False
    speed = 20
    rotate_ax = "oz"
    while run:
        event = pygame.event.poll()

        if event.type == pygame.QUIT:
            run = False

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Cube(cube_color)
        pygame.display.flip()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if cube_color == colors_default:
                    cube_color = colors_new
                else:
                    cube_color = colors_default
                glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
                Cube(cube_color)
                pygame.display.flip()
                pygame.time.wait(10)
            elif event.button == 3:
                if rotation:
                    rotation = False
                else:
                    rotation = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and speed >= 10 and rotation:
                speed -= 10
            elif event.key == pygame.K_DOWN and rotation:
                speed += 10
            elif event.key == pygame.K_SPACE and rotation:
                if rotate_ax == "z": rotate_ax = "y"
                elif rotate_ax == "y": rotate_ax = "x"
                else: rotate_ax = "z"

        if rotation:
            if rotate_ax == "z": glRotatef(1, 0, 1, 0)
            elif rotate_ax == "y": glRotatef(1, 1, 0, 0)
            else: glRotatef(1, 0, 0, 1)
            pygame.time.wait(speed)

main()
