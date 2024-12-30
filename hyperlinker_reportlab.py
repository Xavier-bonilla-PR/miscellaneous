from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.lib.enums import TA_JUSTIFY

# Create a canvas object
c = canvas.Canvas("h2s_signaling.pdf", pagesize=letter)

def create_first_page(c):
    c.setTitle("H2S as a Signaling Molecule")
    c.bookmarkPage("main_page")  # Create a named destination for the main page
    
    # Define a style for the text
    style = ParagraphStyle(
        'Normal',
        fontSize=10,
        leading=12,
        alignment=TA_JUSTIFY
    )
    
    # The main text
    text = """
    <b>I. Introduction</b><br/>
    <b>A. Overview of hydrogen sulfide (H2S) as a signaling molecule (ref42, ref83, ref106, ref108)</b><br/>
    <b>1. Physiological roles and therapeutic potential (ref106, ref108)</b><br/>
    - H2S is an endogenous signaling molecule involved in various <font color="blue"><u>physiological processes</u></font>.<br/>
    - Functions include vasodilation, neurotransmission, and cytoprotection.<br/>
    - Modulates oxidative stress and inflammation, making it relevant in cardiovascular diseases and <font color="blue"><u>neurodegenerative disorders</u></font>.<br/>
    - Potential therapeutic applications in conditions like hypertension, diabetes, and neurodegeneration.<br/>
    <b>2. Challenges and limitations of H2S therapy (ref108, ref115)</b>
    """
    
    # Create a Paragraph object
    p = Paragraph(text, style)
    
    # Draw the paragraph
    p.wrapOn(c, 400, 600)
    p.drawOn(c, 100, 500)
    
    # Create hyperlink annotations
    c.linkRect("", "reveal_processes", (100, 500, 500, 700), thickness=0)
    c.linkRect("", "reveal_disorders", (100, 500, 500, 700), thickness=0)
    
    c.showPage()

def create_second_page(c):
    c.setTitle("Additional Information - Physiological Processes")
    c.bookmarkPage("reveal_processes")  # Create a named destination
    c.drawString(100, 750, "Physiological processes involving H2S:")
    c.drawString(100, 730, "Involves heart, brain, and liver mostly")
    
    # Add "Back to Main Page" link
    c.setFillColor(colors.blue)
    c.drawString(100, 100, "Back to Main Page")
    c.linkRect("Back to Main Page", "main_page", (100, 100, 200, 115), thickness=0)
    
    c.showPage()

def create_third_page(c):
    c.setTitle("Additional Information - Neurodegenerative Disorders")
    c.bookmarkPage("reveal_disorders")  # Create a named destination
    c.drawString(100, 750, "Neurodegenerative disorders related to H2S:")
    c.drawString(100, 730, "Includes Alzheimer's disease, Parkinson's,")
    c.drawString(100, 710, "Huntington's disease, and ALS")
    
    # Add "Back to Main Page" link
    c.setFillColor(colors.blue)
    c.drawString(100, 100, "Back to Main Page")
    c.linkRect("Back to Main Page", "main_page", (100, 100, 200, 115), thickness=0)
    
    c.showPage()

# Create the pages
create_first_page(c)
create_second_page(c)
create_third_page(c)

# Save the PDF
c.save()

# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
# from reportlab.lib import colors
# from reportlab.lib.styles import ParagraphStyle
# from reportlab.platypus import Paragraph
# from reportlab.lib.enums import TA_JUSTIFY

# # Create a canvas object
# c = canvas.Canvas("exampleII.pdf", pagesize=letter)

# def create_first_page(c):
#     c.setTitle("H2S as a Signaling Molecule")
    
#     # Define a style for the text
#     style = ParagraphStyle(
#         'Normal',
#         fontSize=10,
#         leading=12,
#         alignment=TA_JUSTIFY
#     )
    
#     # The main text
#     text = """
#     <b>I. Introduction</b><br/>
#     <b>A. Overview of hydrogen sulfide (H2S) as a signaling molecule (ref42, ref83, ref106, ref108)</b><br/>
#     <b>1. Physiological roles and therapeutic potential (ref106, ref108)</b><br/>
#     - H2S is an endogenous signaling molecule involved in various <font color="blue"><u>physiological processes</u></font>.<br/>
#     - Functions include vasodilation, neurotransmission, and cytoprotection.<br/>
#     - Modulates oxidative stress and inflammation, making it relevant in cardiovascular diseases and neurodegenerative disorders.<br/>
#     - Potential therapeutic applications in conditions like hypertension, diabetes, and neurodegeneration.<br/>
#     <b>2. Challenges and limitations of H2S therapy (ref108, ref115)</b>
#     """
    
#     # Create a Paragraph object
#     p = Paragraph(text, style)
    
#     # Draw the paragraph
#     p.wrapOn(c, 400, 600)
#     p.drawOn(c, 100, 500)
    
#     # Create a hyperlink annotation
#     c.linkRect("", "reveal_info", (100, 500, 500, 700), thickness=0)
    
#     c.showPage()

# def create_second_page(c):
#     c.setTitle("Additional Information")
#     c.bookmarkPage("reveal_info")  # Create a named destination
#     c.drawString(100, 750, "Physiological processes involving H2S:")
#     c.drawString(100, 730, "Involves heart, brain, and liver mostly")
#     c.showPage()

# # Create the pages
# create_first_page(c)
# create_second_page(c)

# # Save the PDF
# c.save()


# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
# from reportlab.lib.colors import blue

# # Create a canvas object
# c = canvas.Canvas("exampleinteractive.pdf", pagesize=letter)

# # Function to create the first page with a hyperlink
# def create_first_page(c):
#     c.setTitle("Interactive PDF Example")
#     c.drawString(100, 750, "Welcome to the interactive PDF example!")
#     c.drawString(100, 730, "Click the link below to see the hidden text:")
    
#     # Draw hyperlink
#     c.setFillColor(blue)
#     c.drawString(100, 710, "Click here to reveal the text")
    
#     # Create a hyperlink annotation pointing to a named destination 'reveal_text'
#     c.linkRect("Click here to reveal the text", "reveal_text")
    
#     c.showPage()

# # Function to create the second page with the hidden text
# def create_second_page(c):
#     c.setTitle("Revealed Text Page")
#     c.bookmarkPage("reveal_text")  # Create a named destination
#     c.drawString(100, 750, "Here is the hidden text:")
#     c.drawString(100, 730, "This is the text that was hidden. You revealed it by clicking the link.")
#     c.showPage()

# # Create the pages
# create_first_page(c)
# create_second_page(c)

# # Save the PDF
# c.save()


