from fpdf import FPDF

def main():
    name = input("Name: ")
    pdf = FPDF(orientation="portrait", format="A4")
    pdf.add_page()
    pdf.set_font("helvetica", style="B", size=40)
    pdf.cell(0, 60, "CS50 Shirtificate", align="C")
    pdf.image("shirtificate.png", x="C", y=60, w=pdf.epw)
    pdf.set_font("helvetica", style="B", size=25)
    pdf.set_text_color(255, 255, 255)
    pdf.text(x=(pdf.epw - pdf.get_string_width(name)) / 2 + pdf.l_margin, y=140, text=name)
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
