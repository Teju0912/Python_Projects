## import libreries

from tkinter import *  # windows, buttons, text boxes, labels jaise visual element bna skte hai GUI ke liye
from gtts import gTTS  #  creates an audio file (MP3)
import playsound       # mp3 sound play


root = Tk()
root.geometry('350x300')
root.resizable(0,0)                    # (0,0)   width x height
root.config(bg = 'ghost white')         # config= setting like colour, font, size, text ye sb set kr skte hai bg = background colour
root.title('GetProjects - TEXT_TO_SPEECH')

# heading
Label(root, text = ' TEXT_TO_SPEECH', font='arial 20 bold', bg = 'white smoke').pack()
Label(root, text = 'GetProjects', font = 'arial 15 bold', bg = 'white smoke').pack(side=BOTTOM)

# Lable
Label (root, text = 'Enter text', font = 'arial 15 bold', bg= 'white smoke').place(x=20,y=60)

# texy variable
Msg = StringVar()

# Entry
entry_field = Entry(root, textvariable = Msg, width = 50)
entry_field.place(x=20, y=100)


# define function 
def TEXT_TO_SPEECH():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('GetProject.mp3')
    playsound.playsound('GetProject.mp3')
    
def Exit():
    root.destroy()
    
def Reset():
    Msg.set("")

# Butoon

Button(root, text = "play", font = 'arial 15 bold', command = TEXT_TO_SPEECH, width = 4).place(x=25, y=140)
Button(root, text = "Exit", font = 'arial 15 bold', command = Exit, bg = "orangered",).place(x=100, y=140)
Button(root, text = "Reset", font = 'arial 15 bold', command = Reset).place(x=175, y=140)

#infinite loop to run program
root.mainloop()








