from diaries.diary_ import Diary

name = input("Enter your username")
password = input("Enter your password")
diary: Diary = Diary(name, password)


def unlock_diary():
    pass_word = input("Enter your password: ")
    try:
        diary.unLocked(pass_word)
        main_menu()
    except Exception as exceptionInfo:
        print(exceptionInfo)
        main_menu()


def add_to_diary():
    title = input("Enter your title for the entry:")
    body = input("Enter the body of the title")
    try:
        diary.create_entry(title, body)
        main_menu()
    except Exception as exceptionInfo:
        print(exceptionInfo)
        unlock_diary()
        main_menu()


def update_diary():
    id = int(input("Enter the id for the diary to update: "))
    title = input("Enter the title of the diary to update")
    body = input("Enter the body of the diary")
    try:
        diary.update(id, title, body)
        main_menu()
    except Exception as exceptionInfo:
        print(exceptionInfo)
        main_menu()


def lock_diary():
    diary.lock()


def delete_entry():
    id = int(input("Enter the id of the entry"))
    try:
        diary.delete_entry(id)
        main_menu()
    except Exception as exceptionInfo:
        print(exceptionInfo)
        main_menu()


def operation_code(response):
    match response:
        case 1:
            add_to_diary()
        case 2:
            update_diary()
        case 3:
            unlock_diary()
        case 4:
            lock_diary()
        case 5:
            delete_entry()


def main_menu():
    main_menus = """
    =====================
    1 -> Add to a diary
    2 -> Update a diary
    3 -> Unlock diary
    4 -> Lock diary
    5 -> Delete Entry
    ===================
    """
    response = int(input(main_menus))
    operation_code(response)


main_menu()
