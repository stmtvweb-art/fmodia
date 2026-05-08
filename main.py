from fastapi import FastAPI
from fastapi.responses import JSONResponse
from dotenv import dotenv_values

from metadata.infoaudio_reader import get_nowplaying
from images.fetcher import get_cover

config = dotenv_values("config/settings.env")

app = FastAPI()


@app.get("/")
def home():
    return {
        "status": "online",
        "radio": config.get("RADIO_NAME")
    }


@app.get("/nowplaying.json")
def nowplaying():
    data = get_nowplaying()

    return JSONResponse({
        "radio": config.get("RADIO_NAME"),
        "pi_code": config.get("PI_CODE"),
        "artist": data["artist"],
        "title": data["title"],
        "cover": get_cover(data["artist"], data["title"])
    })
