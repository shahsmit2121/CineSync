import requests
import os
import ctypes
import time
import random
from datetime import datetime, timedelta
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

TMDB_API_KEY = "your_api_key"
WALLPAPER_FOLDER = "wallpapers"
ROTATE_INTERVAL = 5

GENRES = {
    "action": 28, "adventure": 12, "animation": 16, "comedy": 35,
    "crime": 80, "documentary": 99, "drama": 18, "family": 10751,
    "fantasy": 14, "history": 36, "horror": 27, "music": 10402,
    "mystery": 9648, "romance": 10749, "science fiction": 878,
    "tv movie": 10770, "thriller": 53, "war": 10752, "western": 37
}

def fetch_movies(start_date, end_date, genre_id=None, region=None):
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&primary_release_date.gte={start_date}&primary_release_date.lte={end_date}&sort_by=popularity.desc"
    if genre_id:
        url += f"&with_genres={genre_id}"
    if region:
        url += f"&region={region}"
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        return response.json().get('results', [])
    except requests.exceptions.RequestException:
        print("Cannot connect to TMDB. Check VPN or internet.")
        return []

def download_backdrop(movie):
    backdrop_path = movie.get("backdrop_path")
    if not backdrop_path:
        return None

    img_url = f"https://image.tmdb.org/t/p/original{backdrop_path}"
    try:
        response = requests.get(img_url, timeout=15)
        response.raise_for_status()
        image = Image.open(BytesIO(response.content)).convert("RGB")

        draw = ImageDraw.Draw(image)
        title = movie['title']

        box_width = int(image.width * 0.3)
        box_height = int(image.height * 0.1)
        padding = 30

        x = image.width - box_width - padding
        y = padding

        draw.rectangle(
            [x, y, x + box_width, y + box_height],
            fill=(0, 0, 0, 200)
        )

        max_font_size = int(box_height * 0.9)
        try:
            font = ImageFont.truetype("DejaVuSans-Bold.ttf", max_font_size)
        except:
            font = ImageFont.load_default()

        bbox = draw.textbbox((0, 0), title, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        while text_width > (box_width - 20) and max_font_size > 10:
            max_font_size -= 2
            try:
                font = ImageFont.truetype("DejaVuSans-Bold.ttf", max_font_size)
            except:
                font = ImageFont.load_default()
                break
            bbox = draw.textbbox((0, 0), title, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]

        text_x = x + (box_width - text_width) // 2
        text_y = y + (box_height - text_height) // 2

        draw.text((text_x, text_y), title, font=font, fill="white")

        os.makedirs(WALLPAPER_FOLDER, exist_ok=True)
        filename = os.path.join(WALLPAPER_FOLDER, f"{title.replace(' ', '_')}.jpg")
        image.save(filename)

        return filename
    except requests.exceptions.RequestException:
        print(f"Failed to download image for {movie['title']}")
        return None


def set_wallpaper_windows(image_path):
    abs_path = os.path.abspath(image_path)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, abs_path, 3)

def main():
    print("Movie Wallpaper Updater")
    print("\nAvailable genres:")
    for name in GENRES:
        print(f"- {name.title()}")

    genre_input = input("\nEnter genre (or press Enter for all): ").strip().lower()
    region_input = input("Enter region code like 'US', 'IN', 'KR' (or press Enter to skip): ").strip().upper()

    genre_id = GENRES.get(genre_input) if genre_input in GENRES else None
    if genre_input and genre_id is None:
        print("Invalid genre entered. Using all genres.")

    today = datetime.now().strftime("%Y-%m-%d")
    movies = fetch_movies(today, today, genre_id, region_input)

    if not movies:
        print("No releases today. Checking past 7 days...")
        past = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
        movies = fetch_movies(past, today, genre_id, region_input)

    if not movies:
        print("No recent movies found. Exiting.")
        return

    backdrops = []
    for movie in movies:
        path = download_backdrop(movie)
        if path:
            backdrops.append((movie['title'], path))

    if not backdrops:
        print("No wallpapers downloaded. Exiting.")
        return

    print(f"Downloaded {len(backdrops)} wallpapers. Rotating every {ROTATE_INTERVAL//60} minutes...")

    try:
        while True:
            for title, path in backdrops:
                print(f"Now showing: {title}")
                set_wallpaper_windows(path)
                time.sleep(ROTATE_INTERVAL)
    except KeyboardInterrupt:
        print("Wallpaper rotation stopped.")

if __name__ == "__main__":
    main()
