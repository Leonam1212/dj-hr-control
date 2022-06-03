from jinja2 import Environment, FileSystemLoader
from xhtml2pdf import pisa


def createPDF(data):
    loader = FileSystemLoader('createPdf/templates')
    env = Environment(loader=loader)
    template = env.get_template('workschedule.html')
    
    file = open('createPdf/output/index.html', 'w')
    render = template.render(data=data)
    file.write(render)

    convert_html_to_pdf(render, "createPdf/output/file.pdf")
    file.close()
    

def convert_html_to_pdf(source_html, output_filename):
    # open output file for writing (truncated binary)
    result_file = open(output_filename, "w+b")

    # convert HTML to PDF
    pisa_status = pisa.CreatePDF(
            source_html,                # the HTML to convert
            dest=result_file)           # file handle to recieve result

    # close output file
    result_file.close()                 # close output file

    # return False on success and True on errors
    return pisa_status.err

