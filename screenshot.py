import pyautogui
import time
import os

output_dir = 'screenshots'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 設置截圖範圍 (x, y, width, height)
region = (747, 0, 1812 - 747, 1437 - 0)

time.sleep(10)
start_page = 1
end_page = 730

# 截圖和按向右鍵的操作
for i in range(start_page, end_page + 1):
    # 截取指定範圍的螢幕
    screenshot = pyautogui.screenshot(region=region)
    filename = os.path.join(output_dir, f'raspberry.pi.projects-{i+1:03}.png')
    screenshot.save(filename)
    print(f'正在截取第 {i+1} 頁，檔名為: {filename}')
    pyautogui.press('right')
    time.sleep(2)

print('完成所有截圖。')
