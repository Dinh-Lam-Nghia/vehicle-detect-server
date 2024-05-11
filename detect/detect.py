import os
from PIL import Image
import cv2
import torch
from flask import Flask,request,jsonify
import function.helper as helper
import function.utils_rotate as utils_rotate
from datetime import datetime
yolo_LP_detect = torch.hub.load('yolov5', 'custom', path='model/LP_detector.pt', force_reload=True, source='local')
yolo_license_plate = torch.hub.load('yolov5', 'custom', path='model/LP_ocr.pt', force_reload=True, source='local')
yolo_license_plate.conf = 0.60
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

from common import convert_to_dict
from db import *

def detect():
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
                            print(lp)
                            list_read_plates.add(lp.replace('-', ''))
                            cv2.putText(img, lp.replace('-', ''), (int(plate[0]), int(plate[1]-10)), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
                            flag = 1
                            break
                    if flag == 1:
                        break
        result = list(list_read_plates)
    return result

def detect_vehicle():
    target = os.path.join(APP_ROOT, 'images/')
    if not os.path.isdir(target):
        os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))

    if request.files:
        img = request.files["detect"]
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
                            list_read_plates.add(lp.replace('-', ''))
                            cv2.putText(img, lp.replace('-', ''), (int(plate[0]), int(plate[1]-10)), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
                            flag = 1
                            break
                    if flag == 1:
                        break
        result = list(list_read_plates)

    s = f'"'.join(list_read_plates)
    return get_vehicle_infor(s)


def get_vehicle_infor(vehicleID: str):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    sql = f"SELECT vehicle.* FROM vehicle INNER JOIN user ON vehicle.user_id = user.id WHERE vehicle.vehicle_id = '{vehicleID}' AND active = 0"
    cursor.execute(sql)
    result = cursor.fetchall() 
    result = convert_to_dict(cursor, result)
    cursor.close()
    # get_vehicle_staff(vehicleID)
    if(len(result) != 0):
        if(get_location(result[0]['vehicle_id'], 0) == 0):
            insert_to_log(result[0]['vehicle_id'], 0, 1)
        else:
            insert_to_log(result[0]['vehicle_id'], 0, 0)
        return result
    else:
        return get_vehicle_staff(vehicleID)


def get_location(vehicleID: str, role: int):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    sql = f"SELECT * FROM log WHERE role = {role} AND vehicle_id = '{vehicleID}' ORDER BY time DESC"
    cursor.execute(sql)
    result = cursor.fetchall() 
    result = convert_to_dict(cursor, result)
    cursor.close()
    if(len(result) != 0):
        return result[0]['status']
    else:
        return 0

def get_vehicle_staff(vehicleID: str):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    sql = f"SELECT * FROM vehicle_staff WHERE vehicle_id = '{vehicleID}'"
    cursor.execute(sql)
    result = cursor.fetchall() 
    result = convert_to_dict(cursor, result)
    cursor.close()
    if(len(result) != 0):
        if(get_location(result[0]['vehicle_id'], 1) == 0):
            insert_to_log(result[0]['vehicle_id'], 1, 1)
        else:
            insert_to_log(result[0]['vehicle_id'], 1, 0)
        return result
    else:
        return "fail"



def insert_to_log(vehicle_id: int, role: int, status: int):
    print(datetime.now())
    time = str(datetime.now())[0:19]
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    sql = "INSERT INTO log (status, vehicle_id, role, time) VALUES (%s, %s, %s, %s)"
    val = (status, vehicle_id, role, time)
    cursor.execute(sql, val)
    conn.commit()

