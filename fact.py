
import tkinter
from tkinter import *
# import threading
import random
# from time import sleep

fw = open('fact.txt','r',encoding='gb18030',errors='ignore')
facts = fw.read()
facts = facts.split('\n')

def change():
    i = random.randrange(2, len(facts) - 1)
    text.delete(1.0,'end')
    text.insert(END, facts[i])
i = random.randrange(2,len(facts)-1)
root = tkinter.Tk()
root.wm_attributes('-topmost',1)
root.title(facts[1])
text = Text(root,width=50,height=8)
text.insert(END,facts[i])
text.pack()
Button(root, text="change", command=change).pack()
root.mainloop()



'''
for i in range(10):
    url = 'http://www.snapple.com/real-facts/list-view/'+str(i+1)       
    sc = requests.get(url)
    soup = BeautifulSoup(sc.text,'lxml')
    fact = soup.findAll('p',{'class':'fact_detail'})
    for i in range(len(fact)):
        fw.write(fact[i].text+'\n')
'''