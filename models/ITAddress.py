from typing import List


class ITAddress(object):
    def __init__(self, cls_tapi):
        self.state = cls_tapi.State
        self.addressName = cls_tapi.AddressName
        self.serviceProviderName = cls_tapi.ServiceProviderName
        self.calls: List = list(cls_tapi.Calls)
        self.dialableAddress = cls_tapi.DialableAddress
        self.currentForwardInfo: object = cls_tapi.CurrentForwardInfo
        self.messageWaiting = cls_tapi.MessageWaiting
        self.doNotDisturb = cls_tapi.DoNotDisturb

    def __str__(self):
        return (f'ITAddress.state - {self.state}\nITAddress.addressName - {self.addressName}\n'
                f'ITAddress.serviceProviderName - {self.serviceProviderName}\n'
                f'ITAddress.dialableAddress - {self.dialableAddress}\n'
                f'ITAddress.currentForwardInfo - {self.currentForwardInfo}\n'
                f'ITAddress.messageWaiting - {self.messageWaiting}\n'
                f'ITAddress.doNotDisturb - {self.doNotDisturb}')