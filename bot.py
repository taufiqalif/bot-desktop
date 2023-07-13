import requests


def send_message(message):
    url = 'https://api.openai.com/v1/chat/completions'
    headers = {
        'Authorization': 'Bearer YOUR_API_KEY',
        'Content-Type': 'application/json'
    }
    data = {
        'model': 'gpt-3.5-turbo',
        'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': message}]
    }
    response = requests.post(url, headers=headers, json=data)
    response_json = response.json()
    choices = response_json['choices']
    if choices:
        bot_response = choices[0]['message']['content']
        return bot_response
    return "Oops! Something went wrong."
