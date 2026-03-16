# QR Code Generator

A web-based QR code generator with customizable styles, colors, and error correction levels.

![Python](https://img.shields.io/badge/Python-3.10+-blue) ![Flask](https://img.shields.io/badge/Flask-3.1-green) ![License](https://img.shields.io/badge/License-MIT-yellow)

## Features

- **4 module styles** — Square, Rounded, Circle, Gapped Square
- **Custom colors** — pick any foreground and background color
- **Error correction** — Low (7%), Medium (15%), Quartile (25%), High (30%)
- **Adjustable size** — control pixels per module (4–40)
- **Download** — save as PNG or SVG
- **Instant preview** — see the QR code as soon as it's generated

## Setup

```bash
# Clone the repo
git clone https://github.com/nwtsmnt/qr-generator.git
cd qr-generator

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run
python app.py
```

The app runs at `http://localhost:5002`.

## Tech Stack

- **Backend**: Flask, qrcode, Pillow
- **Frontend**: Vanilla JS

## Project Structure

```
qr-generator/
├── app.py              # Flask backend (QR generation)
├── requirements.txt    # Python dependencies
└── static/
    └── index.html      # Single-page frontend
```
