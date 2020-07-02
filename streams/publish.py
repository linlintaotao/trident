# coding= utf-8
# 观察者模式
from streams.QThreadSerial import SerialThread
from serial import Serial


class Publisher:

    def __init__(self):
        self._observers = []
        self._data = None

    def register(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
            print(self._observers)

    def unregister(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def unregisterAll(self):
        for observer in self._observers:
            self._observers.remove(observer)

    def notifyAll(self, data):
        if data is not None:
            self._data = data
        for obs in self._observers:
            if isinstance(obs, SerialThread):
                obs.notify(self._data)
            elif isinstance(obs, Serial):
                obs.write(self._data)