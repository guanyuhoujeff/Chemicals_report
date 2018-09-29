# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 22:58:34 2018

@author: user
"""

from chemicals_api.convert import Processing_DOCX

## 輸入DOCX檔案存在的資料夾路徑以及要讀取的檔案名稱
docx_path = "./test_file/test_docx"
docx_file = '桃園縣蘆竹鄉某公司爆炸事故.docx'

## 處理PDF檔的類別物件
docx_opject = Processing_DOCX.DOCXReader(
        read_docx_path = docx_path, 
        docx_file_name = docx_file )

## 可以將讀取到的文字以及圖片存在本地端
Output_path = "./test_file/Output/"
docx_opject.save_txt_file(Output_path)
print(docx_opject.content)

