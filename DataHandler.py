import os
import json


class ImgManifest():


    _CONFIG_PATH='CONFIG'

    def __init__(self,idstr):

        self._id = idstr


    '''
    Attempts to create a new manifest file for a given ID, if that ID has not already been provisioned
    Returns manifest_filename on success, and None on any writing failure
    '''
    def create(self):


        manifest_filename = "{}/{}.json".format(self._CONFIG_PATH,self._id)
        manifest_skeleton = {'data':[],'checksum':'0'}

        if not self._manifest_exists(manifest_filename):
            try:
                with open(manifest_filename,"w") as manifestFile:
                    json.dump(str(manifest_skeleton),manifestFile)

            except EnvironmentError:
                manifest_filename = None

        return manifest_filename


    def _manifest_exists(self,filename):

        return os.path.isfile(filename)



class DataHandler():

    def __init__(self,idnum=None):

        self.id = idnum


    def __str__(self):

        return str(self.id)



def test_func():

    print("test")


if __name__ == "__main__":
    imgm = ImgManifest("i001234")
    print(imgm.create())
