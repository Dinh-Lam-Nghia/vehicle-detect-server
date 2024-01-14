from flask import Flask,request,jsonify

from PIL import Image
import cv2
import torch
import function.utils_rotate as utils_rotate
from IPython.display import display
import os
import function.helper as helper
from user.user_service import add_user, check_user_exist
from vehicle.vehicle_service import get_vehicle_infor, add_vehicle_infor, remove_active, update_vehicle_infor, get_all_vehicles
from admin.admin_service import login, send_sms
from admin.logs_service import get_logs, get_log_table, get_all_vehicle_admin, get_request, accpect_request, remove_request
from vehicle_staff.vehicle_staff_service import add_vehicle_staff, get_vehicle_staff, remove_staff, update_staffs
import hashlib
from flask_cors import CORS

from detect.detect import detect, detect_vehicle