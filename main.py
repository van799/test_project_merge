import sys

# здесь объявляется класс StreamData
# добавляем коментарии для проверки мердж

class StreamData:
    def create(self, FIELDS, lst_values):

        if len(FIELDS) == len(lst_values):
            self.__dict__= dict(zip(FIELDS, lst_values))
            return True
        else:
            return False
# добавляем коментарии для проверки мердж

class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in_all = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in_all)
        return sd, res


sr = StreamReader()
data, result = sr.readlines()

# добавляем коментарии для проверки мердж
print(data)