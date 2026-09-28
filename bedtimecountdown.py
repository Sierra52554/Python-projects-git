import time 

x = float(input("Please enter time till you want to sleep:(in minutes):"))

def countdown(minutes):

    seconds = int(minutes*60)

    print("⏰ Timer activate ")
    print("Please relax and try to fall asleep")
    print("*" * 40)

    try:
        while seconds   >   0:
            mins,secs = divmod(seconds,60)
            if seconds ==  15:
                print("\nHEYYY TIME IS ALMOST UP NERD")
                print("*"   *   30)
            timer_format = f"{mins:02d}:{secs:02d}"
            
            # Print over the same line using carriage return (\r)
            print(f"Time left to relax: {timer_format}", end="\r")
            time.sleep(1)
            seconds -= 1
        print ("\n\n SLEEP WELL NERD . TIMER DONE")

    except KeyboardInterrupt:
        print("\n\n SLEEP WELL NERD . TIMER STOPPED EARLY")
        
countdown(x)
        

        
        