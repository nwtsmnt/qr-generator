import io
import base64
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import (
    SquareModuleDrawer,
    GappedSquareModuleDrawer,
    CircleModuleDrawer,
    RoundedModuleDrawer,
)
from qrcode.image.styles.colormasks import SolidFillColorMask
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_folder="static")

MODULE_DRAWERS = {
    "square": SquareModuleDrawer,
    "gapped": GappedSquareModuleDrawer,
    "circle": CircleModuleDrawer,
    "rounded": RoundedModuleDrawer,
}


def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


@app.route("/")
def index():
    return send_from_directory("static", "index.html")


@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    link = data.get("link", "").strip()
    if not link:
        return jsonify({"error": "No link provided"}), 400

    style = data.get("style", "square")
    fg_color = hex_to_rgb(data.get("fg", "#000000"))
    bg_color = hex_to_rgb(data.get("bg", "#ffffff"))
    box_size = max(4, min(40, int(data.get("size", 10))))
    error_correction = {
        "L": qrcode.constants.ERROR_CORRECT_L,
        "M": qrcode.constants.ERROR_CORRECT_M,
        "Q": qrcode.constants.ERROR_CORRECT_Q,
        "H": qrcode.constants.ERROR_CORRECT_H,
    }.get(data.get("ec", "M"), qrcode.constants.ERROR_CORRECT_M)

    qr = qrcode.QRCode(
        version=None,
        error_correction=error_correction,
        box_size=box_size,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)

    drawer_cls = MODULE_DRAWERS.get(style, SquareModuleDrawer)
    color_mask = SolidFillColorMask(
        back_color=bg_color,
        front_color=fg_color,
    )

    img = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=drawer_cls(),
        color_mask=color_mask,
    )

    buf = io.BytesIO()
    img.save(buf, format="PNG")

    return jsonify({
        "image": base64.b64encode(buf.getvalue()).decode(),
    })


if __name__ == "__main__":
    app.run(debug=True, port=5002)
