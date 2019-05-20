import os
import json
import hashlib
from werkzeug.utils import secure_filename

class ImgManifest():


    _CONFIG_PATH='CONFIG'
    _IMG_PATH='IMG'

    def __init__(self,idstr):

        self._id = idstr
        self._filename="{}/{}.json".format(self._CONFIG_PATH,self._id)

    def __str__(self):
        return str(self.read())


    def _checksum(self,data):
        chkString = ""

        for entry in data:
            chkString+=str(entry)

        return hashlib.md5(chkString).hexdigest()

    '''
    Reads the contents of the manifest file
    '''
    def read(self):

        data=None

        if self._manifest_exists(self._filename):
            try:
                with open(self._filename,'r') as manifest:
                    data = json.load(manifest)

            except EnvironmentError:
                pass

        return data


    '''
    Writes data to the specified file
    '''
    def write(self,data):

        filename = None

        try:
            with open(self._filename,'w') as manifest:
                json.dump(data,manifest)
            filename = self._filename
        except EnvrionmentError:
            pass

        return filename


    def add_img(self,img_filename):

        if not self._manifest_exists(self._filename):
            filename=self.create()

        manifest = self.read()

        img_path = "{}/{}".format(self._IMG_PATH,img_filename);

        if(manifest['data'].get(img_filename,False)):
            return self._filename

        if manifest != None and isinstance(img_filename,str):
            manifest['data'][img_filename]={"img_path":img_path}
            manifest['checksum']=self._checksum(manifest)

        return self.write(manifest)


    '''
    Attempts to create a new manifest file for a given ID, if that ID has not already been provisioned
    Returns manifest_filename on success, and None on any writing failure
    '''
    def create(self):

        manifest_filename = None
        manifest_skeleton = {'data':{},'checksum':'0'}

        if not self._manifest_exists(self._filename):
            self.write(manifest_skeleton)
            manifest_filename = self._filename

        return manifest_filename



    def _manifest_exists(self,filename):

        return os.path.isfile(filename)



class DataHandler():


    UPLOAD_FOLDER = 'IMG'
    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

    def __init__(self,idnum=None):

        self.id = idnum


    def _allowed_extension(self, filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


    def write_image_file(self, file_data, filename):

        if file_data and allowed_file(file_data.filename):
            filename = secure_filename(file_data.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))

        return filename



    def __str__(self):

        return str(self.id)



def test_func():

    imgm = ImgManifest("frame1")
    print(imgm.create())
    print(imgm.add_img("newPhoto1.png"))

    imgm2 = ImgManifest("framex2")
    print(imgm2.add_img("newPhoto1.png"))



if __name__ == "__main__":

    test_func()
