import pandas as pd
import os
import jieba
import numpy as np
import copy
## 載入自訂字典
KeyWords_path = "./keyWordsDB"
jieba.load_userdict(os.path.join(KeyWords_path, "AllKeyWords.txt"))

class KeyWordsComparator:
    def __read_key_words(self, path):
        key_words_list = []
        with open(path, "r", encoding="utf8") as r:
            for item in r.readlines():
                key_words_list.append(item.replace("\ufeff", "").strip())
        return key_words_list

    # 取得一文字檔的原始文章
    def __txt_raw_text(self):
        try:
            with open(os.path.join(self.txt_path, self.txt_file_name), "r", encoding="cp950") as txt_reader:
                text = txt_reader.read()
                text = text.replace("\n", "").replace("\u3000", "\n")
            return text
        except UnicodeDecodeError:
            with open(os.path.join(self.txt_path, self.txt_file_name), "r", encoding="utf8") as txt_reader:
                text = txt_reader.read()
                text = text.replace("\n", "").replace("\u3000", "\n")
            return text            

    def __init__(self, txt_path, txt_file_name):
        # 讀取 Round1, Round2_1 ~ Round2_4,  Round3_1 ~ Round3_4 KeysWords
        self.Round1 = self.__read_key_words(os.path.join(KeyWords_path,  "Poisoning KeyWords/Round1.txt"))
        self.Round2_1 = self.__read_key_words(os.path.join(KeyWords_path,  "Poisoning KeyWords/Round2_1.txt"))
        self.Round2_2 = self.__read_key_words(os.path.join(KeyWords_path,  "Poisoning KeyWords/Round2_2.txt"))
        self.Round2_3 = self.__read_key_words(os.path.join(KeyWords_path,  "Poisoning KeyWords/Round2_3.txt"))
        self.Round2_4 = self.__read_key_words(os.path.join(KeyWords_path,  "Poisoning KeyWords/Round2_4.txt"))
        self.Round3_1 = self.__read_key_words(os.path.join(KeyWords_path,  "Poisoning KeyWords/Round3_1.txt"))
        self.Round3_2 = self.__read_key_words(os.path.join(KeyWords_path,  "Poisoning KeyWords/Round3_2.txt"))
        self.Round3_3 = self.__read_key_words(os.path.join(KeyWords_path,  "Poisoning KeyWords/Round3_3.txt"))
        self.Round3_4 = self.__read_key_words(os.path.join(KeyWords_path,  "Poisoning KeyWords/Round3_4.txt"))

        self.txt_path = txt_path
        self.txt_file_name = txt_file_name
        self.txt_content = self.__txt_raw_text()
        self.segs = self.__get_content_segs()

    def __get_content_segs(self):
        return jieba.lcut(self.txt_content.strip())

    def Main_seg_and_stastic(self, df_mode = True):
        """
        變數宣告區
        """
        ##
        # 共用變數
        Marked_text = copy.deepcopy(self.txt_content)
        Marked_segs = copy.deepcopy(self.segs)

        # R1 variable
        R1_count_array = np.zeros(len(self.Round1))
        R1_keyW_list = []
        R1_count = 0
        R1_tf = 0

        # R21 variable
        R21_count_array = np.zeros(len(self.Round2_1))
        R21_keyW_list = []
        R21_count = 0
        R21_tf = 0

        # R22 variable
        R22_count_array = np.zeros(len(self.Round2_2))
        R22_keyW_list = []
        R22_count = 0
        R22_tf = 0

        # R23 variable
        R23_count_array = np.zeros(len(self.Round2_3))
        R23_keyW_list = []
        R23_count = 0
        R23_tf = 0

        # R24 variable
        R24_count_array = np.zeros(len(self.Round2_4))
        R24_keyW_list = []
        R24_count = 0
        R24_tf = 0

        # R31 variable
        R31_count_array = np.zeros(len(self.Round3_1))
        R31_keyW_list = []
        R31_count = 0
        R31_tf = 0

        # R32 variable
        R32_count_array = np.zeros(len(self.Round3_2))
        R32_keyW_list = []
        R32_count = 0
        R32_tf = 0

        # R33 variable
        R33_count_array = np.zeros(len(self.Round3_3))
        R33_keyW_list = []
        R33_count = 0
        R33_tf = 0

        # R34 variable
        R34_count_array = np.zeros(len(self.Round3_4))
        R34_keyW_list = []
        R34_count = 0
        R34_tf = 0

        for seg in self.segs:
            """
            處理Round 1 狀況
            """
            if seg in self.Round1:
                # 出現特徵詞的地方+1
                R1_count_array[self.Round1.index(seg)] += 1
                # 出現特徵詞的地方，在原文Mark
                if not ("<R1>" + seg + "</R1>" in Marked_text):
                    Marked_text = Marked_text.replace(seg, "<R1>" + seg + "</R1>")
                # 出現特徵詞的地方，在斷詞的list Mark
                try:
                    Marked_segs[Marked_segs.index(seg)] = "<R1>" + seg + "</R1>"
                except ValueError:
                    # print("ValueError")
                    pass
                # 出現的特徵詞放入 R1_keyW_list
                if not (seg in R1_keyW_list):
                    R1_keyW_list.append(seg)
            """
            處理Round 21 狀況
            """
            if seg in self.Round2_1:
                # 出現特徵詞的地方+1
                R21_count_array[self.Round2_1.index(seg)] += 1
                # 出現特徵詞的地方，在原文Mark
                if not ("<R21>" + seg + "</R21>" in Marked_text):
                    Marked_text = Marked_text.replace(seg, "<R21>" + seg + "</R21>")
                # 出現特徵詞的地方，在斷詞的list Mark
                try:
                    Marked_segs[Marked_segs.index(seg)] = "<R21>" + seg + "</R21>"
                except ValueError:
                    # print("ValueError")
                    pass
                # 出現的特徵詞放入 R21_keyW_list
                if not (seg in R21_keyW_list):
                    R21_keyW_list.append(seg)
            """
            處理Round 22 狀況
            """
            if seg in self.Round2_2:
                # 出現特徵詞的地方+1
                R22_count_array[self.Round2_2.index(seg)] += 1
                # 出現特徵詞的地方，在原文Mark
                if not ("<R22>" + seg + "</R22>" in Marked_text):
                    Marked_text = Marked_text.replace(seg, "<R22>" + seg + "</R22>")
                # 出現特徵詞的地方，在斷詞的list Mark
                try:
                    Marked_segs[Marked_segs.index(seg)] = "<R22>" + seg + "</R22>"
                except ValueError:
                    # print("ValueError")
                    pass
                # 出現的特徵詞放入 R22_keyW_listhttp://localhost:8888/notebooks/%E7%81%BD%E5%AE%B3%E4%BA%8B%E6%95%85%E5%B0%88%E6%A1%88/%E7%AC%AC%E4%BA%8C%E7%89%88-%E6%96%B0%E8%81%9E%E6%96%B7%E8%A9%9E%E7%AF%A9%E9%81%B8%E7%B3%BB%E7%B5%B1-0407.ipynb#
                if not (seg in R22_keyW_list):
                    R22_keyW_list.append(seg)
            """
            處理Round 23 狀況
            """
            if seg in self.Round2_3:
                # 出現特徵詞的地方+1
                R23_count_array[self.Round2_3.index(seg)] += 1
                # 出現特徵詞的地方，在原文Mark
                if not ("<R23>" + seg + "</R23>" in Marked_text):
                    Marked_text = Marked_text.replace(seg, "<R23>" + seg + "</R23>")
                # 出現特徵詞的地方，在斷詞的list Mark
                try:
                    Marked_segs[Marked_segs.index(seg)] = "<R23>" + seg + "</R23>"
                except ValueError:
                    # print("ValueError")
                    pass
                # 出現的特徵詞放入 R23_keyW_list
                if not (seg in R23_keyW_list):
                    R23_keyW_list.append(seg)
            """
            處理Round 24 狀況
            """
            if seg in self.Round2_4:
                # 出現特徵詞的地方+1
                R24_count_array[self.Round2_4.index(seg)] += 1
                # 出現特徵詞的地方，在原文Mark
                if not ("<R24>" + seg + "</R24>" in Marked_text):
                    Marked_text = Marked_text.replace(seg, "<R24>" + seg + "</R24>")
                # 出現特徵詞的地方，在斷詞的list Mark
                try:
                    Marked_segs[Marked_segs.index(seg)] = "<R24>" + seg + "</R24>"
                except ValueError:
                    # print("ValueError")
                    pass
                # 出現的特徵詞放入 R24_keyW_list
                if not (seg in R24_keyW_list):
                    R24_keyW_list.append(seg)
            """
            處理Round 31 狀況
            """
            if seg in self.Round3_1:
                # 出現特徵詞的地方+1
                R31_count_array[self.Round3_1.index(seg)] += 1
                # 出現特徵詞的地方，在原文Mark
                if not ("<R31>" + seg + "</R31>" in Marked_text):
                    Marked_text = Marked_text.replace(seg, "<R31>" + seg + "</R31>")
                # 出現特徵詞的地方，在斷詞的list Mark
                try:
                    Marked_segs[Marked_segs.index(seg)] = "<R31>" + seg + "</R31>"
                except ValueError:
                    # print("ValueError")
                    pass
                # 出現的特徵詞放入 R31_keyW_list
                if not (seg in R31_keyW_list):
                    R31_keyW_list.append(seg)
            """
            處理Round 32 狀況
            """
            if seg in self.Round3_2:
                # 出現特徵詞的地方+1
                R32_count_array[self.Round3_2.index(seg)] += 1
                # 出現特徵詞的地方，在原文Mark
                if not ("<R32>" + seg + "</R32>" in Marked_text):
                    Marked_text = Marked_text.replace(seg, "<R32>" + seg + "</R32>")
                # 出現特徵詞的地方，在斷詞的list Mark
                try:
                    Marked_segs[Marked_segs.index(seg)] = "<R32>" + seg + "</R32>"
                except ValueError:
                    # print("ValueError")
                    pass
                # 出現的特徵詞放入 R32_keyW_list
                if not (seg in R32_keyW_list):
                    R32_keyW_list.append(seg)
            """
            處理Round 33 狀況
            """
            if seg in self.Round3_3:
                # 出現特徵詞的地方+1
                R33_count_array[self.Round3_3.index(seg)] += 1
                # 出現特徵詞的地方，在原文Mark
                if not ("<R33>" + seg + "</R33>" in Marked_text):
                    Marked_text = Marked_text.replace(seg, "<R33>" + seg + "</R33>")
                # 出現特徵詞的地方，在斷詞的list Mark
                try:
                    Marked_segs[Marked_segs.index(seg)] = "<R33>" + seg + "</R33>"
                except ValueError:
                    # print("ValueError")
                    pass
                # 出現的特徵詞放入 R33_keyW_list
                if not (seg in R33_keyW_list):
                    R33_keyW_list.append(seg)
            """
            處理Round 34 狀況
            """
            if seg in self.Round3_4:
                # 出現特徵詞的地方+1
                R34_count_array[self.Round3_4.index(seg)] += 1
                # 出現特徵詞的地方，在原文Mark
                if not ("<R34>" + seg + "</R34>" in Marked_text):
                    Marked_text = Marked_text.replace(seg, "<R34>" + seg + "</R34>")
                # 出現特徵詞的地方，在斷詞的list Mark
                try:
                    Marked_segs[Marked_segs.index(seg)] = "<R34>" + seg + "</R34>"
                except ValueError:
                    # print("ValueError")
                    pass
                # 出現的特徵詞放入 R34_keyW_list
                if not (seg in R34_keyW_list):
                    R34_keyW_list.append(seg)

            """
            共同變數區
            """

            ### 在Round1 特徵詞出現的種類
            R1_count = sum(R1_count_array != 0)
            # 在Round1 特徵詞出現的詞頻
            R1_tf = sum(R1_count_array)
            """
            R2
            """
            ### 在Round21 特徵詞出現的種類
            R21_count = sum(R21_count_array != 0)
            # 在Round21 特徵詞出現的詞頻
            R21_tf = sum(R21_count_array)
            ### 在Round22 特徵詞出現的種類
            R22_count = sum(R22_count_array != 0)
            # 在Round22 特徵詞出現的詞頻
            R22_tf = sum(R22_count_array)
            ### 在Round23 特徵詞出現的種類
            R23_count = sum(R23_count_array != 0)
            # 在Round23 特徵詞出現的詞頻
            R23_tf = sum(R23_count_array)
            ### 在Round24 特徵詞出現的種類
            R24_count = sum(R24_count_array != 0)
            # 在Round24 特徵詞出現的詞頻
            R24_tf = sum(R24_count_array)
            """
            R3
            """
            ### 在Round31 特徵詞出現的種類
            R31_count = sum(R31_count_array != 0)
            # 在Round31 特徵詞出現的詞頻
            R31_tf = sum(R31_count_array)
            ### 在Round32 特徵詞出現的種類
            R32_count = sum(R32_count_array != 0)
            # 在Round32 特徵詞出現的詞頻
            R32_tf = sum(R32_count_array)
            ### 在Round33 特徵詞出現的種類
            R33_count = sum(R33_count_array != 0)
            # 在Round33 特徵詞出現的詞頻
            R33_tf = sum(R33_count_array)
            ### 在Round34 特徵詞出現的種類
            R34_count = sum(R34_count_array != 0)
            # 在Round34 特徵詞出現的詞頻
            R34_tf = sum(R34_count_array)

        if df_mode :
            return pd.DataFrame([[self.txt_file_name, R1_count_array, R1_keyW_list, R1_count, R1_tf, \
                       R21_count_array, R21_keyW_list, R21_count, R21_tf, \
                       R22_count_array, R22_keyW_list, R22_count, R22_tf, \
                       R23_count_array, R23_keyW_list, R23_count, R23_tf, \
                       R24_count_array, R24_keyW_list, R24_count, R24_tf, \
                       R31_count_array, R31_keyW_list, R31_count, R31_tf, \
                       R32_count_array, R32_keyW_list, R32_count, R32_tf, \
                       R33_count_array, R33_keyW_list, R33_count, R33_tf, \
                       R34_count_array, R34_keyW_list, R34_count, R34_tf, \
                       Marked_text, Marked_segs, len(self.segs)]], columns=["txt_file_name", "R1_count_array", "R1_keyW_list", "R1_count", "R1_tf",
                                                "R21_count_array", "R21_keyW_list", "R21_count", "R21_tf",
                                                "R22_count_array", "R22_keyW_list", "R22_count", "R22_tf",
                                                "R23_count_array", "R23_keyW_list", "R23_count", "R23_tf",
                                                "R24_count_array", "R24_keyW_list", "R24_count", "R24_tf",
                                                "R31_count_array", "R31_keyW_list", "R31_count", "R31_tf",
                                                "R32_count_array", "R32_keyW_list", "R32_count", "R32_tf",
                                                "R33_count_array", "R33_keyW_list", "R33_count", "R33_tf",
                                                "R34_count_array", "R34_keyW_list", "R34_count", "R34_tf",
                                                "Marked_text", "Marked_segs", "seg_number"])
        else:
            return [self.txt_file_name, R1_count_array, R1_keyW_list, R1_count, R1_tf, \
                       R21_count_array, R21_keyW_list, R21_count, R21_tf, \
                       R22_count_array, R22_keyW_list, R22_count, R22_tf, \
                       R23_count_array, R23_keyW_list, R23_count, R23_tf, \
                       R24_count_array, R24_keyW_list, R24_count, R24_tf, \
                       R31_count_array, R31_keyW_list, R31_count, R31_tf, \
                       R32_count_array, R32_keyW_list, R32_count, R32_tf, \
                       R33_count_array, R33_keyW_list, R33_count, R33_tf, \
                       R34_count_array, R34_keyW_list, R34_count, R34_tf, \
                       Marked_text, Marked_segs, len(self.segs)], \
                     ["txt_file_name", "R1_count_array", "R1_keyW_list", "R1_count", "R1_tf",
                                                "R21_count_array", "R21_keyW_list", "R21_count", "R21_tf",
                                                "R22_count_array", "R22_keyW_list", "R22_count", "R22_tf",
                                                "R23_count_array", "R23_keyW_list", "R23_count", "R23_tf",
                                                "R24_count_array", "R24_keyW_list", "R24_count", "R24_tf",
                                                "R31_count_array", "R31_keyW_list", "R31_count", "R31_tf",
                                                "R32_count_array", "R32_keyW_list", "R32_count", "R32_tf",
                                                "R33_count_array", "R33_keyW_list", "R33_count", "R33_tf",
                                                "R34_count_array", "R34_keyW_list", "R34_count", "R34_tf",
                                                "Marked_text", "Marked_segs", "seg_number"]      







