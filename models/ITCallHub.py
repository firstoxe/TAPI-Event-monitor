from .Enums import CALLHUB_STATE


class ITCallHub(object):
    def __init__(self, cls_tapi):
        self.calls = list(cls_tapi.Calls)
        self.numCalls = cls_tapi.NumCalls
        self.state = CALLHUB_STATE(int(cls_tapi.State)).name

    def __str__(self):
        return (f'ITCallNotificationEvent.calls - {self.calls}\n'
                f'ITCallNotificationEvent.event - {self.numCalls}\n'
                f'ITCallNotificationEvent.callbackInstance - {self.state}')
