# 📸 Real-Time QR Scanner & Excel Data Logger
### Specialized for Raspberry Pi Native Camera Interface

This project provides a robust solution for high-speed QR code recognition and automated data management using the **Raspberry Pi Camera (PiCamera2)**. Unlike generic USB webcam implementations, this system leverages the native Pi hardware for optimized performance and lower latency.

## 🌟 Key Features
- **Native PiCamera2 Integration:** Uses the latest `picamera2` library with `post_callback` for efficient frame processing.
- **Automated Data Logging:** Every unique scan is automatically timestamped and saved into an **Excel (.xlsx)** file using `openpyxl`.
- **Live Overlay:** Decoded QR content is rendered directly onto the video stream with dynamic bounding boxes.
- **Duplicate Prevention:** Implements a logic to manage processed codes, ensuring clean data entry while allowing continuous tracking.

## 🛠 Tech Stack
- **Hardware:** Raspberry Pi 5 (compatible with 3/4), Raspberry Pi Camera Module.
- **Programming:** Python.
- **Libraries:** `OpenCV`, `NumPy`, `openpyxl`, `pyzbar`, `Picamera2`.

## 📁 Project Structure
- `/src`: Contains `QRScannerLastVersion.py` (Core logic).
- `/data`: Default directory for the generated `QRcodes1.xlsx` log files.

## 🚀 How It Works
The script initializes the PiCamera with a 1024x1024 resolution. The `draw_barcodes` function acts as a callback that intercepts every frame, decodes QR data via `pyzbar`, draws a high-thickness border around the detected code, and writes the results to an Excel sheet with the exact scan time.

---
*This project serves as a foundational module for the **TÜBİTAK 2209-A** Industrial Sorting System.*
