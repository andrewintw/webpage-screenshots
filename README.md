## 流程說明

1. 建議先用 [台灣圖書館電子書搜尋](https://taiwanlibrarysearch.herokuapp.com/) 搜尋你想要看的電子書。
2. 選其中一個圖書館，註冊成為該館的會員（大多可以網路辦證）。
3. 借閱你想看的電子書。有些圖書館需要排順位，有些可以直接線上看。
4. 執行截圖程式，截圖程式會自動翻頁並截圖
5. 執行整併圖檔為 pdf 文件的程式
6. 記得還書

NOTE: 大推 [Andrew Chen](https://www.facebook.com/profile.php?id=100062564447786) 寫的搜尋系統。為什麼這個很重要呢？因為你在 A 圖書館如果需要排順位，可以馬上跳去別的 BCD 圖書館看看有沒有同一本書。

## 環境設定

* 安裝 Python3
* 以 pip 安裝模組 - `pip install pyautogui Pillow reportlab`


## 1. 進入線上閱讀的畫面

* 將閱讀排版改為，每次顯示一頁
* 記住內容頁的左上和右下座標（會根據你的顯示器解析度有所不同，盡量使用高解析度的顯示器）
* 確定翻頁是往左翻，還是往右翻

## 2. 修改程式碼 screenshots.py

以下是我的螢幕設定的截圖範圍，從左上角的 `(747, 0)` 到右下角的 `(1812, 1439)`。你要根據你的螢幕解析度調整。

```
# 電腦書尺寸
(startX, startY) = (747, 0)
(encX, endY) = (1812, 1439)
```

這是截取後的圖檔檔案名稱

```python
# 設置檔名前綴
prefix = 'ebook.python-'
```

這是擷取的數量，會反應在檔名中。例如上面的 `prefix = 'ebook.python-'`，所以截圖後會產生 `ebook.python-001.png` ~ `ebook.python-200.png`

```python
start_page = 1
end_page = 200
```

這是每次擷取後，使用哪個方向鍵翻下一頁。我這邊是向右，許多小說都是向左，就需要改為 'left'

```python
# 按向右鍵 (視網站的翻頁方向而定)
pyautogui.press('right')
```

## 3. 執行截圖工作

建議使用雙螢幕，螢幕一以全螢幕開啟書本，進入閱讀模式。另一個螢幕二執行 `screenshots.py`，執行後需在　8 秒內用滑鼠點一下書本所在的瀏覽器（使其成為現用視窗）。然後就不用動它了，程式碼會先截圖，然後觸發鍵盤的方向鍵換頁，然後等待 2 秒（讓畫面能完整載入），然後截圖，依此繼續。

以上所說的秒數，在程式碼裡面都可以調整。


## 4. 檢查截圖完整性

擷取的圖檔會統一放在名為 `screenshots` 的資料夾下。如果你發現有些圖檔出現轉圈圈的模糊樣。表示換頁後的等待時間不足。可以修改程式碼，增加秒數（以下是 2 秒）。或是事後修改程式碼，單獨下載該頁即可。

```python
# 等待幾秒以確保頁面加載完成
time.sleep(2)
```

## 5. 將 png 圖檔轉成 pdf 檔

執行 `img2pdf.py` 即可將 screenshots/ 資料夾下的 png 都合併為 output.pdf


## 6. 記得還書

聽起來很怪，但電子書也是要還書的。確認沒問題後，記得快還書，讓下一個順位的人能快點閱讀。
