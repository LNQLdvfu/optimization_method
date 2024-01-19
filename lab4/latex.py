import numpy as np
from datetime import datetime

vec = np.array
matrix = np.array


def print_matrix(mat: matrix, letter: str = None, scale: float = 1,
                 row: int = None,
                 column: int = None):
    print("\\[")
    if letter is not None:
        print(letter, "=", end="")
    print("\\scalebox{" + str(scale) + "}{")
    print("\\setlength{\\arraycolsep}{2pt}")
    print("\\renewcommand{\\arraystretch}{1}")
    print("\\begin{pmatrix}")
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            if row is not None and i == row-1 and j == column-1:
                print("\\colorbox{yellow}", end="")
                print("{", end="")
                print(round(mat[i, j], 2), ["}" if j == mat.shape[1]-1 else "}  & "][0], end="")
            else:
                print(round(mat[i, j], 2), ["" if j == mat.shape[1]-1 else " & "][0], end="")
        print(["" if i == mat.shape[0]-1 else " \\\\"][0],)
    print("\\end{pmatrix}")
    print("}")
    print("\\]\n")


def print_matrix_data(mat_data):
    print("разрешающий столбец =", mat_data["column"], end="\n\n")
    print("разрешающая строка =", mat_data["row"], end="\n\n")
    print("разрешающий элемент =", mat_data["elem"], end="\n\n")


def preambule(data=None):
    print("\\documentclass[a4paper, 12pt, fleqn]{article}")
    print("\\usepackage[T2A, T1]{fontenc}")
    print("\\usepackage[utf8]{inputenc}")
    print("\\usepackage[main=russian, english]{babel}")
    print("\\usepackage{indentfirst}")
    print("\\usepackage{amsmath}")
    print("\\usepackage{amssymb}")
    print("\\usepackage{geometry}")
    print("\\usepackage{graphicx}")
    print("\\usepackage{listings}")
    print("\\usepackage{xcolor}")

    print("\\definecolor{codegreen}{rgb}{0,0.6,0}")
    print("\\definecolor{codegray}{rgb}{0.5,0.5,0.5}")
    print("\\definecolor{codepurple}{rgb}{0.58,0,0.82}")
    print("\\definecolor{backcolour}{rgb}{0.95,0.95,0.92}")

    print("\\lstdefinestyle{mystyle}{")
    print("backgroundcolor=\\color{backcolour},  ")
    print("   commentstyle=\\color{codegreen},")
    print("   keywordstyle=\\color{magenta},")
    print("   numberstyle=\\tiny\\color{codegray},")
    print("   stringstyle=\\color{codepurple},")
    print("   basicstyle=\\ttfamily\\footnotesize,")
    print("   breakatwhitespace=false,        ")
    print("   breaklines=true,                ")
    print("   captionpos=b,                  ")
    print("   keepspaces=true,                ")
    print("   numbers=left,                  ")
    print("   numbersep=5pt,                ")
    print("   showspaces=false,               ")
    print("   showstringspaces=false,")
    print("   showtabs=false,                ")
    print("   tabsize=2")
    print("}")

    print("\\lstset{style=mystyle}")

    print("\\geometry{margin=1in}")
    
    print("\\begin{document}")

    # print("\\thispagestyle{empty}")
    print("\\begin{titlepage}")
    print("\\begin{figure}[!htb]")
    print("\\centering")
    print("\\includegraphics[width=0.04\\textwidth]{fefu_logo.jpg}")
    print("\\end{figure}")
    
    print("\\begin{center}")
    print("\\fontsize{10pt}{18pt}\\selectfont")
    print("МИНИСТЕРСТВО НАУКИ И ВЫСШЕГО ОБРАЗОВАНИЯ И НАУКИ РОССИЙСКОЙ ФЕДЕРАЦИИ\n")
    print("Федеральное государственное автономное образовательное учреждение высшего образования\n")
    print("\\textbf{«Дальневосточный федеральный университет»}\n")
    print("(ДВФУ)\n")

    print("\\end{center}")

    print("\\vspace{2mm}")
    print("\\noindent\\rule{\\textwidth}{2pt}")
    print("\\vspace{2mm}")

    print("\\begin{center}")
    print("\\textbf{ИНСТИТУТ МАТЕМАТИКИ И КОМПЬЮТЕРНЫХ ТЕХНОЛОГИЙ}\n")

    print("\\vspace{12mm}")

    print("\\textbf{Департамент математического и компьютерного моделирования}\n")

    print("\\vspace{12mm}")

    print("\\textbf{ЛАБОРАТОРНАЯ РАБОТА №4}\n")

    print("\\vspace{3mm}")

    print("По основной образовательной программе подготовки бакалавров ", end="")
    print("направлению 02.03.01 Математика и компьютерне науки ", end="")
    print("профиль «Сквозные цифровые технологии»")
    print("\\vspace{9mm}")
    print("\\end{center}")

    print("\\hfill")

    print("\\begin{minipage}[t]{0.5\\textwidth}")
    print("\\raggedright")
    print("Студент группы Б9121-02.03.01сцт\n")

    print("\\vspace{2mm}")

    print("\\underline{Ле Нгоу Куок Лик}\n")

    print("\\vspace{2mm}")

    print(f"«{datetime.now().day}» январь 2024 г.\n")
    
    print("\\vspace{24pt}")

    print("Преподаватель, \\underline{кандидат физико-} \\underline{математических наук\\phantom{qqqqqqqqqqq}}\n")

    print("\\vspace{2mm}")
    
    print("\\underline{Яковлев Анатолий Александрович}\n")

    print("\\vspace{2mm}")

    print("\\underline{\\phantom{s}\\hspace{5cm}} (подпись)\n")

    print("\\vspace{2mm}")

    print("\\vspace{2mm}")

    print("«\\underline{\\phantom{dddd}\\hspace{0.5mm}}» \\underline{\\phantom{}\\hspace{3cm}}2024 г.\n")
    
    print("\\end{minipage}\n")
    
    print("\\vspace{24mm}")

    print("\\begin{center}")
    print("г. Владивосток\n")
    print("2024")
    print("\\end{center}")
    print("\\end{titlepage}")

    # print("\\newpage")
    print("\\setcounter{MaxMatrixCols}{24}")

    print("\\section*{Постановка задачи}")
    print("Пусть дана матричная игра, заданная матрицей \\(А\\) размерности 6х8. Необходимо найти верхнюю и нижнюю цену игры и равновесное решение в смешанных стратегиях.")
    print_matrix(vec(data["A"]), "A")

    print("Нижняя цена игры:\n")

    print("\\(\\underline{A}=\\max_i\\min_j a_{ij}=", data["lower_price"], "\\)\n")
    print("Верхняя цена игры:\n")
    print("\\(\\overline{A}=\\min_j\\max_i a_{ij}=", data["upper_price"], "\\)\n")
    print("Искать равновесное решение в смешанных стратегиях будем с помощью симплекс-метода. Для этого необходимо сделать матрицу \\(А\\) неотрицательной, поэтому к каждому элементу матрицы \\(А\\) добавим модуль минимального элемента  матрицы \\(А\\).\n")

    print("\\beta=\\min_{ij}a_{ij} =", data["beta"], "\n")
    
    print("Получается неотрицательная матрица \\(\\hat{A}\\)")
    
    print_matrix(data["A_hat"], "\\hat{A}")

    print("Необходимо решить следующие задачи:\n")
        
    print("\\[\\left\\{\\begin{aligned}")
    print("&ye \\rightarrow \\max\\\\")
    print("&\\hat{A}y \\le e^{T}\\\\")
    print("&y \\ge 0")
    print("\\end{aligned}")
    print("\\right.")
    print("\\]\n")

    print("\\[\\left\\{\\begin{aligned}")
    print("&ex \\rightarrow \\min\\\\")
    print("&\\hat{A}^{T}y \\ge e\\\\")
    print("&x \\ge 0")
    print("\\end{aligned}")
    print("\\right.")
    print("\\]\n")

    print("В этом случае оптимальная стратегия первого игрока будет найдена по формуле:")

    print("\\[")
    print("p^*=\\frac{x}{||x||}")
    print("\\]\n")

    print("А оптимальная стратегия второго игрока будет найдена по формуле:")
    
    print("\\[")
    print("q^*=\\frac{y}{||y||}")
    print("\\]\n")

    print("Цена игры будет равна:")
    
    print("\\[")
    print("\\phi=\\frac{1}{\\alpha} - |\\beta|")
    print("\\]\n")

    print("где  – \\(\\alpha\\) значение целевой функции, полученной в результате решения задач линейной оптимизации.\n")

    print("\\(q^*\\) - находится прямой задачей.\n")
    print("\\(p^*\\) - находится двойственной задачей.\n")

    print("\\section*{Прямая задача}")

    print("Задача приводится к каноническому виду. За начальную угловую точку берём \\(y_0=(0,e)\\)")

    m_data = data["matrices"][0]
    row = m_data["row"]
    column = m_data["column"]
    print_matrix(vec(data["matrices"][0]["mat"]), row=row, column=column)

    print("Начальная угловая точка:\n")

    print_matrix(vec(data["corner_solution"]).T)
    print_matrix_data(m_data)

    for i in range(1, len(data["matrices"])):
        m_data = data["matrices"][i]
        row = m_data["row"]
        column = m_data["column"]
        print_matrix(vec(data["matrices"][i]["mat"]), row=row, column=column)
        if i != len(data["matrices"])-1:
            print_matrix_data(m_data)
        else:
            print("В первой строке (не включая значение целевой функции) НЕТ отрицательных элементов, а значит оптимальное решение найдено\n")

    print("\nРезультат\n")
    print_matrix(data["optim"].T, "y")
    print("Значение целевой функции} \\(\\alpha\\) =", data["obj_function"], end="\n\n")
    print("Оптимальная стратегия второго игрока:", end="\n\n")

    q = data["optim"].T/np.linalg.norm(data["optim"])
    print_matrix( q, "q^* = \\frac{y}{||y||}")

    print("\\section*{Двойственная задача}")

    print("Двойственная задача приводится к каноническому виду, далее ищется начальная угловая точка, решая вспомогательную задачу.")


    print("\\section*{Решение вспомогательной задачи}")

    print_matrix(vec(data["second_simplex_table"]), scale=0.7)

    print("Базисные столбцы выделяются с помощью элементарных преобразований строк. К первой строке добавляются остальные строки, умноженные на -1. Получается:")

    m_data = data["matrices_second"][0]
    row = m_data["row"]
    column = m_data["column"]
    print_matrix(vec(data["matrices_second"][0]["mat"]), scale=0.7, row=row, column=column)
    print("Начальная угловая точка:\n")
    print_matrix(vec(data["corner_solution_second"]).T)
    print_matrix_data(m_data)

    for i in range(1, len(data["matrices_second"])):
        m_data = data["matrices_second"][i]
        row = m_data["row"]
        column = m_data["column"]
        print_matrix(vec(data["matrices_second"][i]["mat"]), scale=0.7, row=row, column=column)
        if i != len(data["matrices_second"])-1:
            print_matrix_data(data["matrices_second"][i])

    print("\nНайденная угловая точка:\n")

    print_matrix(data["optim_second"].T)

    print("В первой строке не осталось отрицательных элементов (не считая значение целевой функции) И \\(u = 0\\), значит найдено оптимальное решение для вспомогательной задачи, но начальное угловое и допустимое решение для исходной двойственной задачи.")

    print("\\section*{Решение двойственной задачи}")
    print("Для нахождения решения двойственной задачи продолжим с найденной угловой точки. Исключим из таблицы столбцы, соответствующие элементам \\(u\\) и заменим первую строку на \\((e,0)\\)\n")

    print_matrix(vec(data["third_simplex_table"]), scale=0.6)

    print("Начальная угловая точка:\n")

    print_matrix(vec(data["corner_solution_third"]).T)

    print("Выделяем базисные столбцы с помощью элементарных преобразований строк матрицы.")
    # print_matrix(vec(data["matrices_third"][0]["mat"]), scale=0.60)

    for i in range(0, len(data["matrices_third"])):
        m_data = data["matrices_third"][i]
        row = m_data["row"]
        column = m_data["column"]
        print_matrix(vec(data["matrices_third"][i]["mat"]), scale=0.6, row=row, column=column)
        if i != len(data["matrices_third"])-1:
            print_matrix_data(data["matrices_third"][i])

    print("Результат:\n")
    print_matrix(data["optim_third"].T, "x")
    print("Значение целевой функции \\(\\alpha\\)=", data["obj_function_third"], end="\n\n")

    print("Получим оптимальную стратегию первого игрока\n")
    p = data["optim_third"].T/np.linalg.norm(data["optim_third"])
    print_matrix( p, "p^* = \\frac{x}{||x||}")

    print("Цена игры:\n")

    phi = 1/data["obj_function"] - abs(data["beta"])
    
    print("\\[")
    print("\\phi=\\frac{1}{\\alpha} - |\\beta| =", phi)
    print("\\]\n")

    print("\\section*{Ответ}")

    print("Нижняя цена игры: \\(\\underline{A} =", data["lower_price"], "\n")
    print("Верхняя цена игры: \\(\\overline{A} =", data["upper_price"], "\n")
    print("Оптимальная стратегия первого игрока\n")
    print_matrix(p, "p{*}")

    print("Оптимальная стратегия второго игрока\n")
    print_matrix(q, "q{*}")

    print("Цена игры: \\(\\phi\\)=",phi ,"\n")

    print("\\section*{Листинг}")
    print("\\lstinputlisting[language=Python]{main.py}")
    print("\\end{document}")
