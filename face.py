from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

import sys

def drawEyebrow(rot):
	brow = [
		[3.03125, 2.75, 0],
		[3, 2.78, 0],
		[2.75, 2.81, 0],
		[2.5, 2.81, 0],
		[2.25, 2.81, 0],
		[2, 2.78, 0],
		[1.75, 2.76, 0],
		[1.5, 2.75, 0],
		[1.25, 2.56, 0],
		[1, 2.5, 0],
		[0.875, 2.35, 0],
		[0.75, 2.2, 0],
		[0.75, 2.1, 0],
		[0.875, 2.031, 0],
		[1, 2.0675, 0],
		[1.25, 2.1, 0],
		[1.5, 2.3, 0],
		[1.75, 2.44, 0],
		[2, 2.5, 0],
		[2.25, 2.51, 0],
		[2.5, 2.53, 0],
		[2.75, 2.51, 0],
		[3, 2.5, 0]
	]
	
	glMatrixMode(GL_MODELVIEW)
	glPushMatrix()
	glTranslatef(2.5, 2, 0)
	glRotatef(rot, 0, 0, -1)
	glTranslatef(-2.5, -2, 0)
	glBegin(GL_LINE_LOOP)
	glColor3f(1, 0, 0)
	for point in brow:
		glVertex3fv(point)
		
	glEnd()
	
	glPopMatrix()
	glFlush()
		
def drawEye():
	eye = [
		[2.7, 1.94, 0],
		[2.5, 2, 0],
		[2.25, 2.06, 0],
		[2, 2.08, 0],
		[1.75, 2.06, 0],
		[1.5, 2.01, 0],
		[1.25, 1.86, 0],
		[1, 1.58, 0],
		[1.25, 1.5, 0],
		[1.5, 1.47, 0],
		[1.75, 1.47, 0],
		[2, 1.48, 0],
		[2.25, 1.55, 0], 
		[2.5, 1.7, 0]
	]
	
	glMatrixMode(GL_MODELVIEW)
	glPushMatrix()
	
	glBegin(GL_LINE_LOOP)
	glColor3f(1, 0, 0)
	for point in eye:
		glVertex3fv(point)
	
	glEnd()
	
	glPopMatrix()
	glFlush

def drawNose():
	mid = [
		[0.5, 0.09, 0],
		[0.6, 0, 0],
		[0.55, -0.09, 0],
		[0.5, -0.25, 0]
	]
	
	edge = [
		[0.94, 0, 0], 
		[1, -0.25, 0],
		[0.94, -0.5, 0]
	]
	
	glMatrixMode(GL_MODELVIEW)
	glPushMatrix()
	
	glBegin(GL_LINE)
	glColor3f(1, 0, 0)
	glVertex3fv(mid[0])
	glVertex3fv(mid[1])
	glVertex3fv(mid[1])
	glVertex3fv(mid[2])
	glVertex3fv(mid[2])
	glVertex3fv(mid[3])
	glEnd()
	
	glBegin(GL_LINE)
	glVertex3fv(edge[0])
	glVertex3fv(edge[1])
	glVertex3fv(edge[1])
	glVertex3fv(edge[2])
	glEnd()
	
	glPopMatrix()
	glFlush()
	
def drawMouth():
	upper = [
		[0, -1.94, 0],
		[0.25, -1.9, 0],
		[0.5, -1.85, 0],
		[0.75, -1.9, 0],
		[1, -1.9, 0],
		[1.25, -1.85, 0],
		[1.5, -1.94, 0],
		[1.25, -1.75, 0],
		[1, -1.56, 0],
		[0.75, -1.5, 0],
		[0.5, -1.45, 0],
		[0.25, -1.5, 0],
		[0, -1.5, 0]
	]
	
	lower = [
		[0, -2.25, 0],
		[0.25, -2.25, 0],
		[0.5, -2.21, 0],
		[0.75, -2.17, 0],
		[1, -2.1, 0],
		[1.25, -1.96, 0],
		[1.5, -1.94, 0],
		[1.25, -1.85, 0],
		[1, -1.9, 0],
		[0.75, -1.9, 0],
		[0.5, -1.85, 0],
		[0.25, -1.9, 0],
		[0, -1.94, 0],
	]
	
	glMatrixMode(GL_MODELVIEW)
	glPushMatrix()
	
	glBegin(GL_LINE_LOOP)
	glColor3f(1, 0, 0)
	for point in upper:
		glVertex3fv(point)
	
	glEnd()
	
	glBegin(GL_LINE_LOOP)
	for point in lower:
		glVertex3fv(point)
	
	glEnd()
	
	glPopMatrix()
	glFlush()

def drawScene():
	glMatrixMode(GL_MODELVIEW)
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	
	drawEyebrow(20)
	drawEye()
	drawNose()
	drawMouth()
	
	glRotatef(180, 0, 1, 0)
	
	drawEyebrow(20)
	drawEye()
	drawNose()
	drawMouth()
	
	glFlush()
	glutSwapBuffers()

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB|GLUT_DEPTH)
	glutInitWindowSize(400,400)
	glutCreateWindow("FaceTest")
	glutDisplayFunc(drawScene)
	
	glMatrixMode(GL_MODELVIEW)
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	glEnable(GL_CULL_FACE)
	glCullFace(GL_BACK)
	glShadeModel(GL_FLAT)
  	glEnable(GL_NORMALIZE)
  	glEnable(GL_COLOR_MATERIAL)
  	
  	glMatrixMode(GL_PROJECTION)
  	glLoadIdentity()
  	glOrtho(-5, 5, -5, 5, -10, 10)
  	
  	glMatrixMode(GL_MODELVIEW)
  	glLoadIdentity()
  	gluLookAt(0, 0, 10, 0, 0, -1, 0, 1, 0)
  	
  	glClearDepth(1)
  	glClearColor(0, 0, 0, 0)
  	
  	glutMainLoop()
  	return
  	
if __name__ == "__main__":
	main()
