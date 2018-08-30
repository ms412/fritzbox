
import fritzbox.api.x_AVM_DE_OnTel as x_AVM_DE_OnTel
import json
import logging

class callhistory(x_AVM_DE_OnTel.x_AVM_DE_OnTel):

    def _filterCall(self,type):
        _callerList = self.GetCallerList()

        _outgoing = []
        if _callerList is None:
            self._log.error('Cannot read the CallerList')
            return json.dumps({})

        for elem in _callerList.iter("Call"):
   #         print(elem.findall('.//' + 'Type')[0].text)
            #  _id[0].text
            #print('elem',elem)
            if type in elem.findall('.//' + 'Type')[0].text:
                # if len(elem):
                _caller = {}
                _caller['Id'] = elem.findall('.//' + 'Id')[0].text
                _caller['Date'] = elem.findall('.//' + 'Date')[0].text
                _caller['Called'] = elem.findall('.//' + 'Called')[0].text
                _caller['Caller'] = elem.findall('.//' + 'Caller')[0].text
                _caller['Name'] = elem.findall('.//' + 'Name')[0].text
                _caller['Duration'] = elem.findall('.//' + 'Duration')[0].text
                _outgoing.append(_caller)

        return json.dumps(_outgoing)

    def incommingCalls(self):
        _incomming = self._filterCall('1')
    #    print('1INCOMMING',_incomming)
        logging.debug('Incomming')
        return _incomming

    def missedCalls(self):
        _missed = self._filterCall('2')
     #   print('1MISSED',_missed)
        return _missed

    def outgoingCalls(self):
        _outgoing = self._filterCall('3')
      #  print('1OUTGOING', _outgoing)
        return _outgoing

    def activeCalls(self):
        return self._filterCall('9')

    def rejectedCalls(self):
        return self._filterCall('10')

    def activeOutgoingCalls(self):
        return self._filterCall('11')

