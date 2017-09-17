import random


emojis = ['😋','😀', '😂', '☺️', '😇']

def get_random_emoji():
    return emojis[random.randint(0, len(emojis)-1)]
