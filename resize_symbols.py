import cv2
import os
import numpy as np
import shutil

def resize_symbols():
    input_dir = "symbols"
    output_dir = "symbols_28x28"

    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir, exist_ok=True)

    def extract_number(name):
        """Извлекает номер из symbol_XX.png"""
        return int(name.split("_")[1].split(".")[0])

    def resize_to_28x28(img):
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        _, img_bin = cv2.threshold(
            img_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
        )

        coords = cv2.findNonZero(img_bin)
        x, y, w, h = cv2.boundingRect(coords)

        symbol = img_bin[y:y+h, x:x+w]

        scale = 20 / max(w, h)
        symbol_resized = cv2.resize(symbol, None, fx=scale, fy=scale,
                                    interpolation=cv2.INTER_AREA)

        canvas = np.zeros((28, 28), dtype=np.uint8)

        sy, sx = symbol_resized.shape
        y_offset = (28 - sy) // 2
        x_offset = (28 - sx) // 2

        canvas[y_offset:y_offset+sy, x_offset:x_offset+sx] = symbol_resized

        return canvas

    files = sorted(
        [f for f in os.listdir(input_dir) if f.lower().endswith(".png")],
        key=extract_number
    )

    i = 0
    for filename in files:
        img = cv2.imread(os.path.join(input_dir, filename))

        out_img = resize_to_28x28(img)

        out_path = os.path.join(output_dir, f"symbol_{i}.png")
        cv2.imwrite(out_path, out_img)
        i += 1