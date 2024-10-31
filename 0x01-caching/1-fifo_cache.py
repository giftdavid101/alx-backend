#!/usr/bin/env python3

'''FIFO caching'''

from threading import RLock
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''A class `FIFOCache` that inherits from
       `BaseCaching` and is a caching system.
    '''

    def __init__(self):
        super().__init__()
        self.__keys = []
        self.__rlock = RLock()

    def put(self, key, item):
        '''assign to the dictionary `self.cache_data` the
           `item` value for the key `key`
        '''

        if key is not None and item is not None:
            keyOut = self._balance(key)
            with self.__rlock:
                self.cache_data.update({key: item})
            if keyOut is not None:
                print('DISCARD: {}'.format(keyOut))

    def get(self, key):
        '''return the value in `self.cache_data` linked to `key`
        '''
        with self.__rlock:
            return self.cache_data.get(key, None)
