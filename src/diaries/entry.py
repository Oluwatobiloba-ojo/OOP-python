import datetime


class Entry:

    def __init__(self, id, title, body):
        self._id = id
        self._title = title
        self._body = body
        self._date = datetime.date.today()
        self._time = datetime.time

    def get_id(self):
        return self._id

    def get_title(self):
        return self._title

    def get_body(self):
        return self._body

    def setTitle(self, title):
        self._title = title

    def set_body(self, body):
        self._body += '\n' + body

    def __str__(self):
        return f'''
        ==============================================
        DATE:{self._date}           TIME: {self._time}
                     {self.get_title()}
        {self.get_body()}
        =================================================
        '''
