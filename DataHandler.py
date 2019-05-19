import os
import json


class ImgManifest():


    CONFIG_PATH='config/'

    def __init__(self,idstr):

        self.id = idstr


    def manifest_exists(self):

        filename=CONFIG_PATH+self.id
        return os.path.isfile(filename)



class DataHandler():

    def __init__(self,idnum=None):

        self.id = idnum


    def __str__(self):

        return str(self.id)



def test_func():

    print("test")


if __name__ == "__main__":
    test_func()
