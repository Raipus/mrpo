"""Игровой движок для игр."""

def run_game(generate_question, task):
    """Функция игрового движка, запускающая проверку вопросов."""
    print('\nWelcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f'Hello, {name}!\n{task}')
    flag = 0
    while flag != 3:
        correct_answer = generate_question()
        answer = int(input('Your answer: '))
        if correct_answer == answer:
            print('Correct!')
            flag += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            flag = 0
    print(f"Congratulations, {name}!")
