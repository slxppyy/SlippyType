import customtkinter as ctk
import time as t
from random import choice 
def app():
    
    # __init__ 
   root = ctk.CTk()
   root.geometry("500x300+700+200")
   root.wm_title("SlippyType")
   root.resizable(False, False)

   phraseList = ["Blue garden music smile large dream silent fire", "River stone quick jump bright star field moon", "Quiet lake winter frost golden sun evening shadow", "Ocean wave gentle breeze forest path night sky", "Silver mountain sunrise calm whisper soft breeze"]
   phrase = choice(phraseList)

   def levDistance(s1, s2):
    if len(s1) < len(s2):
        return levDistance(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]


   def startTimer(event):
      global startTime
      startTime = t.time()
      startButton.configure(state = "disabled")

   def endTimer(event):
    global endTime
    endTime = t.time()

    # enable startButton 
    startButton.configure(state="normal")
    
    # calculate final time
    totalTime = endTime - startTime

    # calculate WPM
    typingSpeed = 9 / (totalTime / 60)
    wordsPer = int(typingSpeed)

    # Get the input text
    inputText = typeText.get()

    # Calculate Levenshtein Distance
    distance = levDistance(phrase, inputText)
    accuracyInt = 100 * (1 - distance / max(len(phrase), len(inputText)))
    accuracyPercentage = str(int(accuracyInt)) + "%"

    topLevel = ctk.CTkToplevel(root)
    topLevel.geometry("200x200+850+250")
    topLevel.wm_title("Results")
    topLevel.resizable(False, False)
    topLevel.attributes('-topmost', True) 

    # resultLabel
    wpmLabel = ctk.CTkLabel(topLevel, text="wpm", font=("Lilita One", 16))
    wpmLabel.pack()

    wpmResult = ctk.CTkLabel(topLevel, text=str(wordsPer), font=("Lilita One", 32))
    wpmResult.pack()

    accLabel = ctk.CTkLabel(topLevel, text="acc", font=("Lilita One", 16))
    accLabel.pack()

    accResult = ctk.CTkLabel(topLevel, text=accuracyPercentage, font=("Lilita One", 32))
    accResult.pack()

    # closeButton
    closeButton = ctk.CTkButton(topLevel, text="Close", hover=True, corner_radius=15, fg_color="#b80b0b", hover_color="#e82323", command=topLevel.destroy, font=("Lilita One", 18))
    closeButton.place(x=100, y=175, anchor='s')


   def clearText():
      typeText.delete(0, ctk.END)
      startButton.configure(state = "enabled")

# clearButton
   clearButton = ctk.CTkButton(root, text = "Clear", font = ("Lilita One", 20), corner_radius=15, command = clearText, fg_color="#b80b0b", hover_color="#e82323", hover = True)
   clearButton.place(x = 250, y = 230, anchor = 'center')

# showText

   textDisplay = ctk.CTkLabel(root, text = phrase, font = ("Lilita One", 18), corner_radius=15)
   textDisplay.place(x = 250, y = 75, anchor = 'center')

# typeText

   typeText = ctk.CTkEntry(root, placeholder_text="                                           Shift To Start", corner_radius=15, font=("Lilita One", 18), width=400)
   typeText.place(x = 250, y = 150, anchor = 'center')

# startButton

   startButton = ctk.CTkButton(root, text = "Start", font=("Lilita One", 18), hover = True, corner_radius=15, command = startTimer, fg_color="#194ee0", hover_color="#2c62f5")
   startButton.place(x = 250, y = 190, anchor = 'center')

# Enter keyBind

   root.bind('<Return>', endTimer)
   root.bind('<Shift_R>', startTimer)
   root.bind('<Shift_L>', startTimer)

   root.mainloop()


app()