import webbrowser

def search_google(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    return f"Searching Google for {query}"
