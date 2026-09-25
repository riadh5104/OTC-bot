import time
import requests

TOKEN = "8841511294:AAGs89K85hYfB..."  # استبدله بالتوكن الكامل الخاص بك إذا لزم الأمر
CHAT_ID = "8925866445"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        response = requests.post(url, json=payload)
        return response.json()
    except Exception as e:
        print(f"Error sending message: {e}")

if __name__ == "__main__":
    send_telegram_message("🤖 تم تشغيل بوت التداول الآلي (OTC) بنجاح على السيرفر ويعمل على مدار الساعة 24/7!")
    while True:
        # هنا سيتم إضافة منطق إشارات التداول لاحقاً
        time.sleep(60)
