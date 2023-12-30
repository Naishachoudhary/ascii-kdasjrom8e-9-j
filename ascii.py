from tkinter import *
root = Tk()

root.title("ASCII Code")
root.geometry("400x400")
root.config(background= "blue")

entry = Entry(root)
entry.place(relx = 0.5, rely = 0.3 , anchor=CENTER)

label = Label(root , text = "Ascii Code : ", bg = 'yellow', fg = 'black')
label.place(relx = 0.5 , rely = 0.4 ,  anchor = CENTER)

label2 = Label(root, text = "Encrypted code : ",  bg = 'yellow', fg = 'black' )
label2.place(relx = 0.5 , rely = 0.5 ,  anchor = CENTER)

def ascii() :
    input_word = entry.get()
     
    for letter in input_word :
        label['text'] += str(ord(letter)) + " "
        ascii = int(ord(letter))
        encrypted = ascii - 1
        label2['text'] += str(chr(encrypted))
        
btn = Button(root , text = "ascii" , bg = 'yellow' , fg = 'black',  command = ascii)
btn.place(rely = 0.6 , relx = 0.5, anchor = CENTER)
        
    
    
root.mainloop()

