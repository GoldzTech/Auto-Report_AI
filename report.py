from fpdf import FPDF

def generate_report(total, average, highest, summary):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(0, 10, "Automated Sales Report", ln=True, align="C")

    pdf.ln(10)
    pdf.set_font("Helvetica", size=12)
    pdf.cell(0, 8, f"Total Sales: ${total:.2f}", ln=True)
    pdf.cell(0, 8, f"Avarage Sales: {average:.2f}", ln=True)
    pdf.cell(0,8, f"Highest Sale: ${highest:.2f}", ln=True)

    pdf.ln(10)
    pdf.set_font("Helvetica", "B", 14)
    pdf.cell(0, 8, "AI-generated Summary:", ln=True)

    pdf.set_font("Helvetica", size=12)
    pdf.multi_cell(0, 8, summary)

    pdf.output("report.pdf")