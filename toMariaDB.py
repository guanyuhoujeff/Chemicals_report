#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 18:12:14 2018

@author: jam

功能：將Dataframe資料寫入Maria資料庫

"""

import pymysql
pymysql.install_as_MySQLdb()
from sqlalchemy import create_engine
import pandas as pd

# =============================================================================
# 資料讀取
# =============================================================================

screening_result = pd.read_excel("chemicals_screening_result.xlsx")

# =============================================================================
# 資料前處理：寫入DB時，schema型態要明確定義，關鍵字的部份須為String
# =============================================================================

screening_result =  screening_result.sort_values(by=["R1_count", "R21_count", "R22_count"], ascending=False)
## data clean
screening_result[["txt_file_name", "Marked_text", "Marked_segs"]] = \
screening_result[["txt_file_name", "Marked_text", "Marked_segs"]].astype(str)

# =============================================================================
#  Write to MariaDB
#  ex: port : 3307, username, password = root
# =============================================================================

SQL_db_name = "Chemicalsdb"
engine = create_engine(r"mysql+mysqldb://root:root@127.0.0.1:3307/"+SQL_db_name+"?charset=utf8")
connection = engine.connect()

screening_result.to_sql("screening_result", con=connection, if_exists="replace")

connection.close()
