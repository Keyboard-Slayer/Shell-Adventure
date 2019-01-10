#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

class History:
    def __init__(self, home: str):
        if not os.path.isfile(os.path.join(home, ".bash_history")):
            open(os.path.join(home, ".bash_history"), 'w').close()
        self.hist = open(os.path.join(home, ".bash_history"), 'a+')


    def __getitem__(self, index: int) -> str:
        self.hist.seek(0)
        return self.hist.readlines()[index][:-1]

    def append(self, line: str):
        self.hist.readlines()
        self.hist.write(f"{line}\n")
