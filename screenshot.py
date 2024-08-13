import pyautogui
import time
import os

# 設置保存圖片的目錄
output_dir = 'screenshots'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 電腦書常用尺寸
(startX, startY) = (747, 0)
(encX, endY) = (1812, 1439)

# 圖畫書
# (startX, startY) = (88, 0)
# (encX, endY) = (2470, 1439)

# 小說
# (startX, startY) = (772, 0)
# (encX, endY) = (1786, 1439)

# 108%
# (startX, startY) = (796, 123)
# (encX, endY) = (1763, 1429)

# 設置截圖範圍 (x, y, width, height)
region = (startX, startY, encX - startX, endY - startY)

# 設置檔名前綴
prefix = 'ebook.python-'

# 從第 1 頁開始截圖
start_page = 1
end_page = 200

time.sleep(8) # 讓你有時間將滑鼠移到視窗點一下

# 獲取當前滑鼠位置
original_position = pyautogui.position()

# 截圖和按向右鍵的操作
for i in range(start_page, end_page + 1):
    # 截取指定範圍的螢幕
    screenshot = pyautogui.screenshot(region=region)
    # 設置檔名
    filename = os.path.join(output_dir, f'{prefix}{i:03}.png')
    # 儲存截圖
    screenshot.save(filename)

    # 列印當前頁面數字
    print(f'正在截取第 {i} 頁，檔名為: {filename}')

    # 按向右鍵 (視網站的翻頁方向而定)
    pyautogui.press('right')
    # pyautogui.press('left')

    # 將滑鼠右移 5 像素再左移 5 像素，避免閱讀器被判定為閒置
    pyautogui.moveTo(original_position[0] + 5, original_position[1])
    pyautogui.moveTo(original_position[0], original_position[1])

    # 等待幾秒以確保頁面加載完成
    time.sleep(2)

print('完成所有截圖。')
