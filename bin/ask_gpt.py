import os
import sys

import openai
from config.reader import read

report_words = read('../config/reported_words.yaml')

class AskChat(object):
    def __init__(self):
        self.api_key = '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'
        self.model = 'gpt-3.5-turbo'
        self.user_input = ''
        self.gpt_answer = []
    def set_user_input(self, msg):
        self.user_input = msg

    def ask_gpt(self):
        for word in report_words.get('WARNING'):
            if word in self.user_input:
                print(f'There is word: {word}')
                continue
            else:
                print(f'Ask GPT......')
                openai.api_key = self.api_key
                self.gpt_answer = openai.ChatCompletion.create(
                    model=self.model,
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": self.user_input},
                        {"role": "assistant", "content": "Who's there?"},
                    ],
                    temperature=0,
                )

if __name__ == '__main__':
    print('-------------------- Welcome to the GPT world --------------------')

    askChat = AskChat()
    askChat.set_user_input('Hi GPT')
    askChat.ask_gpt()
    print(askChat.gpt_answer)
