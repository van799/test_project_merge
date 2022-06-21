import sys

# здесь объявляется класс StreamData
class StreamData:
    def create(self, FIELDS, lst_values):

        if len(FIELDS) == len(lst_values):
            self.__dict__= dict(zip(FIELDS, lst_values))
            return True
        else:
            return False

class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


sr = StreamReader()
data, result = sr.readlines()


class StreamDataV2:
    def create(self, FIELDS, lst_values):

        if len(FIELDS) == len(lst_values):
            self.__dict__= dict(zip(FIELDS, lst_values))
            return True
        else:
            return False


class StreamReaderV2:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        sd = StreamDataV2()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


sr = StreamReaderV2()
data, result = sr.readlines()