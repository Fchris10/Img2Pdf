import os
from PIL import Image
#from fpdf import FPDF
from pathlib import Path

def img_to_pdf(path_image):
    
    try:
        img = Image.open(f"{path_image}")
        download = Path(Path.home(), "Desktop")
        pdf_path = os.path.join(download, "Output_Img.pdf") # Save the pdf file in Desktop
        img.save(pdf_path, "PDF")
        return True
    except:
        return False


# Alternative way to convert Image file to Pdf file with more details

#def img_to_pdf_m2():

#    pdf = FPDF()
#    pdf.add_page('P', 'A4')
#    pdf.image("key.jpg")
#    pdf.output("save.pdf")


    ## If i want a list of images: ##

    #for image in imagelist:
    #   pdf.add_page()
    #   pdf.image(image,x,y,w,h)
    #pdf.output("save_images.pdf")