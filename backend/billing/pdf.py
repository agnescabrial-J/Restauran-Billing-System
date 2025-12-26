from reportlab.pdfgen import canvas

def generate_bill_pdf(bill):
    file_name = f"bill_table_{bill.table.id}.pdf"
    c = canvas.Canvas(file_name)
    c.drawString(100, 750, f"Bill for Table {bill.table.table_number}")
    c.drawString(100, 700, f"Total Amount: {bill.total}")
    c.save()
    return file_name