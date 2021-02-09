from random import randint

def generate_matrix():
    return [[randint(10, 50) for i in range(10)] for j in range(10)]
