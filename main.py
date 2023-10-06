from hugchat import hugchat
from hugchat.login import Login
from env import *

sign = Login(email,passwd)
cookies = sign.login()
chatbot = hugchat.ChatBot(cookies=cookies)
id = chatbot.new_conversation()
chatbot.change_conversation(id)
# Switch to meta-llama/Llama-2-70b-chat-hf
chatbot.switch_llm(1)
print("Bienvenido")
while True:
    user_input = input('> ')
    print(chatbot.chat(user_input))