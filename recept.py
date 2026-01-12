from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

# New dummy data for a bookstore invoice
DATA = [
    ["Order Date", "Book Title", "Quantity", "Unit Price ($)", "Total ($)"],
    [
        "2024-03-15",
        "The Python Programming Language (4th Edition)",
        "2",
        "45.99",
        "91.98",
    ],
    [
        "2024-03-15",
        "Data Science Handbook",
        "1",
        "68.50",
        "68.50",
    ],
    [
        "2024-03-15",
        "Web Development with Django",
        "3",
        "32.75",
        "98.25",
    ],
    [
        "2024-03-15",
        "Machine Learning Fundamentals",
        "1",
        "54.20",
        "54.20",
    ],
    ["", "", "", "Subtotal:", "312.93"],
    ["", "", "", "Tax (8%):", "25.03"],
    ["", "", "", "Shipping:", "5.99"],
    ["", "", "", "Total:", "343.95"],
]

# creating a Base Document Template of page size A4
pdf = SimpleDocTemplate("bookstore_invoice.pdf", pagesize=A4)

# standard stylesheet defined within reportlab itself
styles = getSampleStyleSheet()

# fetching the style of Top level heading (Heading1)
title_style = styles["Heading1"]

# 0: left, 1: center, 2: right
title_style.alignment = 1

# creating the paragraph with 
# the heading text and passing the styles of it
title = Paragraph("TechBooks Pro - Invoice", title_style)

# Create a subtitle
subtitle_style = styles["Heading2"]
subtitle_style.alignment = 1
subtitle = Paragraph("Order #TB-2024-0783", subtitle_style)

# creates a Table Style object and in it,
# defines the styles row wise
style = TableStyle(
    [
        ("BOX", (0, 0), (-1, -1), 1, colors.black),
        ("GRID", (0, 0), (-1, -4), 1, colors.black),  # Changed grid range
        ("BACKGROUND", (0, 0), (4, 0), colors.darkblue),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (0, 0), (3, -1), "LEFT"),  # Align first 4 columns left
        ("ALIGN", (4, 0), (4, -1), "RIGHT"),  # Align price column right
        ("BACKGROUND", (0, 1), (-1, -5), colors.beige),  # Adjusted background range
        ("BACKGROUND", (3, -4), (4, -1), colors.lightgrey),  # Summary section background
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 12),
        ("FONTNAME", (3, -4), (4, -1), "Helvetica-Bold"),  # Bold summary section
        ("ROWBACKGROUNDS", (0, 1), (-1, -5), [colors.white, colors.lightcyan]),  # Alternate row colors
    ]
)

# creates a table object and passes the style to it
table = Table(DATA, style=style)

# Add customer information
customer_style = styles["Normal"]
customer_info = [
    Paragraph("<b>Bill To:</b>", customer_style),
    Paragraph("John Smith", customer_style),
    Paragraph("123 Main Street", customer_style),
    Paragraph("San Francisco, CA 94105", customer_style),
    Paragraph("Email: john.smith@email.com", customer_style),
]

# Build the PDF with all elements
pdf.build([title, subtitle] + customer_info + [table])