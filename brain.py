from utils.time_utils import get_current_time
from utils.search_utils import search_google

def process_command(command):
    command = command.lower()

    if "time" in command:
        return get_current_time()
    elif "search" in command:
        query = command.replace("search", "").strip()
        return search_google(query)
    else:
        return "T'm still learning. Try something else."
