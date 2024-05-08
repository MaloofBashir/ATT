import PyPDF2

def get_subname_rollno(pdf_obj,page_no):
        page1=pdf_obj.pages[page_no].extract_text() 

        if page1:
            lines=page1.split('\n')

            for pageno,line in enumerate(lines):
                rollno=0
                subjects=""
                if pageno==14 or pageno==19:
                    if pageno==14:
                         rollno=line.split(".")[1]
                         print(f"roll no:{rollno}")
                    if pageno==19:
                         subjects=line.split(" ")[0]
                         subjects=subjects.split("-")
                         print(f"subjects:{subjects}")

                    # print(f"roll no {rollno} and subjects are:{subjects}")

with open('ATT.pdf','rb') as pdffile:
    pdf_obj=PyPDF2.PdfReader(pdffile)
    num_pages=len(pdf_obj.pages)
    for i in range(num_pages):
        get_subname_rollno(pdf_obj,page_no=i)