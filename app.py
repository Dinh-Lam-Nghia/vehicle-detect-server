from flask import Flask,request,jsonify

from PIL import Image
import cv2
import torch
import function.utils_rotate as utils_rotatecle
from IPython.display import display
import os
import function.helper as helper
from user.user_service import add_user, check_user_exist
from vehicle.vehicle_service import get_vehicle_infor, add_vehicle_infor


app=Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

yolo_LP_detect = torch.hub.load('yolov5', 'custom', path='model/LP_detector.pt', force_reload=True, source='local')
yolo_license_plate = torch.hub.load('yolov5', 'custom', path='model/LP_ocr.pt', force_reload=True, source='local')
yolo_license_plate.conf = 0.60

@app.route('/')
def welcome():
    return jsonify(welcome = 'wfd');

@app.route('/login_user',methods=['POST'])
def check_login_user():
    email = request.form['email']
    name = request.form['name']
    urlPhoto = request.form['urlPhoto']
    isCheck = check_user_exist(email)
    if(isCheck == False):
        add_user(email, name, urlPhoto)
    return jsonify(isCheck)

@app.route('/vehicle_infor',methods=['POST'])
def check_vehicle_infor():
    email = request.form['email']
    return jsonify(get_vehicle_infor(email));

@app.route('/add_vehicle',methods=['POST'])
def add_vehicle():
    vehicle_id = request.form['vehicle_id']
    role = request.form['role']
    vehicle_model = request.form['vehicle_model']
    vehicle_color = request.form['vehicle_color']
    vehicle_type = request.form['vehicle_type']
    user_id = request.form['user_id']
    add_vehicle_infor(vehicle_id, role, vehicle_model, vehicle_color, vehicle_type, user_id)
    return jsonify(get_vehicle_infor(user_id));

@app.route("/upload",methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    if not os.path.isdir(target):
        os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))

    if request.files:
        img = request.files["upload"]
        filename = img.filename

        destination = "/".join([target, filename])
        img.save(destination)
        img = cv2.imread(destination);
        os.remove(destination);

        plates = yolo_LP_detect(img, size=640)
        list_plates = plates.pandas().xyxy[0].values.tolist()
        list_read_plates = set()
        if len(list_plates) == 0:
            lp = helper.read_plate(yolo_license_plate,img)
            if lp != "unknown":
                cv2.putText(img, lp, (7, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
                list_read_plates.add(lp)
        else:
            for plate in list_plates:
                flag = 0
                x = int(plate[0]) # xmin
                y = int(plate[1]) # ymin
                w = int(plate[2] - plate[0]) # xmax - xmin
                h = int(plate[3] - plate[1]) # ymax - ymin  
                crop_img = img[y:y+h, x:x+w]
                cv2.rectangle(img, (int(plate[0]),int(plate[1])), (int(plate[2]),int(plate[3])), color = (0,0,225), thickness = 2)
                cv2.imwrite("crop.jpg", crop_img)
                rc_image = cv2.imread("crop.jpg")
                lp = ""
                for cc in range(0,2):
                    for ct in range(0,2):
                        lp = helper.read_plate(yolo_license_plate, utils_rotate.deskew(crop_img, cc, ct))
                        if lp != "unknown":
                            list_read_plates.add(lp)
                            cv2.putText(img, lp, (int(plate[0]), int(plate[1]-10)), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
                            flag = 1
                            break
                    if flag == 1:
                        break
        result = list(list_read_plates)
        return jsonify(number_plate = str(list_read_plates));

if __name__=='__main__':
    app.run()