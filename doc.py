import PyPDF2

def print_info_per_page(pdf_obj,page_no):
        page1=pdf_obj.pages[3].extract_text() 

        if page1:
            lines=page1.split('\n')

            for pageno,line in enumerate(lines):
                if pageno==14 or pageno==19:
                    print(f"page no: {pageno}: {line}")

with open('ATT.pdf','rb') as pdffile:
    pdf_obj=PyPDF2.PdfReader(pdffile)
    num_pages=len(pdf_obj.pages)
    print(num_pages)
    print_info_per_page(pdf_obj,page_no)