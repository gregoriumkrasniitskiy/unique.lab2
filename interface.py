import importlib.util


class TextInterface:
    def __init__(self):
        spec = importlib.util.spec_from_file_location("getBestStudent", "./second/best_student.py")
        self.bestStudMod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.bestStudMod)

        spec = importlib.util.spec_from_file_location("countNum", "./first/count_num.py")
        self.countNumMod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.countNumMod)

        self._errorObj_ = {
            'isError': False,
            'text': None
        }

    def textMenu(self):
        exitFlag = False
        menuPunctsList = ['0', '1', '2']
        usrResponse = ''

        while not exitFlag:
            if self._errorObj_['isError']:
                print('\n' + self._errorObj_['text'] + '\n')
            
            print("1 - Первое задание")
            print("2 - Второе задание")
            print("0 - Выход")

            usrResponse = input()

            if usrResponse not in menuPunctsList:
                self._errorObj_['isError'] = True
                self._errorObj_['text'] = 'Такого пункта нет в меню'
            else:
                if int(usrResponse) == 1:
                    numA = input('Введите первое число: ')
                    numB = input('Введите второе число: ')
                    print(self.countNumMod.countNum(numA, numB), '\n')
                elif int(usrResponse) == 2:
                    print(self.bestStudMod.getBestStudent(), '\n')
                elif int(usrResponse) == 0:
                    exitFlag = True

        

obj = TextInterface()
obj.textMenu()