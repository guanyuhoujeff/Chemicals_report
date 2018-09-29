#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 02:47:26 2018

@author: jam
"""


import os
import pandas as pd

# =============================================================================
#  load txt chemicals_txt
# =============================================================================

chemicals_txt_path = "./chemicals_rawdata/chemicals_txt"
chemicals_txts = os.listdir(chemicals_txt_path)

all_txt_files = []
for txt_file in chemicals_txts:
    Comparator = KeyWordsComparison.KeyWordsComparator(txt_path=chemicals_txt_path,
                                                   txt_file_name=txt_file)
    stastic_data, colname = Comparator.Main_seg_and_stastic(df_mode = False)
    all_txt_files.append(stastic_data)
    
    

chemicals_screening_result = pd.DataFrame(all_txt_files, columns=colname)
chemicals_screening_result.to_excel("chemicals_screening_result.xlsx", index=False)