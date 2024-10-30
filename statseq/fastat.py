#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .fareader import Reader

class StatDict(dict):
    def __getattr__(self,name):
        return self.__getitem__(name)

class FaStat:
    def __init__(self,filePath) -> None:
        self.reader = Reader(filePath)
        self._fa_stat = self.fa_headle()

    def fa_headle(self):
        _fa_stat = StatDict({})

        _len_lst = []
        with self.reader as parser:
            for record in parser:
                _fa_stat.setdefault("allNum",0)
                _fa_stat["allNum"] += 1
                _fa_stat.setdefault("allLen",0)
                _fa_stat["allLen"] += record.seq_len
                _len_lst.append(record.seq_len)
                _fa_stat.setdefault("allN",0)
                _fa_stat["allN"] += record.base_num("N")
                _fa_stat.setdefault("allGC",0)
                _fa_stat["allGC"] += record.base_num("G")
                _fa_stat["allGC"] += record.base_num("C")
        _fa_stat.setdefault("minLen",min(_len_lst))
        _fa_stat.setdefault("maxLen",max(_len_lst))
        return _fa_stat
    
    @property
    def summary(self):
        # self._fa_stat = self.fa_headle()
        keys = "\t".join(self._fa_stat.keys())
        values = "\t".join(map(str,self._fa_stat.values()))
        return f"{keys}\n{values}"

    @property
    def fa_stat(self):
        return self._fa_stat
