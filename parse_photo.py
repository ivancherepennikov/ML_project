import cv2
import numpy as np
import os
import shutil

def parse_photo(input_photo):
    symbols_dir = "symbols"

    if os.path.exists(symbols_dir):
        shutil.rmtree(symbols_dir)

    os.makedirs(symbols_dir, exist_ok=True)
    img = cv2.imread(f'{input_photo}')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    th = cv2.adaptiveThreshold(
        blur, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV,
        41,
        7
    )

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
    morph = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel)

    contours, _ = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda c: cv2.boundingRect(c)[0])
    symbols = []

    for i, cnt in enumerate(contours):
        x, y, w, h = cv2.boundingRect(cnt)
        area = cv2.contourArea(cnt)

        # мусор пора выкидывать
        if area < 80:
            continue
        if h < 15:
            continue

        # Вырезаем символ
        symbol = img[y:y+h, x:x+w]
        symbols.append(symbol)
        cv2.imwrite(os.path.join(symbols_dir, f"symbol_{i}.png"), symbol)


