from .Enums import CALLINFO_LONG, CALL_PRIVILEGE, CALL_STATE, CALLINFO_STRING


def param(fn, p):
    try:
        return fn(str(p))
    except:
        return None


class CallInfoLong(object):
    def __init__(self, fn):
        for item in CALLINFO_LONG:
            self.__setattr__(item.name, param(fn, item.value))

    def __str__(self):
        result = []
        for att in dir(self):
            if str(att)[0] != '_' and str(att)[1] != '_':
                result.append(f"{att} - {getattr(self, att)}")
        return '\n'.join(result)


class CallInfoString(object):
    def __init__(self, fn):
        for item in CALLINFO_STRING:
            self.__setattr__(item.name, param(fn, item.value))

    def __str__(self):
        result = []
        for att in dir(self):
            if str(att)[0] != '_' and str(att)[1] != '_':
                result.append(f"{att} - {getattr(self, att)}")
        return '\n'.join(result)


class ITCallInfo(object):
    def __init__(self, cls_tapi):
        self.address: object = cls_tapi.Address
        self.callState: str = CALL_STATE(int(cls_tapi.CallState)).name
        self.privilege: str = CALL_PRIVILEGE(int(cls_tapi.Privilege)).name
        self.callHub: object = cls_tapi.CallHub
        self.CallInfoLong: object = cls_tapi.CallInfoLong
        self.CallInfoString: object = cls_tapi.CallInfoString
        self.CallInfoBuffer: object = cls_tapi.CallInfoBuffer

    def __str__(self):
        return (f'ITCallInfo.address - {self.address}\nITCallInfo.callState - {self.callState}\n'
                f'ITCallInfo.privilege - {self.privilege}\nITCallInfo.callHub - {self.callHub}\n'
                f'ITCallInfo.CallInfoLong - {self.CallInfoLong}\nITCallInfo.CallInfoString - {self.CallInfoString}\n'
                f'ITCallInfo.CallInfoBuffer - {self.CallInfoBuffer}')

    def __repr__(self):
        return (f'ITCallInfo.address - {self.address}\nITCallInfo.callState - {self.callState}\n'
                f'ITCallInfo.privilege - {self.privilege}\nITCallInfo.callHub - {self.callHub}\n'
                f'ITCallInfo.CallInfoLong - {self.CallInfoLong}\nITCallInfo.CallInfoString - {self.CallInfoString}\n'
                f'ITCallInfo.CallInfoBuffer - {self.CallInfoBuffer}')


class ITCallInfo2(object):
    def __init__(self, cls_tapi):
        self.eventFilter = cls_tapi.EventFilter
        self.address: object = cls_tapi.Address
        self.callState: int = cls_tapi.CallState
        self.privilege = cls_tapi.Privilege
        self.callHub: object = cls_tapi.CallHub
        self.CallInfoLong = cls_tapi.CallInfoLong
        self.CallInfoString: CallInfoString = CallInfoString(cls_tapi.CallInfoString)
        self.CallInfoBuffer = cls_tapi.CallInfoBuffer

    def __str__(self):
        return (f'ITCallInfo.eventFilter - {self.eventFilter}\nITCallInfo.address - {self.address}\n'
                f'ITCallInfo.callState - {self.callState}\nITCallInfo.privilege - {self.privilege}\n'
                f'ITCallInfo.callHub - {self.callHub}\nITCallInfo.CallInfoLong - {self.CallInfoLong}\n'
                f'ITCallInfo.CallInfoString - {self.CallInfoString}\nITCallInfo.CallInfoBuffer - {self.CallInfoBuffer}')
