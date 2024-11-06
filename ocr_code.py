import cv2
import pytesseract
from pytesseract import Output
import imutils
import pandas as pd

def add_branding(frame, text="OCR", position=(50, 50), font_scale=1, font_thickness=2, text_color=(255, 255, 255), bg_color=(0, 0, 0)):
    overlay = frame.copy()
    alpha = 0.6  

    (text_width, text_height), _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, font_scale, font_thickness)
    x, y = position

    cv2.rectangle(overlay, (x, y + 10),(x + text_width, y - text_height - 10), bg_color, -1)
    cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)
    cv2.putText(frame, text, position, cv2.FONT_HERSHEY_SIMPLEX, font_scale, text_color, font_thickness)

    return frame

cap = cv2.VideoCapture(0)

ocr_output = []

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    frame = imutils.resize(frame, width=600)

    frame = add_branding(frame)
    cv2.imshow('Real-Time OCR -Renault', frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('c'):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

       
        data = pytesseract.image_to_data(gray, output_type=Output.DICT)

        n_boxes = len(data['level'])
        for i in range(n_boxes):
            (x, y, w, h) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
            confidence = int(data['conf'][i])  

            if confidence > 0:
                text = data['text'][i].strip()
                if text:
                   
                    ocr_output.append([text, x, y, x + w, y + h, confidence])

        for item in ocr_output:
            print(item)

    if key == ord('q'):
        break

if ocr_output:
    df = pd.DataFrame(ocr_output, columns=['Text', 'Left', 'Top', 'Right', 'Bottom', 'Confidence'])
    
    try:
        df.to_excel('ocr_output.xlsx', index=False)
        print("Output saved to 'ocr_output.xlsx'")
    except Exception as e:
        print(f"Error saving to Excel: {e}")
else:
    print("No OCR data to save.")

cap.release()
cv2.destroyAllWindows()
