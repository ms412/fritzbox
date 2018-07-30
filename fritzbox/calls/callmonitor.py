import fritzbox.api.x_AVM_DE_OnTel as x_AVM_DE_OnTel
import json

class callmonitor(x_AVM_DE_OnTel.x_AVM_DE_OnTel):

    def __init__(self):
        print('Caller Object')
        self._callerlist = self.GetCallerList(max=1)

    def _filterCall(self,type):
        _callerList = self.GetCallerList()
        _outgoing = []
        for elem in _callerList.iter("Call"):
            #       print(elem.findall('.//' + 'Type')[0].text)
            #  _id[0].text
            if type in elem.findall('.//' + 'Type')[0].text:
                # if len(elem):
                _caller = {}
                _caller['Id'] = elem.findall('.//' + 'Id')[0].text
                _caller['Date'] = elem.findall('.//' + 'Date')[0].text
                _caller['Caller'] = elem.findall('.//' + 'Caller')[0].text
                _caller['Name'] = elem.findall('.//' + 'Name')[0].text
                _caller['Duration'] = elem.findall('.//' + 'Duration')[0].text
                _outgoing.append(_caller)

        return json.dumps(_outgoing)


    def currentActiveCalls(self):
        return self._filterCall('9')

    def currentActiveOutgoingCalls(self):
        return self._filterCall('11')
