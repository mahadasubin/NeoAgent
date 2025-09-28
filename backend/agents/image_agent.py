import requests

def fetch_images(query):
    # Example: Unsplash API
    url = f"https://api.unsplash.com/search/photos?query={query}&client_id=YOUR_UNSPLASH_ACCESS_KEY"
    resp = requests.get(url)
    data = resp.json()
    return [img['urls']['regular'] for img in data['results'][:3]]
