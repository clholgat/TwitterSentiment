from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys, math

class Face(object):

	def drawEyebrow(self, rot):
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
		if rot >= 0:
			glRotatef(rot/10, 0, 0, -1)
			glTranslatef(0, rot/100, 0)
		else:
			glTranslatef(rot/100, 0, 0)
	
		glTranslatef(-2.5, -2, 0)
		glBegin(GL_LINE_LOOP)
		glColor3f(1, 0, 0)
		for point in brow:
			glVertex3fv(point)
			
		glEnd()
	
		glPopMatrix()
		glFlush()
		
	def drawEye(self, scale):
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
		glTranslatef(0, 1.86, 0)
		glScalef(1, 1+scale/100, 1)
		glTranslatef(0, -1.86, 0)
		
		
		glBegin(GL_LINE_LOOP)
		glColor3f(1, 0, 0)
		for point in eye:
			glVertex3fv(point)
		
		glEnd()
		
		glPopMatrix()
		glFlush
	
	def drawNose(self):
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
		
	def drawMouth(self, shx, shy):
		upper = [
			[0, -1.94, 0],
			[0.25, -1.9, 0],
			[0.5, -1.85, 0],
			[0.75, -1.88, 0],
			[1, -1.87, 0],
			[1.25, -1.85, 0],
			[1.5, -1.8, 0],
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
			[1.5, -1.8, 0],
			[1.25, -1.85, 0],
			[1, -1.9, 0],
			[0.75, -1.9, 0],
			[0.5, -1.85, 0],
			[0.25, -1.9, 0],
			[0, -1.94, 0],
		]
		
		shear = [
			[1, shx, 0, 0],
			[shy, 1, 0, 0],
			[0, 0, 1, 0],
			[0, 0, 0, 1]
		]
		
		glMatrixMode(GL_MODELVIEW)
		glPushMatrix()
		glScalef(1+math.fabs(shx)/2, 1+math.fabs(shy)/2, 0)
		glTranslatef(0, -2.25, 0)
		glMultMatrixd(shear)
		glTranslatef(0, 2.25, 0)
		
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
		
	def printText(self, text):
		#text = text.encode('ascii')
		print(text)
		glMatrixMode(GL_MODELVIEW)
		glPushMatrix()
		
		glRasterPos2f(-4.5, -3)
		#glScalef(0.1, 0.1, 1)
		
		glColor3f(1, 0, 0)
		i = 0
		j = 45
		for char in text:
			glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ord(char))
			if i >= j:
				glRasterPos2f(-4.5, -3-(i/80.0))
				j += 45
			i += 1
		
  		glPopMatrix()
  		glFlush()
	
	def drawScene(self):
		pass
	
	def idleFunc(self):
		pass
		
	
	def main(self):
		glutInit(sys.argv)
		glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB|GLUT_DEPTH)
		glutInitWindowSize(400,400)
		glutCreateWindow("FaceTest")
		glutDisplayFunc(self.drawScene)
		glutIdleFunc(self.idleFunc)
		
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
  		gluLookAt(0, 0, 5, 0, 0, -1, 0, 1, 0)
  		
  		glClearDepth(1)
  		glClearColor(0, 0, 0, 0)
  		
  		glutMainLoop()
  		return
  	
if __name__ == "__main__":
	thisFace = Face()
	thisFace.main()
