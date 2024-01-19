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

    print("\\textbf{ЛАБОРАТОРНАЯ РАБОТА №3}\n")

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

    print("\\underline{Канцуров Александр Вадимович}\n")

    print("\\vspace{2mm}")

    print(f"«{datetime.now().day}» январь 2024 г.\n")
    
    print("\\vspace{24pt}")

    print("Преподаватель, \\underline{кандидат физико-} \\underline{математических наук\\phantom{qqqqqqqqqqq}}\n")

    print("\\vspace{2mm}")
    
    print("\\underline{Яковлев Анатолий Александрович}\n")

    print("\\vspace{2mm}")

    print("\\underline{\\phantom{s}\\hspace{5cm}} (подпись)\n")

    print("\\vspace{2mm}")

    print("\\underline{Яковлев Анатолий Александрович}\n")

    print("\\vspace{2mm}")

    print("«\\underline{\\phantom{dddd}\\hspace{0.5mm}}» \\underline{\\phantom{}\\hspace{3cm}}2024 г.\n")
    
    print("\\end{minipage}\n")
    
    print("\\vspace{24mm}")

    print("\\begin{center}")
    print("г. Владивосток\n")
    print("2024"
          "")
    print("\\end{center}")
    print("\\end{titlepage}")

    # print("\\newpage")

    print("\\section*{Постановка задачи}")

    print("Дана задача:")
    print("\\setcounter{MaxMatrixCols}{22}")
    print("\\[\\left\\{\\begin{aligned}")
    print("&c \\cdot x \\rightarrow \\max\\\\")
    print("&Ax \\le b\\\\")
    print("&x \\ge 0")
    print("\\end{aligned}")
    print("\\right.")
    print("\\]\n")

    print("Где \\(c\\) - неотрицательный 6-мерный вектор, \\(x\\) - неотрицательный", end="")
    print("6-мерный вектор неизвестных, который необходимо найти, \\(A\\) -", end="")
    print(" матрица 8x6, \\(b\\) - неотрицательный 8-мерный вектор")

    print_matrix(vec(data["A"]), "A")
    print_matrix(vec(data["b"]), "b")
    print_matrix(vec(data["c"]).T, "c")

    print("\nРешать будем симплекс-методом. Для начала приведем задачу к каноническому виду. Введем дополнительный 8-мерный вектор переменных \\(z = Ax - b\\)\n")
    print("Тогда к вектору c дописываем 8 нулей и рассматриваем вектор \\(\\begin{pmatrix}x\\\\z\\end{pmatrix}\\). К матрице \\(A\\) справа дописываем единичную матрицу получаем:\n")

    print("\\[\\left\\{\\begin{aligned}")
    print("&(c,0) \\cdot \\begin{pmatrix}x\\\\ z \\end{pmatrix} \\rightarrow \\max\\\\")
    print("&(AI)\\cdot\\begin{pmatrix}x\\\\ z \\end{pmatrix} = b\\\\")
    print("&x,z \\ge 0")
    print("\\end{aligned}")
    print("\\right.")
    print("\\]\n")

    print("\\section*{Прямая задача}")
    print("Составим симплекс-таблицу. Первая строка – расширенный вектор \\(c\\), где элементы мы запишем со знаком минус, чтобы решать задачу на минимум. Остальные строки – расширенная матрица \\(A\\), последний столбик – вектор \\(b\\), а первый элемент последнего столбца - значение целевой функции, равное 0.\n")
    print("Видим, что в первой строке (не включая значение целевой функции) есть отрицательные элементы, а значит оптимальное решение еще не найдено.\n")
    print("\\underline{Разрешающая колонка} находится путем выборки такого столбца, у которого элемент строки целевой функции отрицательный. Мы будем брать отрицательный элемент, максимальный по модулю.\n")
    print("\\underline{Разрешающей строкой} будет строка, содержащая наименьшее положительное отношение свободного числа к элементу разрешающего столбца.\n")
    print("Элемент, расположенный на пересечении разрешающих столбцаи строки, называется разрешающим элементом\n")

    m_data = data["matrices"][0]
    row = m_data["row"]
    column = m_data["column"]
    print_matrix(vec(data["matrices"][0]["mat"]), row=row, column=column)
    print("Начальное угловое решение:\n")
    print_matrix(vec(data["corner_solution"]).T)
    print_matrix_data(data["matrices"][0])
    print("Преобразовываем строки матрицы, то есть один из базисных столбцов станет \\textbf{не} базисным, а разрешающий столбец – базисным:\n")
    print("\\begin{enumerate}")
    print("\\item Элементы разрешающей строки делим на разрешающий элемент, так как разрешающий элемент = 1, то строка останется прежней.")
    print("\\item Преобразования остальных строк: Новая строка = Строка – элемент строки в разрешающем столбце * элемент разрешающей строки")
    print("\\end{enumerate}\n")

    for i in range(1, len(data["matrices"])):
        m_data = data["matrices"][i]
        row = m_data["row"]
        column = m_data["column"]
        print_matrix(vec(data["matrices"][i]["mat"]), row=row, column=column)
        if i != len(data["matrices"])-1:
            print("В первой строке (не включая значение целевой функции) есть отрицательные элементы, а значит оптимальное решение еще не найдено\n")
            print_matrix_data(data["matrices"][i])
            print("Преобразовываем строки матрицы")
        else:
            print("В первой строке (не включая значение целевой функции) НЕТ отрицательных элементов, а значит оптимальное решение найдено\n")
    print("\n\\underline{Оптимальное решение:}\n")
    print_matrix(data["optim"].T)
    print("\\underline{Целевая функция} =", data["obj_function"], end="\n\n")

    print("\\section*{Двойственная задача}")
    print("Двойственная задача будет выглядеть так:")

    print("\\[\\left\\{\\begin{aligned}")
    print("&b \\cdot x \\rightarrow \\min\\\\")
    print("&A^{T}y \\ge c\\\\")
    print("&y \\ge 0")
    print("\\end{aligned}")
    print("\\right.")
    print("\\]\n")

    print("Где \\(c\\) - неотрицательный 6-мерный вектор, \\(y\\) - неотрицательный", end="")
    print("8-мерный вектор неизвестных, который необходимо найти, \\(A^{T}\\) -", end="")
    print(" матрица 6x8, \\(b\\) - неотрицательный 8-мерный вектор\n")

    print_matrix(vec(data["A"]).T, "A^{T}")
    print_matrix(vec(data["b"]).T, "b")
    print_matrix(vec(data["c"]), "c")

    print("\nДля начала приведем задачу к каноническому виду. Введем дополнительный 6-мерный вектор переменных \\(z = Ax - b\\)\n")
    print("Тогда к вектору c дописываем 6 нулей и рассматриваем вектор \\(\\begin{pmatrix}y\\\\z\\end{pmatrix}\\). К матрице \\(A\\) справа дописываем единичную матрицу со знаком минус, получаем:\n")

    print("\\[\\left\\{\\begin{aligned}")
    print("&(c,0) \\cdot \\begin{pmatrix}y\\\\ z \\end{pmatrix} \\rightarrow \\min\\\\")
    print("&(A^{T}(-I))\\cdot\\begin{pmatrix}y\\\\ z \\end{pmatrix} = c\\\\")
    print("&y,z \\ge 0")
    print("\\end{aligned}")
    print("\\right.")
    print("\\]\n")

    print("Двойственная задача не имеет начального углового решения, что бы его найти необходимо решить вспомогательную задачу. Введем неотрицательный 8-мерный вектор \\(u\\), тогда получим равенство \\(Ax+u = b\\) и будем решать задачу не на наш минимум (начальный), а на сумму компонент вектора \\(u\\), получим")
    

    print("\\[\\left\\{\\begin{aligned}")
    print("&\\sum_{i=1}^{m} u_i \\rightarrow \\min\\\\")
    print("&(A^{T}(-I)I)\\cdot\\begin{pmatrix}y\\\\ z \\\\u \\end{pmatrix} = c\\\\")
    print("&y,z \\ge 0,~u\\ge0")
    print("\\end{aligned}")
    print("\\right.")
    print("\\]\n")

    print("И в качестве начальной точки для этой задачи рассмотрим \\(x = 0\\), а \\(u = b\\). Решаем симплекс-методом и если решение \\(u = 0\\), то тогда мы получим точку \\(x\\), для которой \\(x = b, ~x \\ge 0\\) и оно допустимое.")

    print("\\section*{Вспомогательная задача}")
    print("Составим симплекс-таблицу")
    print_matrix(vec(data["second_simplex_table"]), scale=0.7)

    print("Выделим базисные столбцы с помощью элементарных преобразований строк. К первой строке добавим все остальные строки, умноженные на -1. Получаем:\n")
    m_data = data["matrices_second"][0]
    row = m_data["row"]
    column = m_data["column"]
    print_matrix(vec(data["matrices_second"][0]["mat"]), scale=0.7, row=row, column=column)
    print("Начальное угловое решение\n")
    print_matrix(vec(data["corner_solution_second"]).T)
    print_matrix_data(data["matrices_second"][0])

    for i in range(1, len(data["matrices_second"])):
        m_data = data["matrices_second"][i]
        row = m_data["row"]
        column = m_data["column"]
        print_matrix(vec(data["matrices_second"][i]["mat"]), scale=0.7, row=row, column=column)
        if i != len(data["matrices_second"])-1:
            print_matrix_data(data["matrices_second"][i])
        else:
            print("В первой строке не осталось отрицательных элементов (не считая значение целевой функции) И \\(u = 0\\), значит найдено оптимальное решение для вспомогательной задачи, но начальное угловое и допустимое решение для исходной двойственной задачи.")

    print("\n\\underline{Оптимальное решение:}\n")
    print_matrix(data["optim_second"].T)

    print("\\section*{Решение двойственной задачи}")
    print("Составим симплекс-таблицу для двойственной задачи. Из прошлой матрицы убираем столбцы, соответствующие вектору \\(u\\), первуюстроку заменяем на расширенный вектор \\(b\\) и значение целевой функции приравниваем к нулю.")

    print_matrix(vec(data["third_simplex_table"]), scale=0.6)

    print("Выделяем базисные столбцы с помощью элементарных преобразований строк матрицы.")
    print_matrix(vec(data["matrices_third"][0]["mat"]), scale=0.60)

    print("Начальное угловое решение\n")
    print_matrix(vec(data["corner_solution_third"]).T)

    for i in range(1, len(data["matrices_third"])):
        m_data = data["matrices_third"][i]
        row = m_data["row"]
        column = m_data["column"]
        print_matrix(vec(data["matrices_third"][i]["mat"]), scale=0.6, row=row, column=column)
        if i != len(data["matrices_third"])-1:
            print_matrix_data(data["matrices_third"][i])
        else:
            print("В первой строке не осталось отрицательных элементов, значит найдено оптимальное решение.")

    print("\n\\underline{Оптимальное решение:}\n")
    print_matrix(data["optim_third"].T)
    print("\\underline{Целевая функция} =", -data["obj_function_third"], end="\n\n")

    print("\\section*{Ответ:}")
    print("Оптимальное решение:")
    print_matrix(data["optim"].T)
    print("Целевая функция прямой задачи =", data["obj_function"], end="\n\n")
    print("\nОптимальное решение:")
    print_matrix(data["optim_third"].T)
    print("Целевая функция двойственной задачи =", data["obj_function_third"])

    print("\\section*{Листинг}")
    # print("\\begin{lstlisting}")
    print("\\lstinputlisting[language=Python]{main.py}")
    # print("\\end{lstlisting}")
    print("\\end{document}")

