import os
import zipfile

from django.http import HttpResponse


def getPdf(self):
    file_path = f'candidates_files/{self.get_object().pdf_file}'
    if os.path.exists(file_path):
        with open(file_path, 'rb') as folder:
            response = HttpResponse(folder.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path) #attachment para download
            return response
    raise FileNotFoundError

def getAllPdfs():
    try:
        if len(os.listdir('candidates_files')) == 0:
            raise FileNotFoundError
            
        archive_zip = zipfile.ZipFile('candidates_files/candidates_cvs.zip', 'w')    
        for folder, _, files in os.walk('candidates_files'):
            for file in files:
                if file.endswith('.pdf'):
                    archive_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), 'candidates_files'), compress_type = zipfile.ZIP_DEFLATED)
        archive_zip.close()

        file_path = f'candidates_files/candidates_cvs.zip'
        if os.path.exists(file_path):
            with open(file_path, 'rb') as folder:
                response = HttpResponse(folder.read(), content_type="application/zip")
                response['Content-Disposition'] = 'attachment; filename=candidates_cvs.zip' #attachment para download
                return response
    except:
        raise FileNotFoundError