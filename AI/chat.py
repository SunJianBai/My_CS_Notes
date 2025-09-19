import requests

# 配置远程服务地址
OLLAMA_ENDPOINT = "https://https://3f54-1-94-231-41.ngrok-free.app/api/generate"

def ask_ollama(prompt, model="deepseek-r1:1.5b"):
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    
    try:
        response = requests.post(OLLAMA_ENDPOINT, json=payload)
        response.raise_for_status()
        return response.json()["response"]
    except Exception as e:
        return f"请求失败: {str(e)}"

# 使用示例
answer = ask_ollama("解释量子力学的基本概念")
print(answer)