"""Игра 'НОК'."""
import random as r
import math
from game_engine import run_game

def lcm_two(x, y):
    """Функция подсчета НОК."""
    return abs(x * y) // math.gcd(x, y)

def generate_question():
    """Функция генерации вопросов."""
    a, b, c = r.randint(1,20), r.randint(1,20), r.randint(1,20)
    print(f'Question: {a} {b} {c}')
    correct_answer = lcm_two(lcm_two(a, b), c)
    return(correct_answer)

run_game(generate_question,"Find the smallest common multiple of given numbers.")
