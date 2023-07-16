# Mnist 數字辨識 
## 前言  
在"深度學習的16堂課"這本書中，認識到了關於深度學習的新手入門"Mnist數字辨識"，但光訓練餵圖辨識總感覺少了一點實用性，
於是萌生了讓視訊鏡頭看到數字就可以辨識的想法，雖然在生活上已經看到許多關於這方面的應用，但還是很好奇其中的運行的過程。
此模型我在 Tensorflow 架構下使用 CNN 模型，安裝 Tensorflow 的過程我記錄在這篇 https://hackmd.io/@ptgtt8_NTSGz9WRLhz2alA/ryRPkaAKh
## 實作
我參考了 kaggle 上 YASSINE GHOUZAM 的 CNN 模型[YASSINE GHOUZAM](https://www.kaggle.com/code/yassineghouzam/introduction-to-cnn-keras-0-997-top-6)
這個模型使用許多工具來讓訓練效果提升，例如:優化器、資料擴充；這篇文章裡面也有解釋為何要這麼做。我調動了一些參數，包含dropout、 ReduceLROnPlateau 的 factor，讓val_accuracy最好可達到0.9948。 

在影像物件偵測上，我先將 Webcam 捕捉到的畫面，進行灰階處理，然後將圖片二值化，接下來運用形態學的閉運算，處理圖片的毛邊，這邊我們的前置處理就完成了，接下來就是去找到我們所需要的物件輪廓，
我使用了 OpenCV 裡面的 cv2.findcontour ，此套件能夠得到圖形輪廓，再使用 cv2.boundingRect 得到了左上角座標點和長方形的長與寬，再將這段範圍的圖片擷取下來送進模型預測，得到我們所想要的數字 
![image](https://github.com/UJayMa/CNN_Mnist_Number/blob/main/detect_result_01.jpg)
