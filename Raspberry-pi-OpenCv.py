import telepot
import cv2
import numpy as np
import requests
from io import BytesIO

# Telegram bot token
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

# Initialize the Telegram bot
bot = telepot.Bot(TOKEN)

# Function to handle incoming messages
def handle_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    
    # Check if the message contains a photo
    if content_type == 'photo':
        # Get the file ID of the photo
        file_id = msg['photo'][-1]['file_id']
        
        print("Image received. Processing...")
        
        # Get file information using the getFile method
        file_info = bot.getFile(file_id)
        
        # Download the photo
        file_url = file_info['file_path']
        response = requests.get(f'https://api.telegram.org/file/bot{TOKEN}/{file_url}')
        image_bytes = BytesIO(response.content)
        image = cv2.imdecode(np.frombuffer(image_bytes.read(), np.uint8), -1)
        
        print("Processing complete. Sending images...")
        
        # Perform image processing tasks
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        sharpened_image = cv2.filter2D(image, -1, np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]]))
        blurred_image = cv2.GaussianBlur(image, (15, 15), 0)
        
        # Encode the processed images as bytes
        _, gray_image_bytes = cv2.imencode('.jpg', gray_image)
        _, sharpened_image_bytes = cv2.imencode('.jpg', sharpened_image)
        _, blurred_image_bytes = cv2.imencode('.jpg', blurred_image)
        
        # Send the processed images back to the user
        bot.sendPhoto(chat_id, photo=BytesIO(gray_image_bytes))
        bot.sendPhoto(chat_id, photo=BytesIO(sharpened_image_bytes))
        bot.sendPhoto(chat_id, photo=BytesIO(blurred_image_bytes))
        
        print("Images sent.")

# Start listening for incoming messages
bot.message_loop(handle_message)

# Display "Waiting for image..." before entering the message loop
print("Waiting for image...")

# Keep the program running
while True:
    pass
