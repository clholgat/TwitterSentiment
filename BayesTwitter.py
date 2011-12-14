from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

from face import Face
from calculation import *
from BayesSentiment import *

class BayesFace(Face):

	def __init__(self):
		self.stream = tweetFilter('SentimentTest', 'passwd')
		self.tweet = None
		self.bayes = BayesSentiment()
		self.classifier = self.bayes.getRawClassifier()		
	
	def idleFunc(self):
		try:
			newTweet = self.stream.next()
			self.tweet = self.bayes.rawClassify(newTweet)
			if self.tweet != None:
				glutPostRedisplay()
		except Exception as e:
			print(e)
			return
			
	def drawScene(self):
		glMatrixMode(GL_MODELVIEW)
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		
		glPushMatrix()
		
		#glScalef(.2, .2, .2)
		#glRotatef(90, 0, 0, 1)
		glRasterPos2f(-0.5,1)
		glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(':'))
		glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord('-'))
		if self.tweet[0] == "positive":
			glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(')'))
		else:
			glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord('('))
		glPopMatrix()
		
		if self.tweet != None:
			self.printText(self.tweet[1])
		
		glFlush()
		glutSwapBuffers()
	
if __name__ == "__main__":
	BayesFace().main()
