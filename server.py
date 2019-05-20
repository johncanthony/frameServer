from flask import Flask , request
from DataHandler import DataHandler, ImgManifest

app = Flask(__name__)

ABOUT_INFO="info.json"



'''
FamFrame Info Page
'''
@app.route('/frame',methods=['GET'])
def get_dish():
        a = DataHandler("1234")
        print(a)
        return "FamFrame v0.1"


@app.route('/frame/healthcheck', methods=['GET'])
def healthcheck():
        return "GOOD"


@app.route('/frame/<frame_id>',methods=['GET'])
def get_manifest(frame_id):

    manifest = ImgManifest(frame_id)

    if not manifest._manifest_exists():
        return "Not Found", 404


@app.route('/frame/<frame_id>/img/', methods=['POST'])
def upload(frame_id):

    dh = DataHandler(frame_id)
    manifest = ImgManifest(frame_id)

    if 'file_data' not in request.files:
        return "No File Provided", 412

    file_data = request.files['file_data']
    if file_data.filename == '':
        return "Filename not valid", 403


    manifest_filename = dh.write_image_file(file_data,file_data.filename)

    if(manifest_filename == None):
        return "Error saving file", 500

    manifest_filename = manifest.add_img(manifest_filename)

    if(manifest_filename == None):
        return "Error updating frame manifest", 500

    return manifest_filename, 200


if __name__=="__main__":
        app.run(host='0.0.0.0', port=1225 ,debug=True)
