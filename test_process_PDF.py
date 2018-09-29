from chemicals_api.convert import Processing_PDF

## 輸入PDF檔案存在的資料夾路徑以及要讀取的檔案名稱
PDF_path = "./test_file/test_pdf/3槽車事故及倉儲意外事故案例"
pdf_file = '3-1高雄縣路竹鄉苯乙烯槽車翻覆事故(槽車類型).pdf'

## 處理PDF檔的類別物件
pdf_opject = Processing_PDF.PDFReader(
        read_pdf_path = PDF_path, 
        pdf_file_name = pdf_file )

## 可以將讀取到的文字以及圖片存在本地端
Output_path = "./test_file/Output/"
pdf_opject.save_txt_file(Output_path)
pdf_opject.save_img_file(Output_path)
print(pdf_opject.content)

