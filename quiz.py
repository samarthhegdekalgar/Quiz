import json
import random


# This function reads the data from json file and returns the file content
def read_data(file):
    with open(file) as file_obj:
        quiz_dict = json.load(file_obj)

    return quiz_dict


# This function returns random questions in list
def pick_question(question_bank):
    return random.choice(question_bank)


def count_question(dl):
    global easy, medium, hard
    if dl == 'E':
        easy += 1
    elif dl == 'M':
        medium += 1
    else:
        hard += 1


def is_cort(ans, qst):
    is_correct = False
    for value in qst['options']:  # validating answer
        if value['id'] == ans - 1:
            if value['isCorrect']:
                is_correct = True
    return is_correct


def is_valid(q):
    difficult_level = q['difficulty']
    global asked_question

    if ((difficult_level == 'E' and easy < 5) or (difficult_level == 'M' and medium < 3) or (
            difficult_level == 'H' and hard < 2)) and q['index'] not in asked_question:
        # checking whether question is choose before and question meets criteria

        count_question(difficult_level)
        asked_question.append(question['index'])  # if not choose add it to asked questions
        return True

    else:
        return False


def ask_question(que):
    global score

    print(f'{easy + medium + hard}] {que["question"]}')  # display question
    print()

    option_num = 1  # display option number

    for value in que['options']:  # display options
        print(f"{option_num}] {value['option']}")
        option_num += 1

    ans = int(input('Answer :\t'))
    print()
    ans = is_cort(ans, que)
    if ans:
        score += 3  # adding marks to correct questions
    else:
        score -= 1  # reduction of marks for incorrect answer


if __name__ == '__main__':

    easy, medium, hard, score = 0, 0, 0, 0  # default value
    asked_question = []  # list to hold question number to avoid repetition of same question

    try:

        question_dict = read_data('EduCompQuiz_data.json')  # Json file which contain question and answers

        while (easy + medium + hard) < 10:
            question = pick_question(question_dict)  # choose random question
            ack = is_valid(question)

            if ack:
                ask_question(question)

        print(f'Your score :\t{score}')  # display score

    except Exception as e:
        print(e)
