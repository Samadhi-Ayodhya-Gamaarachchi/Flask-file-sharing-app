# 📁 File Sharing App

A clean, modern file sharing web application built with **Flask** and vanilla JavaScript. Supports drag & drop uploads, file downloads, instant deletion, and copy-link functionality — all with a polished UI.

---

## 🚀 Features

- **Drag & drop** file uploads with animated progress bar
- **Download** any uploaded file instantly
- **Delete** files with a smooth fade animation
- **Copy link** to clipboard for easy sharing
- **File type icons** — color-coded by file type (PDF, image, doc, zip, spreadsheet)
- **Storage bar** showing how many files are stored
- **Toast notifications** for every action
- **Responsive design** — works on mobile and desktop

---

## 🗂 Project Structure

```
project/
├── app.py                  # Flask backend
├── uploads/                # Uploaded files are stored here (auto-created)
├── templates/
│   └── index.html          # Jinja2 HTML template
└── static/
    └── style.css           # All styles
```

---

## ⚙️ Requirements

- Python 3.7+
- Flask
- Werkzeug

Install dependencies:

```bash
pip install flask werkzeug
```

---

## ▶️ Running the App

```bash
python app.py
```

Then open your browser and go to:

```
http://localhost:5000
```

---

## 🌐 API Routes

| Method | Route | Description |
|--------|-------|-------------|
| GET | `/` | Home page — lists all uploaded files |
| POST | `/upload` | Upload a new file |
| GET | `/download/<filename>` | Download a specific file |
| POST | `/delete/<filename>` | Delete a specific file |

---

## 🎨 UI Dependencies

The app uses **Tabler Icons** for the icon set. Load it via CDN in `index.html`:

```html
<link rel="stylesheet" href="https://unpkg.com/@tabler/icons-webfont@latest/dist/tabler-icons.min.css">
```

> ⚠️ **If icons appear as blank boxes**, the CDN may be blocked in your environment.
> Fix: download the font locally and serve it from `static/tabler-icons/`.

---

## 🛠 Configuration

You can change the upload folder by editing this line in `app.py`:

```python
UPLOAD_FOLDER = "uploads"
```

To change the port:

```python
app.run(host="0.0.0.0", port=5000, debug=True)
```

> Set `debug=False` before deploying to production.

---

## 🔒 Security Notes

- Filenames are sanitized using `werkzeug.utils.secure_filename` to prevent path traversal attacks.
- No authentication is implemented — add Flask-Login if you need user accounts.
- For production, use a proper web server like **Gunicorn** behind **Nginx**.

---

## 📦 Production Deployment (optional)

Install Gunicorn:

```bash
pip install gunicorn
```

Run:

```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

---

## 📄 License

MIT — free to use and modify.
