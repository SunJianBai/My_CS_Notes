from openai import OpenAI

# 配置客户端指向你的远程服务
client = OpenAI(
    base_url="https://3f54-1-94-231-41.ngrok-free.app/v1",
    api_key="ollama"  # 不需要真实API密钥
)

# 创建聊天完成
response = client.chat.completions.create(
    model="deepseek-r1:1.5b",
    messages=[
        {"role": "system", "content": "你是一个有帮助的AI助手"},
        {"role": "user", "content": "讲一下华为云主机"}
    ],
    temperature=0.7
)

print(response.choices[0].message.content)