import sys
import importlib
importlib.reload(sys)
import os

## 讀取PDF　套件
## pip install pdfminer3k

from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams, LTFigure, LTImage
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed


class PDFReader:
    def __init__(self, read_pdf_path, pdf_file_name):
        self.read_pdf_path = read_pdf_path
        self.file_name = pdf_file_name
        self.content, self.img_list = self.__pdf_convent_to_text()
    '''
     輸入pdf 文件的路徑，可取得文件的純文字與圖片列表{list資料型態}
    '''
    def __pdf_convent_to_text(self):
        fp = open(os.path.join(self.read_pdf_path, self.file_name), 'rb')  # 以二進制模式打開
        #用文件對象創造一個pdf分析物件
        praser = PDFParser(fp)
        # 創建一個pdf文檔
        doc = PDFDocument()
        # 连接分析器 与文档对象
        praser.set_document(doc)
        doc.set_parser(praser)
        # 提供初始化密码
        # 如果没有密码 就创建一个空的字符串
        doc.initialize()
        ## content 為PDF純文字內容
        content = ""
        ## img_list 為存放圖片位置
        img_list = []

        # 检测文档是否提供txt转换，不提供就忽略
        if not doc.is_extractable:
            raise PDFTextExtractionNotAllowed
        else:
            # 创建PDf 资源管理器 来管理共享资源
            rsrcmgr = PDFResourceManager()
            # 创建一个PDF设备对象
            laparams = LAParams()
            device = PDFPageAggregator(rsrcmgr, laparams=laparams)
            # 创建一个PDF解释器对象
            interpreter = PDFPageInterpreter(rsrcmgr, device)

            # 循环遍历列表，每次处理一个page的内容
            for page in doc.get_pages(): # doc.get_pages() 获取page列表
                interpreter.process_page(page)
                # 接受该页面的LTPage对象
                layout = device.get_result()
                # 这里layout是一个LTPage对象 里面存放着 这个page解析出的各种对象 一般包括LTTextBox, LTFigure, LTImage, LTTextBoxHorizontal 等等 想要获取文本就获得对象的text属性，
                for line in layout:
                    ## 處理純文字部分，寫入txt
                    if (isinstance(line, LTTextBoxHorizontal)):
                        content = content + line.get_text().replace("北", "北") + '\n'

                    ## 處理圖片，輸出至graph 資料夾
                    if isinstance(line, LTFigure):
                        for im in line:
                            if isinstance(im, LTImage):
                                # Found one!
                                st = None
                                imdata = im.stream.get_data()
                                if not(b'\xbe\x00\x00\xbe\x00\x00' in imdata):
                                    img_list.append(imdata)
        return content, img_list


    '''
     輸入路徑，自動檢查是否存在，並自動產生該路徑
    '''

    def check_and_mdirs(self, path):
        if not(os.path.exists(path)):
            os.makedirs(path)

    '''
     輸入 純文字及存檔路徑，可以自動存成utf-8編碼之文字檔
    '''

    def save_txt_file(self, path):
        save_path = os.path.join(path, "%s" % self.file_name.replace(".pdf", ""), "txt")
        self.check_and_mdirs(save_path)
        with open(os.path.join(save_path, self.file_name.replace(".pdf", ".txt")), 'w', encoding="utf8") as writer:
            writer.write(self.content)
            #print("%s text content save in %s"%(self.file_name.replace(".pdf", ".txt"), save_path))
    '''
     輸入 圖片list及存檔路徑，自動存成jpg圖片檔
    '''
    def save_img_file(self, path):
        save_path = os.path.join(path, "%s" % self.file_name.replace(".pdf", ""), "graph")
        self.check_and_mdirs(save_path)
        graph_idx = 1
        for img in self.img_list:
            with open(os.path.join(save_path, "圖片%d.jpg"%graph_idx), 'wb') as img_writer:
                img_writer.write(img)
                #print("圖片%d.jpg save in %s"%(graph_idx, save_path))
            graph_idx+=1

