import urllib.parse

def generate_map_embed_url(destination):
    base_url = "https://www.google.com/maps/embed/v1/place"
    api_key = "AIzaSyB5PYJodiGGB7pczPXCVOzOwciCHZbM0Ik"
    query = urllib.parse.quote(destination)
    return f"{base_url}?q={query}&key={api_key}"














