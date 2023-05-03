import time

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        print(f"Remaining time: {seconds} seconds")
        time.sleep(1)
        seconds -= 1
    print("Time's up! Focus session complete.")
