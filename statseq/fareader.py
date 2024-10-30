#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gzip
from pathlib import Path
from typing import List,Dict

from .fastaseq import FastaSeq

class Reader:
    def __init__(self, filepath: Path) -> None:
        self.filepath = Path(filepath)
        if self.filepath.suffix.strip(".") == "gz":  # for linux and windowns
            self.file = gzip.open(self.filepath,"rt")
        else:
            self.file = open(self.filepath, 'r')
        self.current_id = None
        self.sequence = []

    def __iter__(self):
        return self

    def __next__(self):
        line = self.file.readline().strip()  
        while line:
            if line.startswith(">"): 
                if self.current_id:  
                    seq_to_return = "".join(self.sequence)
                    previous_id = self.current_id
                    self.current_id, self.sequence = line, []  
                    return FastaSeq(previous_id,seq_to_return)
                else:

                    self.current_id = line
                    self.sequence = []
            else:
                self.sequence.append(line)

            line = self.file.readline().strip()

        if self.current_id:
            seq_to_return = "".join(self.sequence)
            previous_id = self.current_id
            self.current_id = None
            return FastaSeq(previous_id,seq_to_return)
        raise StopIteration

    def close(self):
        self.file.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()