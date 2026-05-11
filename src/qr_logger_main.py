
import cv2
import numpy
import openpyxl 
import datetime
from openpyxl import Workbook
from pyzbar.pyzbar import decode


from picamera2 import MappedArray, Picamera2, Preview
from libcamera import controls
from libcamera import Transform
import time

wb = Workbook()
ws = wb.active

processed_qr_codes = set()

st = datetime.datetime.now()
st_bicimli= st.strftime("%H:%M:%S // %Y-%m-%d")

colour = (255, 0, 0)
font = cv2.FONT_HERSHEY_COMPLEX
scale = 1
thickness =4 

def draw_barcodes(request):
    global processed_qr_codes  # İşlenmiş QR kodlarını takip etmek için global değişkeni kullanın
    with MappedArray(request, "main") as m:
        for b in barcodes:
            if b.polygon:
                # QR kodunun içeriğini alın
                qr_content = b.data.decode('utf-8')
                
                
                # İşlenmiş QR kodlarını kontrol edin
                if qr_content not in processed_qr_codes:
                    # QR kodunun köşe noktalarını alın
                    points = b.polygon
                    points = numpy.array([[point.x, point.y] for point in points], dtype=numpy.int32)
                    
                    # QR kodun etrafına bir çerçeve çizin
                    cv2.polylines(m.array, [points], isClosed=True, color=(0, 0, 0), thickness=8)

                    x = min([p.x for p in b.polygon])
                    y = min([p.y for p in b.polygon]) - 30
                    
                    # QR kodunun içeriğini görüntünün üzerine yazdırın
                    cv2.putText(m.array, qr_content, (x, y), font, scale, colour, thickness)

                    print("QR Kodu İçeriği:", qr_content, "||", st_bicimli)
                    ws.append([qr_content, st_bicimli])  # Veri ve tarih/saat ekleyin
                    wb.save("QRcodes1.xlsx")
                    processed_qr_codes.add(qr_content)

                elif qr_content in processed_qr_codes:
                    processed_qr_codes = set()
                    # QR kodunun köşe noktalarını alın
                    points = b.polygon
                    points = numpy.array([[point.x, point.y] for point in points], dtype=numpy.int32)
                    
                    # QR kodun etrafına bir çerçeve çizin
                    cv2.polylines(m.array, [points], isClosed=True, color=(0, 0, 0), thickness=8)

                    x = min([p.x for p in b.polygon])
                    y = min([p.y for p in b.polygon]) - 30
                    
                    # QR kodunun içeriğini görüntünün üzerine yazdırın
                    cv2.putText(m.array, qr_content, (x, y), font, scale, colour, thickness)
                    ws.append([qr_content, st_bicimli])  # Veri ve tarih/saat ekleyin
                    wb.save("QRcodes1.xlsx")
                    processed_qr_codes.add(qr_content)
                    

       

picam2 = Picamera2()
picam2.start_preview(Preview.QTGL)
config = picam2.create_preview_configuration(main={"size": (1024, 1024)}, transform=Transform(hflip=False, vflip=False))
picam2.configure(config)


barcodes = []
picam2.post_callback = draw_barcodes
picam2.start()

picam2.set_controls({"AfMode": controls.AfModeEnum.Manual, "LensPosition": 8.0})

while True:
    rgb = picam2.capture_array("main")
    barcodes = decode(rgb)

    if (cv2.waitKey(10) & 0xFF == 27):
        
        break

