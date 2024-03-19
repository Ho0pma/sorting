# # Quick sort / Быстрая сортировка
# def quick_sort(lst):
#     if len(lst) <= 1:  # условие выхода из рекурсии
#         return lst
#
#     # устанавливаем опорный элемент
#     support_element = lst[0]
#
#     # создаем списки элементы которого меньше, равны и больше опорного элемента
#     left = [i for i in lst if i < support_element]
#     middle = [i for i in lst if i == support_element]
#     right = [i for i in lst if i > support_element]
#
#     # принты для демонстрации как разбиваются списки
#     print('left:', left)
#     print('middle:', middle)
#     print('right:', right)
#     print('----------------')
#
#     # соединяем полученные списки в один
#     return quick_sort(left) + middle + quick_sort(right)
#
#
# print(quick_sort([5, 3, 8, 4, 6, 3, 2]))

# -------------------------------------------------------------------------------------------------------------------- #
# # Сортировка пузырьком

# n = 6
# lst = [5, 7, 4, 3, 8, 2]
#
# # верхний цикл отвечает сколько обходов нужно совершить
# # n - 1 тк нет необходимости последнего прогона. Оставшийся пузырек - минимальный.
# for run in range(n - 1):
#     # совершаем n - 1 итераций по массиву, сравнивая элементы.
#     # n - 1 тк последний элемент (i) не будет с чем сравнивать (i + 1 -- out of range)
#     # n - 1 - RUN -- чтобы не сравнивать с максимальным элементом предыдущего прохода
#     for i in range(n - 1 - run):
#         if lst[i] > lst[i + 1]:
#             print(f'Сравниваем {lst[i]} c {lst[i + 1]}')
#             # меняем местами элементы
#             lst[i], lst[i + 1] = lst[i + 1], lst[i]
#
#     print(f'Результат обхода № {run + 1}: {lst}')
#     print('----------------')

# -------------------------------------------------------------------------------------------------------------------- #
# Сортировка слиянием / merge_sort

# def merge_two_list(first_lst, second_lst):
#     print(f'fisrt_lst: {first_lst}, second_lst: {second_lst}')
#     # результирующий отсортированный список
#     result_lst = []
#
#     # два указателя, для первого и второго списков
#     i = j = 0
#
#     while i < len(first_lst) and j < len(second_lst):
#         # сравниваем элементы массивов:
#         if first_lst[i] < second_lst[j]:
#             # меньший элемент добавляем в результирующий список
#             result_lst.append(first_lst[i])
#             print(f'i_result_lst: {result_lst}')
#
#             # двигаем указатель
#             i += 1
#         else:
#             result_lst.append(second_lst[j])
#             print(f'j_result_lst: {result_lst}')
#             j += 1
#
#     # один из указателей точно останется меньше исходного списка
#     # оставшееся значение заносим в result_lst
#     if i < len(first_lst):
#         result_lst += first_lst[i:]
#         print(f'i_result_lst: {result_lst}')
#     if j < len(second_lst):
#         result_lst += second_lst[j:]
#         print(f'j_result_lst: {result_lst}')
#     return result_lst
#
#
# # функция в которой мы разбиваем массивы на мелкие
# def merge_sort(lst):
#     print(lst)
#     # точка выхода
#     if len(lst) == 1:
#         return lst
#
#     # ищем центр входного списка
#     middle = len(lst) // 2
#     # получаем два списка путем срезания основного по центру
#     # каждый полученный список left и right вызываем рекурсивно
#     left = merge_sort(lst[:middle])
#     right = merge_sort(lst[middle:])
#
#     # используем функцию, которая склеиваем два листа в один
#     # сортируя с помощью указателей
#     return merge_two_list(left, right)
#
#
# print(merge_sort([7, 5, 2, 3, 9, 8, 6]))

# -------------------------------------------------------------------------------------------------------------------- #
#  сортировка вставками / Insertion Sort

# def insertion_sort(lst):
#     N = len(lst)
#     # идет итерация с 1 и до конца списка
#     for i in range(1, N):
#         print(f'lst: {lst}')
#         # на каждой итерации i будет запускаться цикл j
#         # идущий от текущего i до начала списка
#         for j in range(i, 0, -1):
#             print(f'Сравниваю: {lst[j]} и {lst[j - 1]}')
#             # если предыдущий меньше - меняются местами
#             if lst[j] < lst[j - 1]:
#                 lst[j], lst[j - 1] = lst[j - 1], lst[j]
#                 print(f'тк lst[j] < lst[j - 1] обновляем lst: {lst}')
#             # если нет - цикл останавливается, тк слева остались только значения меньше текущего
#             else:
#                 print(f'{lst[j]} больше {lst[j - 1]} сравнивать слева нет смысла' )
#                 break
#     return lst
#
# print(insertion_sort([7, 5, 2, 3, 9, 8, 6]))

# -------------------------------------------------------------------------------------------------------------------- #
# сортировка выбором / selection sort

# def selection_sort(lst):
#     N = len(lst)
#
#     # берем итератор до предпоследнего элемента тк последняя итерация i
#     # будет гарантировано максимальным числом, те  последним
#     for i in range(N - 1):
#         # говорим, что первое число минимально
#         min_index = i
#
#         # второй цикл идет от i и до конца
#         for j in range(i + 1, N):
#             # если в этом цикле встречается элемент меньше установленного нами ранее
#             # запоминаем его индекс как минимальный
#             if lst[j] < lst[min_index]:
#                 min_index = j
#
#         # после того как нашли минимальный элемент - меняем его места с установленным ранее
#         if min_index != i:
#             lst[i], lst[min_index] = lst[min_index], lst[i]
#
#     return lst
#
# print(selection_sort([7, 5, 2, 3, 9, 8, 6]))


# -------------------------------------------------------------------------------------------------------------------- #
# СОРТИРОВКА С KEY
# при использовании sort или sorted можно использовать key, в котором будем говорить как именно будет сортироваться
# список (передавая в key какую либо функцию)

# # задача: отсортировать и вывести только четные, если не четные + сотка
# def key_sort(x):
#     return x if x % 2 == 0 else 100 + x
#
# a = [4, 3, -10, 1, 7, 12]
# b = sorted(a, key=key_sort)
# print(b)
#
# # задача: отсортировать по кол-ву символов
# cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]
# sorted_cities = sorted(cities, key=len, reverse=True)
# print(sorted_cities)
#
# # задача: отсортировать по первому символу
# sorted_cities = sorted(cities, key=lambda x: x[0])
# print(sorted_cities)
#
# # задача: отсортировать значения по правильному списку
# lst_in = ['Атос=лейтенант', 'Портос=прапорщик', "д'Артаньян=капитан", 'Арамис=лейтенант', 'Балакирев=рядовой']
# rank_order = ['рядовой', 'сержант', 'старшина', 'прапорщик', 'лейтенант', 'капитан', 'майор', 'подполковник', 'полковник']
# lst = [i.split('=') for i in lst_in]
# lst.sort(key=lambda x: rank_order.index(x[1]))
# print(lst)

# задача: отсортировать номерные знаки. В данном примере сначала идет сортировка по условию int,
# потом идет сортировка по условию str тк в key можно передать сразу несколько условий
# lst = ['ZZZ 800', 'aaa 45', 'eee 43', 'DDD 800', 'BBB 43', 'www 14']
# print(sorted(lst, key=lambda x: int(x.split()[1]))) # так отсортирует по одному условию
# print(sorted(lst, key=lambda x: (int(x.split()[1]), x.split()[0]))) # так отсортирует по двум

# -------------------------------------------------------------------------------------------------------------------- #
# TimSort

# тут сорт с аллокацией. Можно сделать добавление в result_lst по индексу
def merge_two_list(first_lst, second_lst):
    result_lst = []
    i = j = 0

    while i < len(first_lst) and j < len(second_lst):
        if first_lst[i] < second_lst[j]:
            result_lst.append(first_lst[i])
            i += 1
        else:
            result_lst.append(second_lst[j])
            j += 1

    if i < len(first_lst):
        result_lst += first_lst[i:]
    if j < len(second_lst):
        result_lst += second_lst[j:]

    return result_lst


def insertion_sort(arr, left, right):
    # добавляем 1 к left, чтобы итерация шла с 1-го элемента
    # к right добавляем 1 тк в range правая граница не включается (на первой итерации передается 31, а minrun = 32)
    for i in range(left + 1, right + 1):
        for j in range(i, left, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break

    return arr


def tim_sort(arr):
    min_run = 8    # устанавливаем минимальный размер подмассива
    n = len(arr)    # длинна всего массива

    # цикл идет с шагом min_run те если в n будет меньше элементов - возьмет сколько сможет
    for i in range(0, n, min_run):
        # передаем подмассивы определенного размера, сортируем их вставками
        insertion_sort(arr, i, min((i + min_run - 1), n - 1))  # на первом шаге передается: arr, 0, 31, 2

    # далее массив состоит из отсортированных подмассивов.

    # size - это указатель на элемент, слева от которого все отсортировано
    size = min_run

    while size < n:
        # берем двойной шаг, чтобы взять два отсортированных подмассива
        for start in range(0, n, size * 2):
            # вычисляем середину (конец первого списка) и конец - где оканчивается второй список
            middle = start + size - 1
            end = min((start + size * 2 - 1), (n - 1))

            # запускаем функцию слияния двух массивов
            merged_array = merge_two_list(arr[start:middle + 1], arr[middle + 1:end + 1])

            # меняем в исходном массиве с текущего старта по длину двух массивов новым отсортированным массивом
            arr[start:start + len(merged_array)] = merged_array

        # увеличиваем размер
        size *= 2

    return arr


print(tim_sort([17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))

# print([i for i in range(33)][::-1])

