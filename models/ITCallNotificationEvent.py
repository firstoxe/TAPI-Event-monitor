from .Enums import CALL_NOTIFICATION_EVENT


class ITCallNotificationEvent(object):
    def __init__(self, cls_tapi):
        """

        :param cls_tapi:
        """
        self.call: object = cls_tapi.Call  # ITCallInfo
        self.event = CALL_NOTIFICATION_EVENT(int(cls_tapi.Event)).name
        self.callbackInstance: int = cls_tapi.CallbackInstance

    def __str__(self):
        return (f'ITCallNotificationEvent.call - {self.call}\n' 
               f'ITCallNotificationEvent.event - {self.event}\n' 
               f'ITCallNotificationEvent.callbackInstance - {self.callbackInstance}')
