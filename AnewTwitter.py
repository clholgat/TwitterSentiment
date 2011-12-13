from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

from face import Face
from calculation import *

class AnewFace(Face):

	def __init__(self):
		self.stream = tweetFilter('clholgat', 'Jumbothedog12')
		self.tweet = None
	
	def idleFunc(self):
		#try:
			newTweet = self.stream.next()
			self.tweet = getAnewSentiment(newTweet)
			if self.tweet != None:
				glutPostRedisplay()
		#except Exception as e:
			#print(e)
			return
			
	def drawScene(self):
		glMatrixMode(GL_MODELVIEW)
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		
		print(self.tweet)
		if self.tweet == None:
			eye = 0
			mouth = 0
		else:
			eye = self.tweet[0]['arousal']*10
			mouth = (self.tweet[0]['valence']-5)/10
			
		if mouth <= 0:
			eye = -eye
		
		glPushMatrix()
		
		self.drawEyebrow(eye)
		self.drawEye(eye)
		self.drawNose()
		self.drawMouth(mouth, 0)
		
		glRotatef(180, 0, 1, 0)
		
		self.drawEyebrow(eye)
		self.drawEye(eye)
		self.drawNose()
		self.drawMouth(mouth, 0)
		
		glPopMatrix()
		
		if self.tweet != None:
			self.printText(self.tweet[1])
		
		glFlush()
		glutSwapBuffers()
	
if __name__ == "__main__":
	AnewFace().main()
