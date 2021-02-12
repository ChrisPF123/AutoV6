import asyncio
import sys
import auraxium
from auraxium import ps2
import pyautogui
from tkinter import *



def keyboard_v6():
    pyautogui.press('v')
    pyautogui.press(userInput.get())
    
async def api_query(player_name):
    print(f"listen on player {player_name}'s killing")
    client = auraxium.EventClient(service_id='s:5825')
    char = await client.get_by_name(ps2.Character, player_name)
    char_id = char.id
    print(f"player {player_name}'s id {char_id}")
    @client.trigger(auraxium.EventType.GAIN_EXPERIENCE)
    async def auto_v6(event):
        if event.payload["experience_id"] == "1" and int(event.payload["character_id"]) == char_id:
            print(f"{player_name} just killed someone")
            keyboard_v6()


root = Tk()
userInput = StringVar(root)
root.geometry("225x200") 
root.title("SALT Auto V6")

l = Label(text = "Keyboard Key Selection") 
l.pack()

userInput.set("6")
w = OptionMenu(root, userInput, "1", "2", "3", "4", "5", "6", "7", "8", "9")
w.pack()

l = Label(text = "Enter your Planetside 2 Player Name") 
l.pack()

def myClick():
    pname = e.get()
    post = f"Tracking {pname}"
    myLabel = Label(root, text=post)
    e.delete(0, 'end')
    myLabel.pack(pady=10)
    print(f"player name is: {pname}")
    print ("value is:" + userInput.get())
    loop = asyncio.get_event_loop()
    loop.create_task(api_query(pname))
    loop.run_forever()

e = Entry(root, width=50, font=('Helvetica', 30))
e.pack(padx=10, pady=10)

myButton= Button(root, text="Submit", command=myClick)
myButton.pack(pady=10)

root.mainloop()