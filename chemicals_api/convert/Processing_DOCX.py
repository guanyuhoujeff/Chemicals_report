import docx
import os


class DOCXReader:
    def __init__(self, read_docx_path, docx_file_name):
        self.read_docx_path = read_docx_path
        self.file_name = docx_file_name
        self.content = self.__docx_convent_to_text()

    def __docx_convent_to_text(self):
        doc = docx.Document(os.path.join(self.read_docx_path, self.file_name))
        content = ""
        for para in doc.paragraphs :
            content = content + para.text
        return content

    '''
     輸入路徑，自動檢查是否存在，並自動產生該路徑
    '''

    def __check_and_mdirs(self, path):
        if not(os.path.exists(path)):
            os.makedirs(path)

    '''
     輸入 純文字及存檔路徑，可以自動存成utf-8編碼之文字檔
    '''

    def save_txt_file(self, path):
        save_path = os.path.join(path, "%s" % self.file_name.replace(".docx", ""), "txt")
        self.__check_and_mdirs(save_path)
        with open(os.path.join(save_path, self.file_name.replace(".docx", ".txt")), 'w', encoding="utf8") as writer:
            writer.write(self.content)

