from io import StringIO
from html.parser import HTMLParser
import urllib.request
from pathlib import Path
import pdfkit

webUrl=urllib.request.urlopen('https://www.theatlantic.com/magazine/archive/2014/04/playing-with-plato/358633/')
html=webUrl.read()
html=html.decode('UTF-8')
html = '<meta http-equiv="Content-type" content="text/html; charset=utf-8" />' + str(html)
#print(html)


class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.text = StringIO()
    def handle_data(self, d):
        self.text.write(d)
    def get_data(self):
        return self.text.getvalue()

def strip_tags(html):
    #removes all the html and php tags, I think
    s = MLStripper()
    s.feed(html)
    return s.get_data()


def delete(start, end, string):
    #print(start, end, string)
    print("delete")
    return string.replace(string[start:end+1], "")

def tag_remover(string, tag):
    for x in string:
        #string=delete(string.find('\\'),string.find('\\')+2,string)
        tagposition = string.find("<"+tag)
        tagend = string.find("</"+tag+">")
        if tagposition != -1:
            string=delete(tagposition, tagend+len(tag)+2, string)#added 2 because of the / and >, 
            #since find returns the start position of the string
    return string

def delink(text):
    text="".join(text.split("</a>"))
    for x in range(len(text)):
        try:
            if text[x].lower() == "a" and text[x-1]=="<" and x>0:
                text=delete(x-1,text[x:].find(">")+1,text)
        except IndexError:
            return text
    return text
    # link_end=text.find("</a>")
    # for x in range(len(text[0:link_end])):
    #     if text[link_end-x] == "<a":
    #         link_beginning=link_end-x
    #     for x in range(len(text[link_beginning:link_end])):
    #         if text[x] == ">":
    #             link_end_tag=x
    #             return text.split()


def title_extractor(text):
    title_end=text.find("</title>")
    for x in range(len(text[0:title_end])):
        if text[title_end-x] == ">":
            title_beginning=title_end-x+1
            return text[title_beginning:title_end]

def stripper(text):
    text=str(text)
    # text=delete(0,1,text)
    # text=delete(-3,-1,text)
    title=title_extractor(text)
    #format whitespace
    text=text.replace("\\n\\n", "\n")
    text=text.replace("\\n", "\n")
    text=text.replace("\\t", "")
    text=text.replace("\\b", "\b")
    #remove common useless tags
    text=tag_remover(text, "title")    
    text=tag_remover(text, "script")
    text=tag_remover(text, "footer")
    text=tag_remover(text, "style")
    text=tag_remover(text, "form")
    text=tag_remover(text, "nav")
    text=tag_remover(text, "figure")
    text=tag_remover(text, "svg")
    text=tag_remover(text, "caption")
    text=tag_remover(text, "head")
    print("tag tag_remover")
    # text=tag_remover(text, "h5")
    # text=tag_remover(text, "h6")
    text=tag_remover(text, "button")
    text=tag_remover(text, "ul")
    #text = delink(text)
    #remove the html with the earlier function
    #text = strip_tags(text)
    print(title)
    return text.strip()

cfr=stripper(html)
print(cfr)
pdfkit.from_string(cfr,"Confirmation Bias.pdf")