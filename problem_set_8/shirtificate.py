from fpdf import FPDF

name = input("Name: ")

pdf = FPDF("P", "mm", "A4")
pdf.add_page()

pdf.set_font("Helvetica", "B", 32)
pdf.cell(0, 40, "CS50 Shirtificate", align="C", ln=True)

pdf.image("shirtificate.png", x=10, w=190)

pdf.set_font("Helvetica", "B", 24)
pdf.set_text_color(255, 255, 255)
pdf.set_xy(0, 140)
pdf.cell(0, 10, name, align="C")

pdf.output("shirtificate.pdf")
