import customtkinter as ctk
import time as t

def app():
    
    # __init__
   root = ctk.CTk()
   root.geometry("500x300")
   root.wm_title("slippy-type")
    
   phrase = "The quick brown fox jumped over the lazy dog."

   def startTimer():
      global startTime
      startTime = t.time()
      startButton.configure(state = "disabled")

   def endTimer(event):
      global endTime
      endTime = t.time()
      print("Test 1 Complete!")
      
# showText

   textDisplay = ctk.CTkLabel(root, text = phrase, font = ("Lilita One", 20), corner_radius=15)
   textDisplay.place(x = 250, y = 75, anchor = 'center')

# typeText

   typeText = ctk.CTkEntry(root, placeholder_text="Quick!", corner_radius=15, font=("Lilita One", 18), width=400)
   typeText.place(x = 250, y = 150, anchor = 'center')

# startButton

   startButton = ctk.CTkButton(root, text = "Start", font=("Lilita One", 18), hover = True, corner_radius=15, command = startTimer, fg_color="#194ee0", hover_color="#2c62f5")
   startButton.place(x = 250, y = 190, anchor = 'center')

# Enter keyBind

   root.bind('<Return>', endTimer)

   root.mainloop()


app()