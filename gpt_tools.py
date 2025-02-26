from openai import OpenAI


with open(".api_key", "r", encoding="utf-8")as r:
    api_key = r.read().strip()

client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

with open("system_message.txt", "r") as file:
    system_message = file.read()

messages = [{"role": "system", "content": system_message}]
error_message = "稍等哈，我这会儿有点事情~~"

while True:
    user_input = input("User: ")
    messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages
    )
    try:
        response_content = response.choices[0].message.content
        print(f"Assistant: {response_content}")
        while len(messages) >= 50:
            messages.pop(1)
        messages.append(response.choices[0].message)
    except:
        # 开发时
        print(response)
        if input().strip(): break


        # print("Assistant:", error_message)
