import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential

IMG_BORDER = 40
IMG_W = 640  # webcam 畫面寬度
IMG_H = 480  # webcam 畫面高度
LABEL_SIZE = 0.5
DETECT_THRESHOLD = np.float32(0.8)  # 預測閥值
CONTOUR_COLOR = (0, 255, 255)  # 輪廓框的顏色 (BGR)
LABEL_COLOR = (255, 255, 0)  # 文字標籤的顏色 (BGR)

model = tf.keras.models.load_model('CNN_Digit_Recognizer.h5')
MORPH_KERNEL = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))


# 開始擷取畫面
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, IMG_W)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, IMG_H)

# while cap.isOpened():
while(True):
    
    # 取得一格畫面
    success, frame = cap.read()

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, frame_binary = cv2.threshold(frame_gray, 127, 255, cv2.THRESH_BINARY_INV)
    img_binary = cv2.morphologyEx(frame_binary, cv2.MORPH_CLOSE, MORPH_KERNEL)
    contours, _ = cv2.findContours(img_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    

# 走訪所有輪廓
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)

        # 如果輪廓太靠近邊緣，忽略它
        if x < IMG_BORDER or x + w > (IMG_W - 1) - IMG_BORDER or y < IMG_BORDER or y + h > (IMG_H - 1) - IMG_BORDER:
            continue

        # 如果輪廓太大或太小，也忽略它  
        if w < 28 // 2 or h < 28 // 2 or w > IMG_W // 2 or h > IMG_H // 2:
            continue

        img_digit = img_binary[y: y + h, x: x + w]

        img_digit = cv2.resize(img_digit, (28, 28),interpolation=cv2.INTER_AREA)  

        img_digit = img_digit.reshape(1, 28, 28, 1)

        img = img_digit.astype('float32')

        img /= 255
        
        predict_prob = model.predict(img)
        label = np.argmax(predict_prob)
        max_prob = predict_prob[0][label]
        
        # 小於預測閥值，不顯示
        if max_prob < DETECT_THRESHOLD:
            continue

        cv2.rectangle(frame, (x, y), (x + w, y + h), CONTOUR_COLOR, 1)
        cv2.putText(frame, str(label), (x + w // 5, y - h // 5), cv2.FONT_HERSHEY_COMPLEX, LABEL_SIZE, LABEL_COLOR, 1)


    cv2.imshow('ImageWindow',frame)

    # if cv2.waitKey(1) == ord('q'):
    if cv2.waitKey(1) == 113:
        break

cap.release()
cv2.destroyAllWindows()
            

