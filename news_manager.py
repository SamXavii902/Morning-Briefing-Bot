import requests

def get_tech_news():
    """
    Fetches top 5 tech news articles and returns them as a list of dictionaries.
    """
    API_KEY = "b52791b6e373454e942ca66dc0e1c0d2"
    url = f"https://newsapi.org/v2/top-headlines?category=technology&language=en&apiKey={API_KEY}"
    
    news_list = []
    try:
        response = requests.get(url).json()
        articles = response.get('articles', [])[:5] # Limit to top 5
        
        for article in articles:
            news_list.append({
                "title": article['title'],
                "url": article['url']
            })
        return news_list
    except Exception as e:
        print(f"❌ News Error: {e}")
        return []