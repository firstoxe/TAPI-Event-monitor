from typing import List
from models.ITForwardInformation import ITForwardInformation
from models.ITCallHub import ITCallHub
from models.ITAddress import ITAddress
from models.ITCallInfo import ITCallInfo, ITCallInfo2, CallInfoLong, CallInfoString
from models.ITCallNotificationEvent import ITCallNotificationEvent
import pythoncom, time
import win32com.client as win32
from models.Enums import TAPI_EVENT
from datetime import datetime as dt
cls = "TAPI.TAPI.1"  # имя модуля


class TapiEvents(win32.getevents(cls)):
    def OnEvent(self, ev1, ev2):
        print(f'Событие {TAPI_EVENT(ev1).name} | {dt.now()}')
        try:
            event = None
            if ev1 == TAPI_EVENT.TE_CALLNOTIFICATION.value:
                event = win32.Dispatch(ev2)
                obj = ITCallNotificationEvent(event)
                print(obj)
                print(ITCallInfo(obj.call))
                print(CallInfoLong(ITCallInfo(obj.call).CallInfoLong))
                print(CallInfoString(ITCallInfo(obj.call).CallInfoString))
            if ev1 == TAPI_EVENT.TE_CALLSTATE.value:
                event = win32.Dispatch(ev2)
                pass
            if ev1 == TAPI_EVENT.TE_ADDRESSDEVSPECIFIC.value:
                event = win32.Dispatch(ev2)
                pass
        except Exception as e:
            raise


if __name__ == '__main__':
    # Создаём кэш библиотеки
    ti = win32.Dispatch(cls)._oleobj_.GetTypeInfo()
    tlb, index = ti.GetContainingTypeLib()
    tla = tlb.GetLibAttr()
    win32.gencache.EnsureModule(tla[0], tla[1], tla[3], tla[4], bValidateFile=0)

    # начинаем работу с TAPi
    tapi = win32.Dispatch(cls)
    tapi.Initialize()  # Активация
    events = TapiEvents(tapi)  # Класс для событий
    tapi.EventFilter = sum([e.value for e in TAPI_EVENT])  # все события (Enums.TAPI_EVENT)

    for address in tapi.Addresses:  # Проходим по всему списку адресов
        if address.AddressName != 'STATION FFFF (UNPLUGGED)':  # Если адрес назначен, регистрируем его для уведомлений
            print('Станция - ', address.AddressName, ' TOKEN - ',
                  tapi.RegisterCallNotifications(address, True, True, 8, 0), 'Зарегистрирована')

    print('Мониторинг com сервера запущен, для остановки ctrl+c', dt.now())
    while True:
        # Trigger the event handlers if we have anything.
        pythoncom.PumpWaitingMessages()  # ожидаем события от com сервера
        time.sleep(0.01)  # Don't use up all our CPU checking constantly
