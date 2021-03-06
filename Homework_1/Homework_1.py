'''
Задача 1
Имеется колода в 52 карты. Найти число возможностей вытянуть из неё 4 карты так,
чтобы среди них был хотя бы один туз.
'''
import numpy as np


def combinations(n: int, k: int) -> int:
    return np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k))


a = combinations(4, 1) * combinations(48, 3)
b = combinations(4, 2) * combinations(48, 2)
c = combinations(4, 3) * combinations(48, 1)
d = combinations(4, 4)
# либо
e = combinations(52, 4) - combinations(48, 4)
# Ответ Число возможнестей вытянуть из 4х карт хотя бы один туз = 76145
print(a + b + c + d)
print(e)


'''
Задача 2
Из 60 вопросов, входящих в экзаменационные билеты, студент знает 50. 
Случайным образом студент вытягивает 3 вопроса. Какова вероятность, что все 
выбранные вопросы знакомы студенту? Какова вероятность что два из 
трёх вопросов знакомы студенту?
'''

# Вероятность что первый вытянутый билет известен
P_a = 50 / 60
# Верятность что второй вытянутый билет известен
P_b = 49 / 59
# Верятность что третий вытянутый билет известен
P_с = 48 / 58

# Ответ 1 Вероятность что все выбранные вопросы знакомы студенту = 0.57
print(P_a * P_b * P_с)
# Ответ 2 Вероятность что два из трёх вопросов знакомы студенту = 0,36
print(combinations(50, 2) * combinations(10, 1) / combinations(60, 3))

'''
Допустим, имеется некоторая очень редкая болезнь (поражает 0.1% населения). 
Вы приходите к врачу, вам делают тест на эту болезнь, и тест оказывается 
положительным. Врач говорит вам, что этот тест верно выявляет 99% больных этой 
болезнью и всего лишь в 1% случаев даёт ложный положительный ответ.
Вопрос: какова вероятность, что вы действительно больны ей?
'''

# Вероятность что человек болен (0.1% населения) = 0.001
P_disease = 0.001
# Вероятность что тест верно выявил больного (99%) = 0.99
P_testDisease_disease = 0.99
# Вероятность что тест выявил болезнь у здорового (1%) = 0.01
P_testDisease_healthy = 0.01
# Верятность что человек в принципе здоров
P_healthy = 0.999
# Формула полной вероятности где в качестве Ai используется healthy и disease
# Верятность нахождения болезни
P_testDisease = P_testDisease_healthy * P_healthy + P_testDisease_disease * P_disease
# Вероятность что человек реально болеет
P_disease_testDisease = P_disease * P_testDisease_disease / P_testDisease
# 9% людей у которых обследование показало болен на самом деле больные люди
print(P_disease_testDisease)