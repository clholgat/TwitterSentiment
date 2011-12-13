from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

import sys, math

def drawScene():
	glMatrixMode(GL_MODELVIEW)
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) 
	
	shx = 0.5
	shy = 0.5
	
	shear = [
		[1, shx, 0, 0],
		[shy, 1, 0, 0],
		[0, 0, 1, 0],
		[0, 0, 0, 1]
	]
	
	print(shear)
	cube = [
		[0.5, 0.5, 0],
		[-0.5, 0.5, 0],
		[-0.5, -0.5, 0],
		[0.5, -0.5, 0]
	]
	
	glMatrixMode(GL_MODELVIEW)
	glPushMatrix()
	glTranslatef(0.5, 0.5, 0)
	glMultMatrixd(shear)
	
	
	glBegin(GL_LINE_LOOP)
	glColor3f(1, 0, 0)
	for point in cube:
		glVertex3fv(point)
	
	glEnd()
	glPopMatrix()
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
