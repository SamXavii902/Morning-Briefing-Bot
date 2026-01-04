import requests

def get_quote():
    url = "https://zenquotes.io/api/random"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            quote = data[0]['q']
            author = data[0]['a']
            return f"\"{quote}\" - {author}"
        else:
            return "Keep pushing forward!"
            
    except:
        return "Make today amazing!"