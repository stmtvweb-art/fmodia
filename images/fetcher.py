import requests
from urllib.parse import quote


def get_cover(artist, title):
    try:
        query = quote(f"{artist} {title}")
        url = f"https://api.deezer.com/search?q={query}"

        r = requests.get(url, timeout=10)
        data = r.json()

        songs = data.get("data", [])

        if songs:
            album = songs[0].get("album", {})
            cover = album.get("cover_xl")

            if cover:
                return cover

    except:
        pass

    return f"https://placehold.co/600x600?text={quote(artist)}"
