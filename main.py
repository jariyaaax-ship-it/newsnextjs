from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="ตอบสั้นๆ และเฉพาะหัวข้อ: https://youtu.be/s8hlfPqdRFw?si=PVeaeAQA7Un7WkFE นี้คือคลิปอะไร",
)

print(response.text)
