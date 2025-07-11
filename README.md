# 🎬 ReelWalls – Movie Wallpaper Rotator

This is my **first Python project using an API**, built as a way to practice working with external data and image processing while creating something useful for cinema lovers.

ReelWalls automatically fetches backdrops of newly released movies from **TMDB (The Movie Database)** and rotates them as desktop wallpapers on Windows. Each wallpaper includes a clean title card with the movie name, positioned in the top-right corner.

---

## 🎥 Demo

> *Add your video demo here once it's ready:*

```html
<video src="demo.mp4" controls></video>
```

---

## 🚀 Features

- Pulls daily movie releases using TMDB API
- Downloads HD movie backdrops automatically
- Adds a styled movie title overlay
- Rotates wallpapers every few seconds (user-configurable)
- Supports genre and region filters like ‘Action’ or ‘IN’
- Handles missing images and connection issues

---

## 🎨 Customization & Configurations

You can easily modify:

- **Wallpaper rotation interval:**\
  By default, wallpapers change every `5 seconds`. You can adjust this by editing the value in the script:

- **Genres and Regions:**\
  The script prompts you to input genre and region codes each time you run it. Example genres: Action, Drama, Sci-Fi. Example regions: US, IN, KR.

---

## 💡 Planned Features & Ideas

### Automatic Scheduling

- Set wallpapers to change at specific times of day\
  (For example: show thrillers in the evening, animations in the morning)
- Add scheduling options via a config file or GUI

### GUI Application (Future Roadmap)

Once I get comfortable with Python GUI frameworks, I plan to:

- Build a full desktop app version using Tkinter or PyQt
- Let users select:
  - Actor name filters
  - Specific movie industries (like Bollywood, Hollywood, Korean cinema, etc.)
  - Language preferences
  - Custom time intervals using sliders or input fields
- Add a preview window before setting wallpapers
- Save user preferences locally

### Visual Improvements

- Smarter title card layout:\
  Support for long movie names with auto-wrap or marquee-style scrolling
- Custom fonts and styling for title cards
- Background blur or gradient overlays behind the text box

### System Compatibility

- Add support for Linux and macOS wallpaper changes
- Multi-monitor support and resolution-specific adjustments

---

## 📚 What I Learned

- Integrating APIs into Python projects
- Working with image manipulation using Pillow
- Managing Windows system-level settings with `ctypes`
- Building configurable, reusable scripts
- Handling user input and program flow cleanly

---

## 🙌 Acknowledgements

- **Movie Data & Images:** [TMDB](https://www.themoviedb.org/)

---

## 🧑‍💻 Author

**Smit Shah**\
*Aspiring Developer – learning one project at a time.*

---

## 🔖 Notes

- TMDB isn’t directly accessible in India, so I had to use a **VPN** during development.
- This script is currently tested only on Windows. Other OS support is in the future plan.

