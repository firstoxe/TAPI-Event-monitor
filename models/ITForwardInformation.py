class ITForwardInformation(object):
    def __init__(self, cls_tapi):
        self.numRingsNoAnswer = cls_tapi.NumRingsNoAnswer
        self.forwardTypeDestination = cls_tapi.ForwardTypeDestination
        self.forwardTypeCaller = cls_tapi.ForwardTypeCaller

    def __str__(self):
        return (f'numRingsNoAnswer - {self.numRingsNoAnswer}\n'
                f'numRingsNoAnswer - {self.forwardTypeDestination}\n'
                f'numRingsNoAnswer - {self.forwardTypeCaller}')
