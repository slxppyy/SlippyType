import customtkinter as ctk
import time as t
from random import choice 

def app():
    
    # __init__ 
    root = ctk.CTk()
    root.geometry("500x300+700+200")
    root.wm_title("SlippyType")
    root.resizable(False, False)
    
    phrase = "Blue garden music smile large dream silent fire"

    def startTimer(event=None):
        global startTime
        startTime = t.time()
        startButton.configure(state="disabled")

    def endTimer(event=None):
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

        # Debugging print statements
        print(f"Original phrase: {phrase}")
        print(f"Input text: {inputText}")

        # Calculate accuracy
        phraseWords = phrase.split()
        inputWords = inputText.split()
        correctWords = sum(1 for pw, iw in zip(phraseWords, inputWords) if pw == iw)
        accuracyInt = 100 * correctWords / len(phraseWords)
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
        startButton.configure(state="enabled")

    # clearButton
    clearButton = ctk.CTkButton(root, text="Restart", font=("Lilita One", 20), corner_radius=15, command=clearText, fg_color="#b80b0b", hover_color="#e82323", hover=True)
    clearButton.place(x=250, y=230, anchor='center')

    # showText
    textDisplay = ctk.CTkLabel(root, text=phrase, font=("Lilita One", 20), corner_radius=15)
    textDisplay.place(x=250, y=75, anchor='center')

    # typeText
    typeText = ctk.CTkEntry(root, placeholder_text="                                           Shift To Start", corner_radius=15, font=("Lilita One", 18), width=400)
    typeText.place(x=250, y=150, anchor='center')

    # startButton
    startButton = ctk.CTkButton(root, text="Start", font=("Lilita One", 18), hover=True, corner_radius=15, command=startTimer, fg_color="#194ee0", hover_color="#2c62f5")
    startButton.place(x=250, y=190, anchor='center')

    # Enter keyBind
    root.bind('<Return>', endTimer)
    root.bind('<Shift_R>', startTimer)
    root.bind('<Shift_L>', startTimer)

    root.mainloop()

app()
