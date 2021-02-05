import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty


class Float(FloatLayout):
    word1=ObjectProperty(None)
    word2=ObjectProperty(None)
    merged=ObjectProperty(None)
    def clicked(self):
        def isVowel(char):
            if char in 'aeiuoAEUIO':
                return True
            else:
                return False
        worduse1=self.word1.text
        worduse2=self.word2.text
        for x in worduse1:
            if isVowel(x) and worduse1.index(x)>0:
                worduse1=worduse1[0:worduse1.index(x)+1]
                break
        for x in worduse2:
            if isVowel(x) and worduse2.index(x)>0:
                worduse2=worduse2[-(len(worduse2)-worduse2.index(x))+1:]
                break
        print(worduse1+worduse2)
        self.merged.text=worduse1+worduse2


class WordJoinAppApp(App):
    def build(self):
        return Float()

if __name__=='__main__':
    WordJoinAppApp().run()