#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class FastaSeq:
    def __init__(self,header,sequence) -> None:
        self._deal_header(header)
        self._sequence = sequence.strip()
        
    def _deal_header(self,header):
        header_lst = header.strip().split(maxsplit=1)
        if len(header_lst) > 1:
            self._id = header_lst[0].replace(">","")
            self._description = header_lst[1]
        else:
            self._id = header_lst[0].replace(">","")
            self._description = None

    @property
    def id(self):
        return self._id
    
    @property
    def description(self):
        return self._description

    @property
    def seq(self):
        return self._sequence
    
    @property
    def seq_len(self):
        return len(self._sequence)

    @property
    def upper_seq(self):
        return self._sequence.upper()
    
    @property
    def lower_seq(self):
        return self._sequence.lower()

    def base_num(self,base):
        base = base.upper()
        upper_seq = self._sequence.upper()
        if base in upper_seq:
            _base_num = upper_seq.count(base)
            return _base_num
        else:
            return 0

    def GC_content(self,as_percentage=True):
        seq_len = self.seq_len
        g_num = self.base_num("G")
        c_num = self.base_num("C")
        gc_content = (g_num + c_num)/seq_len
        if as_percentage:
            return f"{gc_content*100:.2f}%"
        else:
            return f"{gc_content:.4f}" 

    @property
    def gc_content(self):
        return self.GC_content(as_percentage=False)
    
    def seq_reverse(self):
        return self._sequence[::-1]
    
    def seq_complement(self,reverse=False):
        base_dict  = {
            'A': 'T',
            'T': 'A',
            'C': 'G',
            'G': 'C',
            'N':'N'
            }
        if not reverse:
            return "".join([base_dict[base] for base in self.upper_seq])
        else:
            return "".join([base_dict[base] for base in reversed(self.upper_seq)])
