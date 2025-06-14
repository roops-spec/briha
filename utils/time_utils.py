from datetime import datetime

def get_current_time():
    now = datetime.now()
    try:
        return "The time is " + now.strftime("%I:%M %P")
    except ValueError:
        return f"The time is {now.hour}:{now.minute:02d}"

