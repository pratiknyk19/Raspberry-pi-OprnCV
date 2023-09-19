# Raspberry-pi-OprnCV

# Raspberry Pi Telegram Bot for Image Processing with OpenCV

This Python script allows you to create a Telegram bot on your Raspberry Pi that receives images, processes them using OpenCV, and sends back the processed images to the user. The image processing operations include grayscale conversion, sharpening, and blurring.

## Prerequisites

Before running this script on your Raspberry Pi, ensure you have the following prerequisites:

- Raspberry Pi 3+ or 4 (or Zero W).
- Python 3 installed on your Raspberry Pi.
- The `telepot` library installed for Telegram bot integration. Install it using `pip`:
- OpenCV 4 installed for image processing. Install it using `pip`:



## Usage

1. In the file namde `Raspberry-pi-OpenCv.py` Replace `'YOUR_TELEGRAM_BOT_TOKEN'` with your actual Telegram bot token in the script.

2. Run the Python script on your Raspberry Pi. It will continuously listen for incoming messages and process images as follows:

3. When a user sends an image to the bot, it will download the image.
4. The downloaded image will be processed using OpenCV to create three versions: grayscale, sharpened, and blurred.
5. The processed images will be sent back to the user through Telegram.
6. Users can interact with the bot by sending images and receiving the processed results.

# Note
Keep the script running on your Raspberry Pi to continuously listen for incoming messages and process images.
Make sure to handle any exceptions or errors that may occur during image processing or communication with the Telegram API.
