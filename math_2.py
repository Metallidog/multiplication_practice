from kivy.app import App
from kivy.properties import NumericProperty, StringProperty, BooleanProperty, ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from random import randint

class MainScreen(BoxLayout):
    num1 = NumericProperty(0)
    num2 = NumericProperty(0)
    inputTry = StringProperty('Press Start')
    answer = StringProperty('')
    equation = StringProperty('Welcome')
    correct = BooleanProperty(True)
    evalColor = ListProperty([0, 0, 1, 1])
    score = ListProperty([0,0])
    
    
    def __init__(self, *args, **kwargs):
        super(MainScreen, self).__init__(*args, **kwargs)
        self.correct = True
        self.buttonEval()
        self.score = [0,0]
        
    def buildEquation(self):
        if self.correct: #only builds new equation if no wrong answer
            self.num1 = randint(1, 10)
            self.num2 = randint(1, 10)
            self.equation = "{} X {}".format(self.num1, self.num2)
            self.answer = str(self.num1 * self.num2)
        
    def buttonEval(self, dt=0):        
        self.buildEquation()
        self.inputTry = 'Please Input Answer'
        self.evalColor = [0, 0, 1, 1]

    def buildInputTry(self, value):
        if self.inputTry[0]=='P': self.inputTry = '' #clears button text 
        self.inputTry += value  #appends digits from buttons pushed
        if len(self.inputTry) == len(self.answer):  #autochecks answer once the length of answer is correct
            if self.inputTry == self.answer:
                self.inputTry += " is CORRECT!"
                self.evalColor = [0, 1, 0, 1]
                self.correct = True
                self.score[0]+=1
                Clock.schedule_once(self.buttonEval, 1)
            else:
                self.inputTry += " is NOT Correct. Try Again"
                self.evalColor = [1, 0, 0, 1]
                self.correct = False
                self.score[1]+=1
                Clock.schedule_once(self.buttonEval, 1)
              
    def backspace(self):
        self.inputTry = 'Please Input Answer' #just in case first digit is incorrect

class MultiplyApp(App):    
    def build(self):
        return MainScreen()

if __name__=='__main__':
    MultiplyApp().run()
