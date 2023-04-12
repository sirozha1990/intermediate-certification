import json
import datetime

# Создаем пустой список для хранения заметок
notes = []

# Функция для сохранения заметок в файл
def save_notes():
    with open('notes.json', 'w') as f:
        json.dump(notes, f, indent=4)
    print('Заметки сохранены!')

# Функция для чтения заметок из файла
def read_notes():
    with open('notes.json', 'r') as f:
        notes = json.load(f)
    print('Список заметок:')
    for note in notes:
        print(f"ID: {note['id']}\nЗаголовок: {note['title']}\nТекст: {note['body']}\nДата создания: {note['created_at']}\nДата изменения: {note['updated_at']}\n")

# Функция для добавления заметок
def add_note():
    id = len(notes) + 1
    title = input('Введите заголовок заметки: ')
    body = input('Введите текст заметки: ')
    created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    updated_at = created_at
    note = {"id": id, "title": title, "body": body, "created_at": created_at, "updated_at": updated_at}
    notes.append(note)
    print('Заметка добавлена!')

# Функция для редактирования заметок
def edit_note():
    id = int(input('Введите ID заметки: '))
    for note in notes:
        if note['id'] == id:
            title = input('Введите новый заголовок заметки: ')
            body = input('Введите новый текст заметки: ')
            note['title'] = title
            note['body'] = body
            note['updated_at'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print('Заметка отредактирована!')
            return
    print('Заметка не найдена.')

# Функция для удаления заметок
def delete_note():
    id = int(input('Введите ID заметки: '))
    for note in notes:
        if note['id'] == id:
            notes.remove(note)
            print('Заметка удалена!')
            return
    print('Заметка не найдена.')

# Функция для чтения заметок из файла с фильтрацией по дате
def read_notes_by_date():
    date = input('Введите дату в формате ГГГГ-ММ-ДД: ')
    filtered_notes = [note for note in notes if note['created_at'].startswith(date)]
    if filtered_notes:
        print(f'Список заметок за {date}:')
        for note in filtered_notes:
            print(f"ID: {note['id']}\nЗаголовок: {note['title']}\nТекст: {note['body']}\nДата создания: {note['created_at']}\nДата изменения: {note['updated_at']}\n")
    else:
        print(f'Заметки за {date} не найдены.')

# Функция для вывода на экран выбранной записи
def display_note():
    id = int(input('Введите ID заметки: '))
    for note in notes:
        if note['id'] == id:
            print(f"ID: {note['id']}\nЗаголовок: {note['title']}\nТекст: {note['body']}\nДата создания: {note['created_at']}\nДата изменения: {note['updated_at']}\n")
            return
    print('Заметка не найдена.')

# Главный цикл программы
while True:
    print('\nВыберите действие:')
    print('1 - Сохранить')
    print('2 - Просмотр всех заметок')
    print('3 - Добавить заметку')
    print('4 - Редактировать заметку')
    print('5 - Удалить заметку')
    print('6 - Показать заметки за определенную дату')
    print('7 - Показать заметку по ID')
    print('0 - Выход')

    choice = input('> ')

    if choice == '1':
        save_notes()
    elif choice == '2':
        read_notes()
    elif choice == '3':
        add_note()
    elif choice == '4':
        edit_note()
    elif choice == '5':
        delete_note()
    elif choice == '6':
        read_notes_by_date()
    elif choice == '7':
        display_note()
    # elif choice == '8':
        # display_all_notes()
    elif choice == '0':
        break
    else:
        print('Неверный выбор. Попробуйте еще раз.')

