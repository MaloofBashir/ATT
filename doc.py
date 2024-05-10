import PyPDF2
import openpyxl

rollno=""
subjects=""
all_roll_nos=[]
def get_roll_no(pdf_obj,page_no):
      page1=pdf_obj.pages[page_no].extract_text()
      if page1:
            lines=page1.split('\n')

            for lineno, line in enumerate(lines):
                  if lineno==14:
                        rollno=line.split(".")[1]
                        return rollno
def get_subname(pdf_obj,page_no):
        page1=pdf_obj.pages[page_no].extract_text() 

        if page1:
            lines=page1.split('\n')

            for lineno,line in enumerate(lines):
                        
                if lineno==19:
                        subjects=line.split(" ")[0]
                        subjects=subjects.split("-")
                        return subjects

wb=openpyxl.Workbook()
ws=wb.active

with open('ZP.pdf','rb') as pdffile:
    pdf_obj=PyPDF2.PdfReader(pdffile)
    num_pages=len(pdf_obj.pages)
    sub_to_search="IESD620"
    ws.append([sub_to_search])
    for pageno in range(num_pages):
          subs_of_current_candidate=get_subname(pdf_obj,pageno)
          if sub_to_search in subs_of_current_candidate:
                cur_roll_no=get_roll_no(pdf_obj,pageno)
                ws.append([cur_roll_no])
                all_roll_nos.append(cur_roll_no)
                print(cur_roll_no)
excel_filename="myfile.xlsx"
wb.save(excel_filename)

print(f"total no of candidaates {len(all_roll_nos)}")
