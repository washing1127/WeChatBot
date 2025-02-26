import time

from wxauto import WeChat
from openai import OpenAI

# 1. 加载新微信消息
# 2. 拼接 gpt 请求
# 3. 发送 gpt 请求
# 4. 解析 gpt 响应
# 5. 发送解析结果

# GPT init
with open('.api_key', 'r', encoding='utf-8')as r:
    api_key = r.read().strip()
client = OpenAI(api_key=api_key, base_url='https://api.deepseek.com')
with open('system_message.txt', 'r', encoding='utf-8') as file:
    system_message = file.read()
gpt_message = [{'role': 'system', 'content': system_message}]
gpt_error_message = '稍等哈，我这会儿有点事情~~'
print("gpt init finish")

# chat tool init
wx = WeChat()
history_dict = dict()
wx.ChatWith(who='little satiate squat')
print('chat tool init finish')

while True:
    msgs = wx.GetAllMessage()
    new_message = list()
    for msg in msgs:
        role= msg.type
        user = msg.sender
        text = msg.content
        t_id = msg.id

        if t_id not in history_dict:
            history_dict[t_id] = (user, text)
            if role == 'friend':
                new_message.append((user, text))

    if not new_message:
        print("there is no new message, sleep a moment")
        time.sleep(10)
        continue

    new_content = "".join([f"【{user}】说：{text}" for user, text in new_message])

    gpt_message.append({'role': 'user', 'content': new_content})
    
    print("send message to gpt:")
    print(gpt_message)
    
    response = client.chat.completions.create(
        model='deepseek-chat',
        messages=gpt_message
    )
    
    try:
        response_content = response.choices[0].message.content
        gpt_message.append(response.choices[0].message)
        print('response of gpt:', response_content)
    except:
        print('response error:', response)
        response_content = gpt_error_message
        exit()
        
    wx.SendMsg(msg=response_content, who='little satiate squat')
    
    print("=======================================================================================================\n"*3)