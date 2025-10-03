#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: Maria Sedó González
@date: 2025/09/28
"""

# main.py
# import the needed libraries/modules

import pandas as pd
import re
import utils


def main():
    #load your data here
    data = utils.filename()
    #Menu loop and call functions from utils
    while True:
        c = utils.menu()
        if c == "1":
            utils.basic_information(data)
        elif c == "2":
            utils.search_keyword(data)
        elif c == "3":
            utils.count_word_frequencies(data)
        elif c == "4":
            utils.info_regex_email(data)
        elif c == "5":
            utils.dataframe_basic_stats(data)
        elif c == "6":
            utils.goodbye()
        else:
            print("\nOops, invalid choice. Remember to choose with a number (integer, 1-6).")
            continue



if __name__ == "__main__":
    main()
