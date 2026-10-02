from tkinter import Tk, Button,BOTH
from time import time

def game():
    global start, end   
     
    if(b.cget("bg") == colors["go"]):
        b.config(bg = colors["end"])
        b.config(text = f"")
        start = round(time(),2)
    else:
        end = round(time(),2)
        b.config(bg = colors["go"])
        b.config(text = f"{round(end - start,2)}")
        
    
    
    


colors = {"go":"lightgreen", "end":"red"}

asd = Tk()
asd.title("::Timer Game::")
asd.geometry(f"500x458+{asd.winfo_screenwidth()//2-250}+{asd.winfo_screenheight()//2-227}")
asd.resizable(False,False)

b = Button(asd, text="", bg=colors["go"], command=game, font=("",30,"bold"))
b.pack(fill=BOTH, expand=True)
asd.bind("<KeyPress>", (lambda e:game()))
asd.mainloop()