# Mnist 數字辨識 
## 前言  
在"深度學習的16堂課"這本書中，認識到了關於深度學習的新手入門"Mnist數字辨識"，但光訓練餵圖辨識總感覺少了一點實用性，
於是萌生了讓視訊鏡頭看到數字就可以辨識的想法，雖然在生活上已經看到許多關於這方面的應用，但還是好奇其中的奧妙
## 實作
我採用了kaggle上YASSINE GHOUZAM的CNN模型[YASSINE GHOUZAM](https://www.kaggle.com/code/yassineghouzam/introduction-to-cnn-keras-0-997-top-6)
這個模型使用許多工具來讓訓練效果提升，例如:優化器、資料擴充；這篇文章裡面也有解釋為何要這麼做，很適合新手閱讀。
在影像物件偵測上使用了opencv裡面的findcontour套件，此套件能夠得到圖形輪廓，也可以得到將圖形框在長方形的座標點與長寬，再將圖片送進模型預測，得到我們所想要的效果  
![image](https://github.com/UJayMa/CNN_Mnist_Number/blob/main/detect_result_01.jpg)
