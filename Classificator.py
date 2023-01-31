# ==========================< Импорты  Revit >==========================

import clr
clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Mechanical import *
import System
from System.Collections.Generic import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

clr.AddReference('RevitNodes')
import Revit
clr.ImportExtensions(Revit.Elements)

# ==================================<>==================================
# =========================< Исходные данные >==========================

# Переменные текущего файла
doc = DocumentManager.Instance.CurrentDBDocument
filename = Document.PathName.GetValue(doc)

# Параметры записи
input_answers = IN[0]

# Входные данные для поиска и отбора элементов
input_table = IN[1]

# Константы которые нельзя обойти
category_name = "Категория"
section_column_name = "Раздел"

# Словарь встроенных категорий
built_in_categories_dict = {
    "Арматура воздуховодов" : BuiltInCategory.OST_DuctAccessory,
    "Арматура трубопроводов" : BuiltInCategory.OST_PipeAccessory,
    "Воздуховоды" : BuiltInCategory.OST_DuctLinings,
    "Воздухораспределители" : BuiltInCategory.OST_DuctTerminal,
    "Выключатели" : BuiltInCategory.OST_LightingDevices,
    "Гибкие воздуховоды" : BuiltInCategory.OST_FlexDuctCurves,
    "Гибкие трубы" : BuiltInCategory.OST_FlexPipeCurves,
    "Кабельные лотки" : BuiltInCategory.OST_CableTray,
    "Короба" : BuiltInCategory.OST_Conduit,
    "Обобщенные модели" : BuiltInCategory.OST_GenericModel,
    "Оборудование" : BuiltInCategory.OST_MechanicalEquipment,
    "Осветительные приборы" : BuiltInCategory.OST_LightingFixtures,
    "Сантехнические приборы" : BuiltInCategory.OST_PlumbingFixtures,
    "Соединительные детали воздуховодов" : BuiltInCategory.OST_DuctFitting,
    "Соединительные детали кабельных лотков" : BuiltInCategory.OST_CableTrayFitting,
    "Соединительные детали коробов" : BuiltInCategory.OST_ConduitFitting,
    "Соединительные детали трубопроводов" : BuiltInCategory.OST_PipeFitting,
    "Спринклеры" : BuiltInCategory.OST_Sprinklers,
    "Трубы" : BuiltInCategory.OST_PipeCurves,
    "Электрические приборы" : BuiltInCategory.OST_ElectricalFixtures,
    "Электрооборудование" : BuiltInCategory.OST_ElectricalEquipment
}

# =============================< РЕМАРКИ >==============================
# =====================< Объявление функций Revit >=====================

# Функция возвращает все элементы категории по имени категории
def get_all_elements_category_by_name(doc, category_dict, category):
	# Если тип категории строка:
	if type(category) is str:
		# Попытаться:
		try:
			# Получить элементы по встроенной категории полученной из словаря встроенных категорий
			return FilteredElementCollector(doc).OfCategory(category_dict.get(category)).WhereElementIsNotElementType().ToElements()
		# При ошибке типа:
		except TypeError:
			# Вернуть пустой список
			return []
	# Иначе если тип категории список:
	elif type(category) is list:
		# Рекурсия на каждый элемент списка:
		return [get_all_elements_category_by_name(doc, category_dict, category_item) for category_item in category]
	# Пустой список, если ни одной условие не выполнено
	return []

# Функция возвращает имя рабочего набора элемента
def GetWorksetName(item):
    item = UnwrapElement(item)
    if hasattr(item, 'WorksetId'):
        return item.Document.GetWorksetTable().GetWorkset(item.WorksetId).Name
    else:
        return None

# Функция возвращает имя типа системы элемента
def GetSystemTypeName(element):
    sys_type = element.LookupParameter('Тип системы')
    try:
        sys_type = element.Document.GetElement(sys_type.AsElementId())
        return sys_type.ToDSType(True).Name
    except AttributeError:
        return None

# Функция возвращает имя системы элемента
def GetFamilyName(item):
    item = UnwrapElement(item)
    item = item.Document.GetElement(item.GetTypeId())
    if hasattr(item, 'FamilyName'):
        return item.FamilyName
    else:
        return None

# Функция возвращает значение параметра элемента
def GetParameter(item, par):
    if par == 'Рабочий набор':
        return GetWorksetName(item)
    elif par == 'Тип системы':
        return GetSystemTypeName(item)
    elif par == 'Имя семейства':
        return GetFamilyName(item)
    else:
        return item.LookupParameter(par).AsString()

# Функция возвращает несоответствующие значениям параметры и их значения
def check_parameters_values(el, parameters_list):
    names = []
    values = []
    for parameter_name, parameter_value in zip(parameters_list[0], parameters_list[1]):
        if el.LookupParameter(parameter_name).AsString() != parameter_value:
            names.append(parameter_name)
            values.append(parameter_value)
    if names != []:
        return [names,values]
    else:
        return None

# =================< Конец объявления функций Revit >===================

# ========================< Объявление функций >========================

# Функция получения первого индекса значения из списка значений
def get_first_index(lst, val):
    try: # Попытаться:
        return lst.index(val) # Вернуть индекс значения из списка
    except ValueError: # Исключение
        return None # Вернуть "Пусто"

# Фунция получения списка первых индексов списка значений из списка значений
def get_index_list(lst, val_lst):
    return [get_first_index(lst, val) for val in val_lst]

# Функция возвращает список значений lst_small из списка lst_big
def check_list_by_list(lst_big, lst_small):
    return [lst_big[v] for v in get_index_list(lst_big, lst_small) if v is not None]

# Функция забирает из списка data_list список значений по индексам
def take_items_by_index_list(data_list, index_list):
    return [data_list[i] for i in index_list]

# Функция пополнения словаря вопросов
def update_questions_book(questions_book, category, questions, words, unique_words):
    # Для текущего вопроса и слова в скомпонованных списках вопросов и слов:
    for question, word in zip(questions, words):
        # Если слово не пустое:
        if word is not None and word != "":
            # Если категория не существует в словаре:
            if questions_book.get(category) is None:
                # Создать такую категорию
                questions_book.update({category : {}})
            # Если текущего вопроса нет в категории:
            if questions_book.get(category).get(question) is None:
                # Создать такой вопрос с пустым списком слов и ключей
                questions_book[category].update({question : [[],[]]})
            # Получить из словаря список ключей по категории и текущему вопросу
            words_list = questions_book.get(category).get(question)[0]
            # Получить из словаря список слов по категории и текущему вопросу
            keys_list = questions_book.get(category).get(question)[1]
            # Если ключ слова (индекс слова в списке уникальных слов) отсутствует в полученном списке
            if unique_words.index(word) not in keys_list:
                # Добавить ключ в список ключей
                keys_list.append(unique_words.index(word))
                # Добавить слово в список слов
                words_list.append(word)
                # Обновить словарь по данной категории и данному вопросу обновленными списками
                #questions_book.get(category).get(question).update(dict(zip(words_list, keys_list)))
                questions_book.get(category).update({question : [words_list, keys_list]})
            del(keys_list, words_list) # Стереть списки ключей и списки слов

# Функция пополнения словаря рабочей тетради
def update_word_book(wordbook, words, questions, unique_words):
    # Для слова и вопроса в списках слов и вопросов
    for question, word in zip(questions, words):
        # Если слово не пустое
        if word is not None and word != "":
            # Если в словаре нет такого вопроса
            if wordbook.get(question) is None:
                # Добавление вопроса
                wordbook.update({question : {}})
            # Если слова с таким ключом нет:
            if wordbook.get(question).get(unique_words.index(word)) is None:
                # Внести новое слово с ключом
                wordbook.get(question).update({unique_words.index(word) : {word : unique_words.index(word)}})
    del(question, word) # Стереть вопрос и слово

# Функция пополнения словаря ответов
def update_answers_book(answers_book, category, words, unique_words, answers, values):
    # Если в словаре нет такой категории
    if answers_book.get(category) is None:
        # Добавление категории
        answers_book.update({category : {}})
    # Создание пустого списка ключей
    keys = []
    # Если список слов пуст, то:
    if list(filter(bool, words)) == []:
        # Выдать ключ 0
        keys.append(0)
    # Иначе, если список слов не пуст, то:
    else:
        # Для каждого отдельного слова
        for word in words:
            # Если оно не пустое
            if word is not None and word != "":
                # Добавить в ключ индекс слова из списка уникальных
                keys.append(unique_words.index(word))
    if len(keys) > 1: # Если длина ключа больше 1
        keys = frozenset(keys) # Превратить ключи в замороженный набор
    else: # Иначе, если в списке один ключ, то:
        keys = keys[0] # взять из списка его значение
    # Список ответов с непустыми значениями и список непустых значений ответов
    unpivoted_value = (tuple([answer for answer, value in zip(answers, values) if value is not None and value != ""]),
                       tuple([value for value in values if value is not None and value != ""]))
    # Добавить в словарь пару: ключ, ответы с их не пустыми значениями
    answers_book.get(category).update({keys : unpivoted_value})
    del(keys, unpivoted_value) # Освободить ключ и списки ответов

# Функция создания черновика словаря по категории и вопросам
def draft_create(category, current_questions, wordbook):
    new_dict = {}
    # Если получен раздел словаря с вопросами
    if current_questions is not None:
        # Для каждого вопроса словаря
        for question in current_questions.keys():
            # Если по данному вопросу в новом словаре нет ключа
            if new_dict.get(question) is None:
                # Создать раздел и в нем по пустому ключу пустое множество
                new_dict.update({question : {None : set()}})
                # Для каждого пункта в текущем вопросе:
                for index in list(current_questions.get(question)[1]):
                    # Для каждого слова и ключа в текущем пункте:
                    for item, value in zip(list(wordbook.get(question).get(index).keys()), list(wordbook.get(question).get(index).values())):
                        # Добавить в новый словарь в текущем вопросе слово и ключ
                        new_dict.get(question).update({item : value})
    return new_dict

# Функция подбора корректного ответа по содержанию в списке
def what_this_mean(familiar_words, new_word):
    for word in familiar_words:
        if word in new_word:
            return word
    return new_word

# Функция уточнения ключа
def get_my_key_please(new_word, familiar_words, draft, word_book):
    # Запрос ключа с предварительным подбором к заданному списку
    key = draft.get(what_this_mean(familiar_words, new_word))
    if key is not None:
        # Занести в словари слово с подобранным ключом
        draft.update({new_word : key})
        word_book.get(key).update({new_word : key})
    else:
        # Занести новое слово в черновике в набор неверных слов
        err_set = draft.get(None)
        err_set.update(set([new_word]))
        draft.update({None : err_set})
    return key

# Функция получения ключа по одному вопросу
def get_my_key(word, correct_answers, draft, word_book):
    if word not in draft.get(None):
        key = draft.get(word)
        if key is not None:
            return key
        else:
            # Запросить ключ с изучением слова
            return get_my_key_please(word, correct_answers, draft, word_book)
    return None

# Функция опроса элемента и запроса ключей
def get_my_keys(element, questions, draft, wordbook):
    key_set = []
    if questions is not None:
        for question in list(questions.keys()):
            word = GetParameter(element, question)
            if word is not None and word != "":
                # Запросить ключ по полученному слову
                key = get_my_key(word, questions.get(question)[0], draft.get(question), wordbook.get(question))
                if key is not None:
                    key_set.append(key)
    if len(key_set) == 1:
        # Вернуть ключ
        return key_set[0]
    elif len(key_set) > 1:
        # Вернуть замороженный набор ключей
        return frozenset(key_set)
    else:
        # Вернуть халявный ключ
        return 0

# ==========================< ЧАСТЬ I УЛИКИ >===========================

# Получение заголовков столбцов
headers = input_table.pop(0)
# Получение индекса столбца разделов
section_index = get_first_index(headers, section_column_name)
# Удаление секции из заголовоков
del(headers[section_index])
# Получение индекса столбца категорий
category_index = get_first_index(headers, category_name)
# Создание списка категорий
categories_query = []

# Для каждой записи таблицы начиная с конца в обратном порядке
for i in reversed(range(len(input_table))):
    # Секция по индексу секции отрывается от записи
    section = input_table[i].pop(section_index)
    # Если тип данных строка и она содержится в имени файла
    if type(section) is str and section in filename:
        # Категория по индексу категории
        category = input_table[i][category_index]
        # Если категория не в списке на запрос категорий
        if category not in categories_query:
            # Добавить категорию в этот список
            categories_query.append(category)
    # Иначе
    else:
        # Удалить запись из таблицы
        del input_table[i]

# ======================< ЧАСТЬ II РАССЛЕДОВАНИЕ >======================

# Создание списка уникальных слов (Резервируем нулевой индекс для ответов без вопросов)
unique_words = [None]
# Создание словаря вопросов
questions_book = {}
# Создание рабочего словаря
wordbook = {}
# Создание словаря ответов
answers_book = {}

# Уточнение списков
questions = tuple(set(headers)-set(input_answers)-set([category_name]))
answers = tuple(check_list_by_list(headers, input_answers))

# Для номера строки в диапазоне номеров равном длине массива записей
for index in range(len(input_table)):
    # Оторвать первую строку от данных
    record = input_table.pop(0)
    # Взять из строки категорию по индексу
    category = record[headers.index(category_name)]
    # Взять из строки слова вопросов по списку индексов
    questions_words = take_items_by_index_list(record, get_index_list(headers, questions))
    # Взять из строки слова ответов по списку индексов
    answers_values = take_items_by_index_list(record, get_index_list(headers, answers))
    # Пополнить список уникальных слов
    unique_words.extend([v for v in list(filter(bool, questions_words)) if v not in unique_words])
    # Пополнить словарь вопросов
    update_questions_book(questions_book, category, questions, questions_words, unique_words)
    # Пополнить рабочую тетрадь
    update_word_book(wordbook, questions_words, questions, unique_words)
    # Пополнить словарь ответов
    update_answers_book(answers_book, category, questions_words, unique_words, answers, answers_values)
# Очистить ненужные переменныеяуу
del(record, category, questions_words, answers_values)
del(headers, category_name, questions, answers, unique_words)

# ==============< ЧАСТЬ III ПОВЕСТКИ ДОПРОСЫ ПРИЗНАНИЯ >================

# Создание  списков для вывода
out_elements = []
out_parameters = []
out_values = []

# Запуск циклов по длине списка категорий:
for category in categories_query:
    # Получить подсписок элементов категории
    elements = get_all_elements_category_by_name(doc, built_in_categories_dict, category)
    # Если подсписок элементов не пуст:
    if elements != []:
        # Получить раздел словаря вопросов по текущей категории
        current_questions = questions_book.get(category)
        # Получить раздел словаря ответов по текущей категории
        current_answers = answers_book.get(category)
        # Создать черновик словаря по текущей категории
        draft = draft_create(category, current_questions, wordbook)
        # Запуск циклов по длине подсписка
        for element in elements:
            # Допросить элемент, найти в ответах ключевые слова
            keys = get_my_keys(element, current_questions, draft, wordbook)
            # По ключевым словам получить ответы в словаре ответов
            answers = current_answers.get(keys)
            # Если ответ есть:
            if answers is not None:
                # Сверить значение ответа и значения параметров
                answers = check_parameters_values(element, answers)
                # Если выявлены несоответсвия:
                if answers is not None:
                    # Добавить в список на выход элемент
                    out_elements.append(element)
                    # Так же имена параметров требующих корректировку
                    out_parameters.append(answers[0])
                    # И значения параметров, требующих корректировки
                    out_values.append(answers[1])

# =========================< ЧАСТЬ IV ПРИГОВОРЫ >=======================

# Создание транзакции записи
TransactionManager.Instance.EnsureInTransaction(doc)
# Параллельный перебор элементов списков
for el, pars, vals in zip(out_elements, out_parameters, out_values):
    # Для каждого параметра и значения в параметрах и значениях элемента
    for par, val in zip(pars, vals):
        # Изменение значения параметра
        el.LookupParameter(par).Set(val)
# Закрытие транзакции записи
TransactionManager.Instance.TransactionTaskDone()

# ==========================< ЧАСТЬ V ЭПИЛОГ >==========================

tmp = []
for key1 in list(wordbook.keys()):
    tmp1 = []
    for key2 in list(wordbook.get(key1).keys()):
        tmp1.append(wordbook.get(key1).get(key2).keys())
    tmp.append([key1, tmp1])

OUT = [out_elements, out_parameters, out_values, tmp]
