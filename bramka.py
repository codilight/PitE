#!/usr/bin/python

import time
import random

class Gate:
    __states = ("close","open")
    __state = None

    def __init__(self):
        self.__state = self.__states[0]

    def open(self):
        self.__state = self.__states[1]

    def close(self):
        self.__state = self.__states[0]

    def status(self):
        return self.__state

class InvalidCoinError(Exception):
    pass

class CoinBox:
    __coins = []
    __status = None
    
    def __init__(self):
        self.__status = 0;

    def addCoin(self,coin):
        if self.__status == 0:
            if (type(coin) == int or type(coin) == float) and coin > 0:
                self.__coins.append(coin)
            else:
                self.__status = 1;
                raise InvalidCoinError("[Blad] Ktos wrzucil cos, co nie jest moneta! Pojemnik zatkany!\nOproznij go, aby przywrocic funkcjonalnosc.")
        else:
            print "Pojemnik na monety zatkany. Oproznij go!"

    def empty(self):
        self.__coins = []
        self.__status = 0

    def value(self):
        if self.__status == 0:
            return sum(self.__coins)
        else:
            return 0
    
class Human:

    def __init__(self):
        random.seed(time.time())

    def insertCoin(self):
        return random.randint(0,4)/2.0       


class System:

    __states = ("idle","acq","broken","open")
    __st = "idle"
    __nst = "idle"

    __human = None
    
    def run(self):
        while(True):
            time.sleep(1)
            self.__st = self.__nst

            if self.__st == "idle":
                print "\n--- Bramka zamknieta ---"
                print "Zbieram pieniadze..."
                coin = self.getCoin()
                try:
                    self.__coinbox.addCoin(coin)
                except InvalidCoinError, e:
                    print e
                    print "..."
                    time.sleep(3)
                    self.__coinbox.empty()
                    print "Gotowe :) Pojemnik oprozniony!"
                else:
                    print "\twrzucone", coin, "zl"
                self.__nst = "acq"
            elif self.__st == "acq":
                if self.__coinbox.value() >= self.__threshold:
                    print "Dobrze, wystarczy... Otwieram bramke ;)"
                    self.__nst = "open"
                else:
                    coin = self.getCoin()
                    try:
                        self.__coinbox.addCoin(coin)
                    except InvalidCoinError, e:
                        print e
                        print "..."
                        time.sleep(3)
                        self.__coinbox.empty()
                        print "Gotowe :) Pojemnik oprozniony!"
                    else:
                        print "\twrzucone", coin, "zl"
            elif self.__st == "broken":
                print "Bramka zepsuta. Wezwij "
            elif self.__st == "open":
                self.__coinbox.empty()
                self.__nst = "idle"  
                print "Bramka otwarta!"      

    __threshold = None
    __gate = None
    __coinbox = None

    def __init__(self,cost):
        self.__human = Human()
        self.__gate = Gate()
        self.__coinbox = CoinBox()
        self.__threshold = cost 
        __st = "idle"
        __nst = "idle"

    def getCoin(self):
        return self.__human.insertCoin()

if __name__ == "__main__":
    system = System(2) # dwa zlote, aby przejsc przez bramke
    system.run()

