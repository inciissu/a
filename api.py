import openai
import os

# OpenAI API anahtarını yükle
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("HATA: API anahtarı bulunamadı. Lütfen ortam değişkeninizi ayarlayın!")
    exit(1)

# OpenAI istemcisini kullanarak API çağrısı yap
def send_prompt_to_ai(user_input: str) -> str:
    """ Kullanıcı mesajını OpenAI'ye gönderir ve yanıt döndürür. """
    try:
        response = openai.ChatCompletion.create(  # OpenAI 1.61.0 uyumlu
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Sen yardımcı bir asistansın."},
                {"role": "user", "content": user_input}
            ],
            api_key=api_key  # API anahtarını buraya ekleyebilirsiniz (güvenli değil!)
        )
        return response["choices"][0]["message"]["content"]  # AI'nin cevabını döndür
    except Exception as e:
        return f"Hata: {str(e)}"

# Kullanıcıdan giriş alıp çalıştır
if __name__ == "__main__":
    while True:
        user_input = input("Kullanıcı: ")
        if user_input.lower() == "exit":
            print("AI Asistan: Görüşmek üzere!")
            break

        ai_response = send_prompt_to_ai(user_input)
        print(f"AI Asistan: {ai_response}")
