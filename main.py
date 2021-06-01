from tkinter import *
import random as r
from collections import Iterable
size = 4
plays = 0
final_tracks = []
def flatten(lis):
    for item in lis:
        if isinstance(item, Iterable) and not isinstance(item, str):
            for x in flatten(item): yield x
        else: yield item
def button(frame):
    b=Button(frame,text="   ", width=2)
    return b
def change_a():
    global a
    for i in ['O','X']:
        if not(i==a):
            a=i
            label = Label(text="  "+ a + " turn  ")
            label.place(x=2*size*25+2,y=7*20)
            break
def reset():
    global a
    for k in range(size):
        for i in range(size):
            for j in range(size):
                b[i][j][k]["text"]=" "
                b[i][j][k]["state"]=NORMAL
    a=r.choice(['O','X'])
def check():
    global plays
    for track in final_tracks:
        complete_row = True
        foundtrack = []
        for i in range(size):
            if b[track[i][0]][track[i][1]][track[i][2]]["text"] != a:
                complete_row = False
        if complete_row:
            label = Label(text="  "+a + " wins  ")
            label.place(x=2*size*25+2,y=7*20)
            plays = 0
            if input(""): reset()
            break
    if plays == size*size*size:
        label = Label(text="  draw  ")
        label.place(x=2 * size * 25 + 2, y=7 * 20)
        if input(""): reset()
def click(row,col, ais):
        global plays
        plays += 1
        b[row][col][ais].config(text=a,state=DISABLED)
        check()
        change_a()
root=Tk()
root.geometry("500x200")
root.title("TIC TAC TOC TUC")
a=r.choice(['O','X'])
options = []
for k in [-1, 0, 1]:
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i != 0 or j != 0 or k != 0: options.append([i, j, k])
referencepoints = []
for k in range(size):
    for i in range(size):
        for j in range(size):
            if (k==0 or k==size-1) or (i==0 or i==size-1) or (j==0 or k==size-1):
                if [k, i, j] not in referencepoints: referencepoints.append([k, i, j])
for ref in referencepoints:
    for opt in options:
        ref_original = ref
        track = []
        for i in range(size):
            track.append(ref_original)
            ref_original = [ref_original[i] + opt[i] for i in range(len(ref_original))]
        test_track = list(flatten(track))
        passes = True
        for i in test_track:
            if i < 0 or i > (size - 1):
                passes = False
                break
        if passes: final_tracks.append(track)
b = [[[] for j in range(size)] for i in range(size)]
for k in range(size):
    for i in range(size):
        for j in range(size):
            b[i][j].append(button(root))
            b[i][j][k].config(command= lambda row=i,col=j,ais=k: click(row,col,ais))
            b[i][j][k].place(x=40+i*20+k*size*25,y=40+j*20)
res = Button(root, text="Reset", command=reset)
res.place(x=2 * size * 25 + 80, y=7 * 20)
root.mainloop()