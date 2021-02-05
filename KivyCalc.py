import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout


class MainGrid(GridLayout):
    textin=ObjectProperty(None)
    working=[]#variable for the queue... if the user asks for 2*2, the array will be [2,'*',2]

    def writer(self,inp):
#        if len(self.working)>=4:
#            self.working=[self.working[3]]
        if len(self.working)!=0:
            if self.working[len(self.working)-1]=='':
                self.working=[]
        #Numerical Characters
        if inp in [1,2,3,4,5,6,7,8,9,0,'.']:
            if self.working==['='] or self.textin.text=='NaN':
                self.textin.text=''
                self.working=[]
            self.textin.text+=str(inp)
        #Operators
        if inp in ['+','-','/','*']:
            #if len(self.working)>=3:
            #    self.working=[self.textin.text]
            if self.working==['']:
                self.working=[]
            if self.working==['=']:#If the last operation was 'Equals',
                                   #the code should clear the queue
                self.working=[self.textin.text,inp]
            else:#If the last operation was not equals, the code should continue as normal
                self.working+=[self.textin.text]
            if len(self.working)==1:
                self.working+=[inp]
            print(self.working)
            self.textin.text=''
        #Backspace and AC
        if inp == 'bksp':
            self.textin.text=self.textin.text[:-1]
        if inp == 'ac':
            self.working=[]
            self.textin.text=''

    def equals(self,inp):
        if len(self.working)>3:
            self.working=[self.working[3]]
        if '' in self.working:
            self.working=[]
        #Equals
        try:
            if inp=='eq':
                if self.working[0]!='=':
                    self.working+=[self.textin.text]
                    print(self.working)
                    self.textin.text=''
                    #Main 'validation' starts here and ends with the else...
                    if self.working[1]=='+':#Plus
                        ans=float(self.working[0])+float(self.working[2])
                    if self.working[1]=='-':#Minus
                        ans=float(self.working[0])-float(self.working[2])
                    if self.working[1]=='*':#Times
                        ans=float(self.working[0])*float(self.working[2])
                    if self.working[1]=='/':#Divide... Had to do some extra shtuff
                                            #for it to start printing decimals, too
                        if float(self.working[0])%float(self.working[2])==0:
                            ans=float(self.working[0])//float(self.working[2])
                        else:
                            ans=float(self.working[0])/float(self.working[2])
                    if ans.is_integer():
                        self.textin.text=str(int(ans//1.0))
                        working=[self.textin.text]
                        return int(ans//1.0)
                        #print('Is int')
                    else:
                        self.textin.text=str(ans)
                        working=[self.textin.text]
                        return ans
                        #print('not int')
                    self.working=['=']
                else:
                    self.working=[]
            else:
                r=self.equals('eq')
                self.working=[r,inp]
                return r
        except UnboundLocalError:
            pass
        except IndexError:
            pass


class CalculatorApp(App):
    def build(self):
        self.width=200
        self.height=300
        return MainGrid()

if __name__=='__main__':
    CalculatorApp().run()