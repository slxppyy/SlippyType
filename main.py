import customtkinter as ctk
import time as t

def app():
    
    # __init__
   root = ctk.CTk()
   root.geometry("500x300")
   root.wm_title("slippy-type")
   root.resizable(False, False)

   phrase = "The quick brown fox jumped over the lazy dog."

   def startTimer():
      global startTime
      startTime = t.time()
      startButton.configure(state = "disabled")

   def endTimer(event):
      global endTime
      endTime = t.time()

      # enable startButton 
      startButton.configure(state = "enabled")
      
      # calculate final time
      totalTime = endTime - startTime

      # calculate WPM

      typingSpeed = 9 / (totalTime / 60)
      
      wordsPer = int(typingSpeed)

      # accuracy check

      phraseList = list(phrase)
      inputList = list(typeText.get())
      
      accuracyCount = 0
      
      for i in range(len(phraseList)):
         if i < len(inputList) and phraseList[i] == inputList[i]:
            accuracyCount += 1
         
      # finalCalculation

      global accuracy
      accuracyPercentage = (accuracyCount / len(phraseList)) * 100

      topLevel = ctk.CTkToplevel(root)
      topLevel.geometry("300x180")
      topLevel.wm_title("results")

      # resultLabel
      wpmLabel = ctk.CTkLabel(topLevel, text = "wpm", font = ("Lilita One", 14))
      wpmLabel.pack()

      wpmResult = ctk.CTkLabel(topLevel, text = wordsPer, font = ("Lilita One", 20))
      wpmResult.pack()

      accLabel = ctk.CTkLabel(topLevel, text = "acc", font = ("Lilita One", 14))
      accLabel.pack()

      accResult = ctk.CTkLabel(topLevel, text = accuracyPercentage, font = ("Lilita One", 20))
      accResult.pack()

      # closeButton
      
      closeButton = ctk.CTkButton(topLevel, text = "Close", hover = True, corner_radius=15, fg_color="#3e44ed", hover_color="#4f54f0", command = topLevel.destroy, font = ("Lilita One", 18))
      closeButton.pack()

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