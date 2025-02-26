from wxauto import WeChat

wx = WeChat()

# 获取当前聊天窗口消息
msgs = wx.GetAllMessage()

while True:
    ipt = input()
    if ipt.lower() == 'q': break

    for msg in msgs:
        if msg.type == 'sys':    # 系统消息，如时间等
            continue
        elif msg.type == 'self':
            role = 'self'        # 自己的消息
        else:
            role = 'friend'      # 好友的消息
        
        user = msg.sender
        text = msg.content
        t_id = msg.id
        
        data = {'role': role, 'role_name': user, 'content': text, 't_id': t_id}