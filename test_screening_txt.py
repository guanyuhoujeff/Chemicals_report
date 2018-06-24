import KeyWordsComparison

## 輸入要分析的txt檔案存在的資料夾路徑以及要讀取的檔案名稱
txt_dir_path = "./test_file/Output/3-1高雄縣路竹鄉苯乙烯槽車翻覆事故(槽車類型)/txt"
txt_file = "3-1高雄縣路竹鄉苯乙烯槽車翻覆事故(槽車類型).txt"

## 產生特徵詞比對器
Comparator = KeyWordsComparison.KeyWordsComparator(txt_path=txt_dir_path,
                                                   txt_file_name=txt_file)
## 輸出分析結果，資料型態可以為list 或　DF
stastic_data, colname = Comparator.Main_seg_and_stastic(df_mode = False)
## Test
print(stastic_data)