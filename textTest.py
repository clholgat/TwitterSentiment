from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from calculation import *
import sys, math

def printTweet(text):
	#text = text.encode('ascii')
	print(text)
	glMatrixMode(GL_MODELVIEW)
	glPushMatrix()
	
	glRasterPos2f(0, 0);
	
	glColor3f(1, 0, 0)
	for char in text:
		glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ord(char))
	
  	glPopMatrix()
  	glFlush()

def drawScene():
	glMatrixMode(GL_MODELVIEW)
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	
	tweet = "your face"
	if tweet != None:
		printTweet(tweet)
	
	glFlush()
	glutSwapBuffers()
	

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB|GLUT_DEPTH)
	glutInitWindowSize(400,400)
	glutCreateWindow("FaceTest")
	glutDisplayFunc(drawScene)
	#glutIdleFunc(idleFunc)
	
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
  	gluLookAt(0, 0, 1, 0, 0, -1, 0, 1, 0)
  	
  	glClearDepth(1)
  	glClearColor(0, 0, 0, 0)
  	
  	glutMainLoop()
  	return
  	
if __name__ == "__main__":
	main()
