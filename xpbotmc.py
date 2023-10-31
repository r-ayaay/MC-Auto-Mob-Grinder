from tkinter import Frame, Label, Entry, Tk, Toplevel, Button
from threading import Thread
from pyautogui import click
from time import sleep


window = Tk()

window_width = 450
window_height = 175

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

window.title("Aya-ay's Mob Grinder Bot")
window.resizable(False,False)
inputFrame = Frame(window, )




inputFrame.columnconfigure(0, weight=1)
inputFrame.columnconfigure(1, weight=1)

attacks_Label = Label(inputFrame,  text="Attack(s):")
attacks_Label.grid(row=0,column=0)
attacks = Entry(inputFrame)
attacks.grid(row=0,column=1)

SPA_Label = Label(inputFrame,  text="Attack Interval (per sec):")
SPA_Label.grid(row=1,column=0)
secondsPerAtk = Entry(inputFrame)
secondsPerAtk.grid(row=1,column=1)

inputFrame.pack(pady=20,padx=20)

running = True
def bot_window():
   
    popup = Toplevel()
    popup.grab_set()

    popup.geometry("450x175-25-150")
    popup.title("Bot Running")
    popup.resizable(False,False)
    popup.overrideredirect(True)
    popup.attributes('-topmost',True)
    return popup

def run_xp_bot():

    global running
    running = True

    popup = bot_window()
    window.withdraw()
    elapsed_label = Label(popup)
    elapsed_label.pack()

    click_label = Label(popup)
    click_label.pack()

    totalClicks_label = Label(popup)
    totalClicks_label.pack()

    button = Button(popup, text="Stop Bot", command=stop_bot)
    button.pack()
    
    clicks = 0
    second = 0
    minute = 0

    while(running):
        elapsed_label.config(text="Elapsed Time: " + str(minute) + ":" + str(second))
        click_label.config(text="Clicking in " + str((int(secondsPerAtk.get()) - (second % int(secondsPerAtk.get())))))
        totalClicks_label.config(text="Total Clicks: " + str(clicks))
        
        sleep(1)
        second+=1

        if(second > 60):
            minute+=1
            second%=60
        
        if(second == 0):
            continue

        if(second % int(secondsPerAtk.get()) == 0):
            for x in range(int(attacks.get())):

                elapsed_label.config(text="Elapsed Time: " + str(minute) + ":" + str(second))
                click_label.config(text="Clicking in " + str((int(secondsPerAtk.get()) - (second % int(secondsPerAtk.get())))))

                click()
                clicks+=1

                sleep(1)
                second+=1

                if(second > 60):
                    minute+=1
                    second%=60

                if(not running):
                    break

        

    button.pack_forget()  
    popup.destroy()  

    window.deiconify()
    
def check_input():
    if attacks.get():
        if secondsPerAtk.get():
            t1=Thread(target=run_xp_bot)
            t1.start()            

def stop_bot():
    print("\nSTOPPING BOT\n")
    global running 
    running = False

    
button = Button(window, text="Run Bot", command=check_input)
button.pack(pady=20)

window.mainloop()