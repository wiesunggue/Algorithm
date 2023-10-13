import requests
import json


url = "https://kauth.kakao.com/oauth/token"
data = {
    "grant_type" : "authorization_code",
    "client_id" : "a50e35a4665189a78abcf7d0f8d2e5ec",
    "redirect_url" : "https://localhost:3000",
    "code" : "response_type=code&scope=talk_message"
}
response = requests.post(url, data=data)
tokens = response.json()
print(tokens)