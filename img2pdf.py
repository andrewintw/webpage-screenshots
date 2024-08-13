import os
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A3, A4, landscape  # 頁面大小，或可選擇其他尺寸

def convert_images_to_pdf(image_folder, output_pdf):
    # 獲取所有的 PNG 文件
    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    images.sort()  # 根據文件名排序，確保按順序合併

    # 創建 PDF 文件
    c = canvas.Canvas(output_pdf, pagesize=A4)
    pdf_width, pdf_height = A4

    # 使用橫向的 A3 尺寸
    # c = canvas.Canvas(output_pdf, pagesize=landscape(A3))
    # pdf_width, pdf_height = landscape(A3)


    for i, img in enumerate(images, start=1):
        img_path = os.path.join(image_folder, img)
        image = Image.open(img_path)

        # 圖像原始尺寸
        img_width, img_height = image.size

        # 計算圖像比例和縮放
        aspect_ratio = img_width / img_height
        if img_width > pdf_width or img_height > pdf_height:
            if aspect_ratio > 1:  # 圖像是橫向的
                new_width = pdf_width
                new_height = round(pdf_width / aspect_ratio)
            else:  # 圖像是縱向的
                new_height = pdf_height
                new_width = round(pdf_height * aspect_ratio)
        else:
            new_width = img_width
            new_height = img_height

        # 確保新尺寸是整數
        new_width = int(new_width)
        new_height = int(new_height)

        # 確保圖像居中
        x = (pdf_width - new_width) / 2
        y = (pdf_height - new_height) / 2

        # 添加圖像到 PDF
        c.drawImage(img_path, x, y, width=new_width, height=new_height)
        c.showPage()  # 開始新頁面

        # 打印當前處理的頁碼
        print(f'正在處理第 {i} 頁')

    # 保存 PDF 文件
    c.save()

image_folder = 'screenshots'  # 圖片所在的目錄
output_pdf = 'output.pdf'  # 輸出的 PDF 文件名

convert_images_to_pdf(image_folder, output_pdf)
print(f"已經將 PNG 圖片合併成 PDF 文件: {output_pdf}")
