import nltk
import random
from nltk.sentiment import SentimentIntensityAnalyzer
import re

patterns = [
    # Patrones de saludo
    (r'hello|hey|hi', ['Hello, nice to meet you', 'Hi!', 'Hi']),
    # Patrones relacionados con el sentimiento del usuario
    (r'(?i)I am feeling (.*?)', ['Why are you feeling like that?', 'How can I help you?', 'Tell me more about that.']),
    # Patrones relacionados a la presentacion
    (r'(?i)my name is|I am (.*?)', ['Nice to meet you', 'It is a pleassure', 'I am AI.']),
]

def get_sentiment(message):
    nltk.download('vader_lexicon')
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(message)
    if sentiment_scores['compound'] >= 0.5:
        return 'positivo'
    elif sentiment_scores['compound'] <= -0.5:
        return 'negativo'
    else:
        return 'neutro'

def respond_sentiment(message):
    sentiment = get_sentiment(message)
    if sentiment == 'positivo':
        return 'I am glad to hear that.'
    elif sentiment == 'negativo':
        return 'That is so sad.'
    else:
        return None

def respond_pattern(message):
    for pattern, responses in patterns:
        match = re.match(pattern, message)
        if match:
            response = random.choice(responses)
            if response == 'Why are you feeling like that?':
                response = response.replace('%1', match.group(1))
            return response
    return 'I do not get it.'

def respond(message):
    response = respond_pattern(message)
    if response == 'How can I help you?':
        response += ' What can I do?'
    elif response == 'I understand.':
        response += ' Is there anything else?'
    elif response == 'I do not get it.':
        response += ' Can you say it again?'
    return response

while True:
    user_input = input('User: ')
    sentiment_response = respond_sentiment(user_input)
    if sentiment_response:
        print('Chatbot:', sentiment_response)
    else:
        chatbot_response = respond(user_input)
        print('Chatbot:', chatbot_response)
