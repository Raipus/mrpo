"""Игра 'Геометрическая прогрессия'."""
import random as r
from game_engine import run_game

def geometric_progression(a, r, n):
    """Функция генерации геометрической прогрессии."""
    return [a * r**i for i in range(n)]

def generate_question():
    """Функция генерации вопросов."""
    a, b, c = r.randint(1,5), r.randint(1,10), r.randint(5,10)
    rand = r.randint(0,c-1)
    progression = geometric_progression(a,b,c)
    correct_answer = progression[rand]
    progression[rand] = '..'
    print(f'Question: {progression}')
    return(correct_answer)

run_game(generate_question,"What number is missing in the progression?")
