from flask import Flask , request, send_file
from DataHandler import DataHandler, ImgManifest
import json

app = Flask(__name__)

ABOUT_INFO="info.json"



'''
FamFrame Info Page
'''
@app.route('/frame',methods=['GET'])
def get_info():
   
        return "FamFrame v0.1"



@app.route('/frame/healthcheck', methods=['GET'])
def healthcheck():
        return "GOOD"




@app.route('/frame/<frame_id>',methods=['GET'])
def get_manifest(frame_id):

    manifest = ImgManifest(frame_id)

    if not manifest._manifest_exists(manifest._filename):
        return "Not Found", 404

    return json.dumps(manifest._get_client_manifest())


@app.route('/frame/<frame_id>',methods=['POST'])
def create_manifest(frame_id):

    manifest = ImgManifest(frame_id)
    manifest_status = None

    if not manifest._manifest_exists(manifest._filename):
        manifest_status = manifest.create()

        if manifest_status is None:
           return "Error: Issue creating frame manifest file", 500


    return json.dumps(manifest._get_client_manifest()), 200



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



@app.route('/frame/<frame_id>/img/<filename>', methods=['GET'])
def download(frame_id,filename):

    if filename == '':
        return "No filename provided", 412

    manifest = ImgManifest(frame_id)
    dh = DataHandler(frame_id)

    if not manifest._manifest_exists(manifest._filename):
        return "Not Found", 404

    files = manifest.read()

    if filename not in files['data']:
        return "Not Found", 404

    data = dh.read_image_file(filename)
    mimetype_ext = dh._get_extension(filename)

    return send_file(data,mimetype="image/{}".format(mimetype_ext),as_attachment=False)





if __name__=="__main__":
        app.run(host='0.0.0.0', port=1225 ,debug=True)
