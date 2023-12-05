from unittest import TestCase

import pytest

from diaries.entry import Entry
from Bank.exceptions.WrongPinException import WrongPinException
from diaries.diary_ import Diary
from diaries.exceptions.entry_exception import EntryNotFoundException, DiaryUnlocked


class TestSomething(TestCase):
    def test_that_when_diary_is_created_it_is_always_locked(self):
        diary = Diary("user_name", "user_password")
        self.assertTrue(diary.isLocked())

    def test_that_diary_can_be_unlocked_with_the_right_password(self):
        diary = Diary("user_name", "user_password")
        diary.unLocked("user_password")
        self.assertFalse(diary.isLocked())

    def test_that_we_can_unlock_and_lock_the_diary(self):
        diary = Diary('user_name', 'user_password')
        diary.unLocked('user_password')
        diary.lock()
        self.assertTrue(diary.isLocked())

    def test_that_when_we_used_the_wrong_password_for_opening_a_diary_throw_exceptions(self):
        diary = Diary('user_name', 'user_password')
        with pytest.raises(WrongPinException) as diaryInfo:
            diary.unLocked('wrong_password')
        assert str(diaryInfo.value) == 'Wrong password'
        self.assertTrue(diary.isLocked())

    def test_that_a_diary_can_create_an_entry(self):
        diary = Diary('user_name', 'user_password')
        diary.unLocked('user_password')
        diary.create_entry('Tobi is a boy', 'I like reading, my hobby is always eating and playing')
        diary.lock()
        self.assertEqual(1, diary.number_of_entry())

    def test_that_we_create_an_entry_and_find_the_entry_the_title_will_be_the_same_to_one_given(self):
        diary = Diary('user_name', 'user_password')
        diary.unLocked('user_password')
        diary.create_entry('Tobi is a boy', 'I like reading, my hobby is always eating and playing')
        diary.lock()
        self.assertEqual(1, diary.number_of_entry())
        self.assertEqual('Tobi is a boy', diary.find_entry_by_id(1).get_title())

    def test_That_When_an_entry_is_not_created_and_we_find_entry_raises_an_exception(self):
        diary = Diary('user_name', 'user_password')
        with pytest.raises(EntryNotFoundException) as diaryInfo:
            diary.find_entry_by_id(1)
        assert str(diaryInfo.value) == 'Entry not found'
        self.assertEqual(0, diary.number_of_entry())

    def test_that_when_a_diary_is_not_unlocked_we_can_not_create_entry(self):
        diary = Diary('user_name', 'user_password')
        with pytest.raises(DiaryUnlocked) as diaryInfo:
            diary.create_entry('Tobi is a boy', 'I like reading, my hobby is always eating and playing')
        assert str(diaryInfo.value) == 'Diary locked'
        self.assertEqual(0, diary.number_of_entry())

    def test_that_entry_can_be_deleted_from_a_diary(self):
        diary = Diary('user_name', 'user_password')
        diary.unLocked('user_password')
        diary.create_entry('I am a boy', 'I love going to school and obeying my teacher')
        diary.create_entry('I am a girl', 'I love going to man house and also buying jewelry')
        self.assertEqual(2, diary.number_of_entry())
        diary.delete_entry(1)
        self.assertEqual(1, diary.number_of_entry())

    def test_that_when_entry_is_deleted_we_can_not_find_the_entry_again_in_the_entry(self):
        diary = Diary('user_name', 'user_password')
        diary.unLocked('user_password')
        diary.create_entry('I am a boy', 'I love going to school and obeying my teacher')
        diary.create_entry('I am a girl', 'I love going to man house and also buying jewelry')
        self.assertEqual(2, diary.number_of_entry())
        diary.delete_entry(1)
        with self.assertRaises(EntryNotFoundException):
            diary.find_entry_by_id(1)

    def test_that_we_can_update_a_diary_which_has_already_been_created(self):
        diary = Diary('user_name', 'user_password')
        diary.unLocked('user_password')
        diary.create_entry('I am a boy', 'I love going to school and obeying my teacher')
        diary.update(1, 'I am a girl', 'I love going to man house and also buying jewelry')
        entry: Entry = diary.find_entry_by_id(1)
        self.assertEqual('I am a girl', entry.get_title())
        print(entry)
