import os
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def convert_images_to_pdf(image_folder, output_pdf):
    # 獲取所有的 PNG 文件
    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    images.sort()  # 根據文件名排序，確保按順序合併

    # 創建 PDF 文件
    c = canvas.Canvas(output_pdf, pagesize=A4)
    width, height = A4

    for img in images:
        img_path = os.path.join(image_folder, img)
        image = Image.open(img_path)

        # 調整圖像大小以適應 PDF 頁面
        aspect_ratio = image.width / image.height
        if aspect_ratio > 1:  # 圖像是橫向的
            new_width = width
            new_height = round(width / aspect_ratio)
        else:  # 圖像是縱向的
            new_width = round(height * aspect_ratio)
            new_height = height

        # 確保新尺寸是整數
        new_width = int(new_width)
        new_height = int(new_height)

        image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)

        # 添加圖像到 PDF
        c.drawImage(img_path, 0, 0, width=new_width, height=new_height)
        c.showPage()  # 開始新頁面

    # 保存 PDF 文件
    c.save()

image_folder = 'screenshots'  # 圖片所在的目錄
output_pdf = 'output.pdf'  # 輸出的 PDF 文件名

convert_images_to_pdf(image_folder, output_pdf)
print(f"已經將 PNG 圖片合併成 PDF 文件: {output_pdf}")
