import fritzbox.base.fb_base as fb
from lxml import etree
import logging
import time


class x_AVM_DE_OnTel(fb.fb_base):

    def GetCallerList(self, max=999):
        try:
            url = self._session.call_action('X_AVM-DE_OnTel', 'GetCallList')
            self._log.debug('GetCallerList %s' % url)
            # print(url)
            self._log.debug('url %s' % url['NewCallListURL'] + '&max=%s' % (max))
            root = etree.parse(url['NewCallListURL'] + '&max=%s' % (max)).getroot()
            #    except:
            #   print('failed to connect')

            #  self._log.debug('GetCallerList %s' % r.text)
            print(url)
            self._log.debug('url %s' % url['NewCallListURL'] + '&max=%s' % (max))
            root = etree.parse(url['NewCallListURL'] + '&max=%s' % (max)).getroot()
        except:
            print('failed to connect')

            self._log.error('Failed to connect to Fritzbox')
            root = None
        #   print(etree.tostring(root, pretty_print=True))

        return root

    def apiListPhoneBook(self):
        try:
            _pbList = self._session.call_action('X_AVM-DE_OnTel', 'GetPhonebookList')['NewPhonebookList'].split(',')
            self._log.debug('GetPhonebookList %s' % _pbList)
        except:
            self._log.error('Failed to read GetPhonebookList')
            _pbList = None

        return _pbList

    def apiGetPhonebook(self, id):
        # self._phonebook = {}
        info = {}
        phonebook = {}
        #  self._phonebook['DATE']= time.time()

        # self.listPhoneBook()
        try:
            _result = self._session.call_action('X_AVM-DE_OnTel', 'GetPhonebook', NewPhonebookId=id)
            self._log.debug('GetPhonebook %s' % _result)
            #  info['name'] = result['NewPhonebookName']
            # info['url'] = result['NewPhonebookURL']

            _pb = etree.parse(_result['NewPhonebookURL'])

        except:
            #  print('failed to connect')

            self._log.error('Failed to connect to Fritzbox')
            return 0

        # print(_pb.iter('contact'))
        for contact in _pb.iter('contact'):
            name = contact.findall('.//realName')
            nr = contact.findall('.//number')
            #  print(nr.findall('./type'))
            #     print(nr)
            phonebook[name[0].text] = [n.text.replace(' ', '') for n in nr]

        return phonebook

    def GetPhonebookList_old(self):
        info = {}
        try:
            url = self._session.call_action('X_AVM-DE_OnTel', 'GetPhonebookList')
            self._log.debug('GetPhonebookList %s' % url)

            result = self._session.call_action('X_AVM-DE_OnTel', 'GetPhonebook', NewPhonebookId=1)
            self._log.debug('GetPhonebook %s' % result)
            info['name'] = result['NewPhonebookName']
            info['url'] = result['NewPhonebookURL']

            _pb = etree.parse(info['url'])





        except:
            print('failed to connect')

            self._log.error('Failed to connect to Fritzbox')
        #  root = None
        #   print(etree.tostring(root, pretty_print=True))

        print(_pb)
        nrs = {}
        for contact in _pb.iter('contact'):
            name = contact.findall('.//realName')
            nr = contact.findall('.//number')
            #  print(nr.findall('./type'))
            #     print(nr)
            nrs[name[0].text] = [n.text.replace(' ', '') for n in nr]

        print(nrs)

        max = 0
        save = ''
        number = ''
        for key, item in nrs.items():
            #  print(key,item)
            #  print('kk',self.levenshtein(item,'841953200'))
            for i in item[:]:
                value = self.searchNumber(i, '841953200')
                print('result', key, i, value)
                if max < value:
                    max = value
                    save = key
                    number = i

            print('max', save, number, max)

        print('final', save, number, max)

        return

    def searchNumber(self, a, b):
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
