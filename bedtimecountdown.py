import time 

def countdown(minutes):

    seconds = minutes*60

    print("⏰ Timer activate ")
    print("Please relax and try to fall asleep")
    print("*" * 40)

    try:
        while seconds   >   0:
            mins,secs = divmod(seconds,60)
            while secs <   15:
                print("HEYYY TIME IS ALMOST UP NERD")
                print("*"   *   30)
        timer_format = f"{mins:02d}:{secs:02d}"
            
            # Print over the same line using carriage return (\r)
        print(f"Time left to relax: {timer_format}", end="\r")

