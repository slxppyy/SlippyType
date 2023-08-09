import time as clock
def test():
   
   typing_phrase = "Taavishi is a monkey"
   print("Type: {}".format(typing_phrase))
   input("Press enter to start.") # enter input
   start_time = clock.time()
   phrase = input("--> ")
   end_time = clock.time()
   if typing_phrase.lower() == phrase or typing_phrase == phrase:
      final_time = (end_time - start_time) / 60
      print(start_time)
      print(end_time)
      print(final_time)
      print("Your final time was: {}".format(final_time))
   else:
      print("Please make sure you type the correct phrase.")


test()