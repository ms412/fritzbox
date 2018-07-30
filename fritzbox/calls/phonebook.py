
import fritzbox.api.x_AVM_DE_OnTel as x_AVM_DE_OnTel
import time


class phonebook(x_AVM_DE_OnTel.x_AVM_DE_OnTel):
    _phonebook = {}

    def GetPhoneBook(self):
        self._phonebook['DATE'] = time.time()
        self.apiGetPhonebook(1)

        _pbList = self.apiListPhoneBook()

        for x in _pbList:
            print(x)
            self._phonebook[x]= self.apiGetPhonebook(int(x))
          #  print('test',self.GetPhonebook(int(x)))

        print(self._phonebook)
        return

    def LookupName(self,callerid):
        max = 0
        _callerName = ''
        _callerID = ''
        _date = self._phonebook.get('DATE',0)
        if _date + 10000 < time.time():
            self.GetPhoneBook()

        for key, item in self._phonebook.items():
            if isinstance(item,dict):
                for _name, _number in item.items():
                    for _id in _number[:]:
                        value = self._searchNumber(_id, callerid)
                     #   print(value)
                        if max < value:
                            max = value
                            _callerName = _name
                            _callerID = _id
      #  print('Result',_callerName,_callerID)
        return(_callerName,_callerID)

    def _searchNumber(self, a, b):
        #   print('input' ,a ,b)
        #    n, m = len(a), len(b)
        #    print('len' ,n ,m)
        if len(a) > len(b):
            min = len(b)
        else:
            min = len(a)

        for n in range(1, min):
            # while test:
            #   print(n)
            ax = a[-n]
            bx = b[-n]
            if ax != bx:
                #    n = n+1
                #     print(ax,bx,n)
                #  else:
                break
            #    test = False

        return n