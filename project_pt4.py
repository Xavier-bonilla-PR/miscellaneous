import random
import time
import secrets
import os
from dotenv import load_dotenv
from openai import OpenAI

class FortuneCookieChatbot:
    def __init__(self):
        # Load the .env file
        load_dotenv()
        
        # Initialize the OpenAI API client
        self.client = OpenAI(api_key=os.getenv('AI_KEY'))
        
        self.model = "gpt-3.5-turbo"
        self.temperature = 0.9
        self.max_tokens = 100
        
        self.wisdom = [
            'Learn to let go and once you do, remember to not let go completely.',
            'Forgive others but above all, forgive yourself. Do this and the burden of your past will lessen.',
            'If you know what you want, don\'t wait. It might be too late otherwise.',
            'Open yourself to the flow of the universe. It will conspire to get you where you need to be.', 
            'Actively cultivate good karma, you never know when you might need it.',
            'You\'ll never realize different colors exist if all you know is black and white.',
            'Knowledge changes but wisdom does not.',
            'Never forget death and find strength in it to feel more alive.', 
            'Reality is but an illusion of your mind. But this doesn\'t mean that it isn\'t important.', 
            'The essence of life is change. If there is no change, it begins to rot.', 
            'Don\'t let society tell you what is important. Reconnect with yourself to find out what you value most.', 
            'Good things happen when you open yourself to life.'
        ]

    def check_num_bounds(self, num):
        if not num.isdigit() or not (1 <= int(num) <= 12):
            raise ValueError("Number not between 1 and 12")
    
    def delayed_print(self, text, delay=3):
        """Prints `text` after a `delay` in seconds."""
        time.sleep(delay)
        print(text)

    def get_fortune(self):
        num = input("Choose a random number from 1-12: ")
        self.check_num_bounds(num)
        return secrets.randbelow(12)

    def display_initial_messages(self, messages, fortune_num):
        for message in messages:
            self.delayed_print(message, delay=1)
            self.delayed_print(".", delay=1)
        self.delayed_print(self.wisdom[fortune_num], delay=1)

    def chat(self, system_message):
        messages = [{"role": "system", "content": system_message}]
        while True:
            user_input = input("User: ")
            if user_input.lower() in ["exit", "quit"]:
                print("Chatbot: Goodbye!")
                break
            messages.append({"role": "user", "content": user_input})
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
            )
            chat_message = completion.choices[0].message.content
            print(f"\n{chat_message}")
            messages.append({"role": "assistant", "content": chat_message})

def main():
    chatbot = FortuneCookieChatbot()
    fortune_num = chatbot.get_fortune()
    
    initial_messages = [
            "Everything happens for a reason, this message happened for a reason.",
            "You might not see it now but it will make sense soon enough.",
            "The stars have colluded and your message is this:"
        ]
    
    chatbot.display_initial_messages(initial_messages, fortune_num)
    
    print("Have you ever thought about this? (type 'quit' to stop)")
    
    system_message = f"You will be acting as a psychologist to help a user explore and understand their thoughts and feelings in relation to {chatbot.wisdom[fortune_num]}. Carefully read and analyze the conversation, then:" \
                     "Rephrase the key points made by the user in the fewest possible words, focusing on the core meaning they are trying to express." \
                     "Ask a concise follow-up question like why? to help the user further explore and understand their thoughts and feelings about what they've expressed." \
                     "If the user feels lost, ask why they feel lost. If the user finds forgiving hard, ask why forgiving is hard." \
                     f"Remember to keep the conversation centered around {chatbot.wisdom[fortune_num]}"
    
    chatbot.chat(system_message)

if __name__ == "__main__":
    main()
