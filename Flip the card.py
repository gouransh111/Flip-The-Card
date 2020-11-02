from tkinter import*
from tkinter import messagebox
import random
import time
index_l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
random.shuffle(index_l)
root = Tk()
timeleft=120
i = 1
score = 0
#Functions=================================
def changeImage(e,index):
    #print(index)
    global timeleft,i,s
    if i%2 != 0:
        s = e
    if index == 1 or index == 11:
        e.configure(image=b6_image)
        
    elif index == 2 or index==12:
        e.configure(image=b2_image)
    elif index == 3 or index==13:
        e.configure(image=b3_image)
    elif index == 4 or index==14:
        e.configure(image=b5_image)
    elif index == 5 or index==15:
        e.configure(image=b9_image)
    elif index == 6 or index==16:
        e.configure(image=b11_image)
    elif index == 7 or index==17:
        e.configure(image=b8_image)
    elif index == 8 or index==18:
        e.configure(image=b10_image)
    elif index == 9 or index==19:
        e.configure(image=b7_image)
    else:
        e.configure(image=b4_image) 
    if timeleft==120:
        timeless()
    if i%2 == 0:
       checkImage(e,s)    
    i += 1   
def checkImage(event,event2):
    global score
    if event["image"] != event2["image"]:
        event.configure(image=b1_image)
        event2.configure(image=b1_image)
    elif event["image"] == event2["image"] and event != event2:
        score += 1
        event.configure(state=DISABLED)    
        event2.configure(state=DISABLED)
        if score>9:
            win = messagebox.showinfo("Notification","You win the game")
            root.destroy()
    else:
        event.configure(image=b1_image)    

def timeless():
     global timeleft
     if timeleft<11:
         time_l.configure(fg="red")
     if timeleft > 0:
         timeleft -= 1
         time_l.configure(text = timeleft)
         time_l.after(1000,timeless)# 1000 this is milisecond
     else:
         rr = messagebox.showinfo("Notification","Time finished you loose the game")
         root.destroy()   
#Root configuration=====================
root.title("Flip The Card - Game")
root.geometry("580x520+300+50")
root.configure(bg="green yellow")
root.wm_iconbitmap("E://Python projects - G//Flip the card//card.ico")
#Frames=============================================
f1 = Frame(root,bg="blue",border=7,relief=GROOVE)
f1.place(x=0,y=0,width=750,height=45)
#Labels=========================================
head_l = Label(f1,text="Flip The Card-Game",bg="blue",fg="gold",font = "arial 15 bold")
head_l.place(x=190,y=0)
#Photoimage handling================================
b1_image = PhotoImage(file="E://Python projects - G//Flip the card//leaf.png")
b1_image = b1_image.subsample(5,5)

b2_image = PhotoImage(file="E://Python projects - G//Flip the card//cake.png")
b2_image = b2_image.subsample(2,2)

b3_image = PhotoImage(file="E://Python projects - G//Flip the card//coin2.png")
b3_image = b3_image.subsample(2,2)

b4_image = PhotoImage(file="E://Python projects - G//Flip the card//coin1.png")
b4_image = b4_image.subsample(2,2)

b5_image = PhotoImage(file="E://Python projects - G//Flip the card//joker.png")
b5_image = b5_image.subsample(2,2)

b6_image = PhotoImage(file="E://Python projects - G//Flip the card//peoplemale.png")
b6_image = b6_image.subsample(2,2)

b7_image = PhotoImage(file="E://Python projects - G//Flip the card//peoplefemale.png")
b7_image = b7_image.subsample(2,2)

b8_image = PhotoImage(file="E://Python projects - G//Flip the card//tea.png")
b8_image = b8_image.subsample(2,2)

b9_image = PhotoImage(file="E://Python projects - G//Flip the card//leaf1.png")
b9_image = b9_image.subsample(2,2)

b10_image = PhotoImage(file="E://Python projects - G//Flip the card//burger.png")
b10_image = b10_image.subsample(2,2)

b11_image = PhotoImage(file="E://Python projects - G//Flip the card//phone.png")
b11_image = b11_image.subsample(2,2)
#Butoons==============================================
button1 = Button(root,bg="VioletRed1",image=b1_image,command=lambda:changeImage(button1,index_l[0]))
button1.place(x=2,y=45,width=110,height=100)

button2 = Button(root,bg="VioletRed1",image=b1_image,command=lambda:changeImage(button2,index_l[1]))
button2.place(x=115,y=45,width=110,height=100)

button3 = Button(root,bg="VioletRed1",image=b1_image,command=lambda:changeImage(button3,index_l[2]))
button3.place(x=230,y=45,width=110,height=100)

button4 = Button(root,bg="VioletRed1",image=b1_image,command=lambda:changeImage(button4,index_l[3]))
button4.place(x=345,y=45,width=110,height=100)

button5 = Button(root,bg="VioletRed1",image=b1_image,command=lambda:changeImage(button5,index_l[4]))
button5.place(x=460,y=45,width=110,height=100)

button6 = Button(root,bg="VioletRed1",image=b1_image,command=lambda:changeImage(button6,index_l[5]))
button6.place(x=2,y=150,width=110,height=100)

button7 = Button(root,bg="VioletRed1",image=b1_image,command=lambda:changeImage(button7,index_l[6]))
button7.place(x=115,y=150,width=110,height=100)

button8 = Button(root,bg="VioletRed1",image=b1_image,command=lambda:changeImage(button8,index_l[7]))
button8.place(x=230,y=150,width=110,height=100)

button9 = Button(root,bg="VioletRed1",image=b1_image,command=lambda:changeImage(button9,index_l[8]))
button9.place(x=345,y=150,width=110,height=100)

button10 = Button(root,bg="VioletRed1",image=b1_image,command=lambda:changeImage(button10,index_l[9]))
button10.place(x=460,y=150,width=110,height=100)

button11 = Button(root,bg="VioletRed1",image=b1_image,command=lambda:changeImage(button11,index_l[10]))
button11.place(x=2,y=255,width=110,height=100)

button12 = Button(root,bg="VioletRed1",image=b1_image,command=lambda:changeImage(button12,index_l[11]))
button12.place(x=115,y=255,width=110,height=100)

button13 = Button(root,bg="VioletRed1",image=b1_image,command=lambda:changeImage(button13,index_l[12]))
button13.place(x=230,y=255,width=110,height=100)

button14 = Button(root,bg="VioletRed1",image=b1_image,command=lambda:changeImage(button14,index_l[13]))
button14.place(x=345,y=255,width=110,height=100)

button15 = Button(root,bg="VioletRed1",image=b1_image,command=lambda:changeImage(button15,index_l[14]))
button15.place(x=460,y=255,width=110,height=100)

button16 = Button(root,bg="VioletRed1",image=b1_image,command=lambda:changeImage(button16,index_l[15]))
button16.place(x=2,y=360,width=110,height=100)

button17 = Button(root,bg="VioletRed1",image=b1_image,command=lambda:changeImage(button17,index_l[16]))
button17.place(x=115,y=360,width=110,height=100)

button18 = Button(root,bg="VioletRed1",image=b1_image,command=lambda:changeImage(button18,index_l[17]))
button18.place(x=230,y=360,width=110,height=100)

button19 = Button(root,bg="VioletRed1",image=b1_image,command=lambda:changeImage(button19,index_l[18]))
button19.place(x=345,y=360,width=110,height=100)

button20 = Button(root,bg="VioletRed1",image=b1_image,command=lambda:changeImage(button20,index_l[19]))
button20.place(x=460,y=360,width=110,height=100)

time2_l = Label(root,text="Time remaining:",bg="cyan",font = "lucida 18 bold")
time2_l.place(x=180,y=480)

time_l = Label(root,text=timeleft,bg="cyan",font = "lucida 18 bold")
time_l.place(x=370,y=480)
root.mainloop()