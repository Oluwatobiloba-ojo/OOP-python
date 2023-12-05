from src.Bank.exceptions.WrongPinException import WrongPinException
from src.diaries.entry import Entry
from src.diaries.exceptions.entry_exception import EntryNotFoundException, DiaryUnlocked


class Diary:
    def __init__(self, user_name, user_password):
        self._password = user_password
        self._locked = True
        self._number_of_entries = 0
        self._list_of_entries = []
        self.username = user_name

    def isLocked(self) -> bool:
        return self._locked

    def unLocked(self, password):
        self.validate(password)
        self._locked = False

    def lock(self):
        self._locked = True

    def validate(self, password):
        if self._password != password:
            raise WrongPinException("Wrong password")

    def create_entry(self, title, body):
        if self._locked:
            raise DiaryUnlocked('Diary locked')
        self._number_of_entries += 1
        number = self.generate_id()
        entry = Entry(number, title, body)
        self._list_of_entries.append(entry)

    def number_of_entry(self) -> int:
        return self._number_of_entries

    def find_entry_by_id(self, id) -> Entry:
        for entry in self._list_of_entries:
            if entry.get_id() == id:
                return entry
        raise EntryNotFoundException('Entry not found')

    def generate_id(self) -> int:
        return self._number_of_entries

    def delete_entry(self, id) -> None:
        self._number_of_entries -= 1
        entry = self.find_entry_by_id(id)
        self._list_of_entries.remove(entry)

    def update(self, id, title, body) -> None:
        new_entry: Entry = self.find_entry_by_id(id)
        new_entry.setTitle(title)
        new_entry.set_body(body)
