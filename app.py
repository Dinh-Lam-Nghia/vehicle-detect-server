from lib import *
from user.user_service import get_onlyOne_user

app=Flask(__name__)
CORS(app)


yolo_LP_detect = torch.hub.load('yolov5', 'custom', path='model/LP_detector.pt', force_reload=True, source='local')
yolo_license_plate = torch.hub.load('yolov5', 'custom', path='model/LP_ocr.pt', force_reload=True, source='local')
yolo_license_plate.conf = 0.60

@app.route('/login_user',methods=['POST'])
def check_login_user():
    email = request.form['email']
    name = request.form['name']
    urlPhoto = request.form['urlPhoto']
    isCheck = check_user_exist(email)
    if(isCheck == False):
        add_user(email, name, urlPhoto)
    return jsonify(isCheck)

@app.route('/get_onlyOne_user',methods=['POST'])
def check_onlyOne_user():
    email = request.form['email']
    return jsonify(get_onlyOne_user(email))

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
    expires = request.form['expires']
    phone = request.form['phone']
    add_vehicle_infor(vehicle_id, role, vehicle_model, vehicle_color, vehicle_type, user_id, expires, phone)
    return jsonify(get_vehicle_infor(user_id));

@app.route('/remove_active_vehicle',methods=['POST'])
def remove_active_vehicle():
    vehicle_id = request.form['vehicle_id']
    remove_active(vehicle_id)
    return jsonify(message = 'Deleted vehicle!');

@app.route('/update_vehicle',methods=['POST'])
def update_vehicle():
    vehicle_id = request.form['vehicle_id']
    role = request.form['role']
    vehicle_color = request.form['vehicle_color']
    expires = request.form['expires']
    phone = request.form['phone']
    update_vehicle_infor(vehicle_id, role, vehicle_color, expires, phone)
    return jsonify(message = 'Updated vehicle!');


@app.route('/login', methods=['POST'])
def login_admin():
    email = request.form['email']
    password = request.form['password']
    hashed_password = hashlib.md5(password.encode()).hexdigest()
    if(len(login(email, hashed_password)) != 0):
        return jsonify(message = 'Login successful');
    else:
        return jsonify(message = 'Login failed'); 

@app.route('/get_all_vehicle', methods=['POST'])
def get_all_vehicle():
    return jsonify(get_all_vehicles());

@app.route('/get_logs', methods=['POST'])
def get_log():
    return jsonify(get_logs());

@app.route('/add_staff', methods=['POST'])
def add_staff():
    phone = request.form['phone']
    plate_number = request.form['plate_number']
    expires = request.form['expires']
    role = request.form['role']
    name = request.form['name']
    model = request.form['model']
    add_vehicle_staff(name, phone, model, plate_number, role, expires)
    return jsonify(message = 'Success'); 

@app.route('/get_staff', methods=['POST'])
def get_staff():
    return jsonify(get_vehicle_staff()); 

@app.route('/remove_staff', methods=['POST'])
def remove_active_staff():
    id_staff = request.form['id']
    remove_staff(id_staff)
    return jsonify(message = 'Deleted vehicle!');

@app.route('/update_staff', methods=['POST'])
def update_staff():
    id_staff = request.form['id']
    phone = request.form['phone']
    plate_number = request.form['plate_number']
    expires = request.form['expires']
    role = request.form['role']
    name = request.form['name']
    model = request.form['model']
    update_staffs(id_staff, name, phone, model, plate_number, role, expires)
    return jsonify(message = 'Update success!');

@app.route('/get_logs_table', methods=['POST'])
def get_log_tables():
    role = request.form['role']
    return jsonify(get_log_table(role));

@app.route('/get_all_vehicle_admin', methods=['POST'])
def get_all_vehicles_admin():
    role = request.form['role']
    return jsonify(get_all_vehicle_admin(role));

@app.route('/send_sms', methods=['POST'])
def sent_sms():
    phone = request.form['phone']
    content = request.form['content']
    send_sms(phone, content)
    return jsonify(message = 'Sent!');

@app.route("/upload",methods=['POST'])
def upload():
    return jsonify(number_plate = detect()[0]);

@app.route("/detect_vehicle",methods=['POST'])
def detects():
    return jsonify(detect_vehicle());
   

@app.route("/get_request",methods=['POST'])
def get_requests():
    return jsonify(get_request());


@app.route("/accpect_request",methods=['POST'])
def accpect_requests():
    id = request.form['id']
    return jsonify(accpect_request(id));

@app.route("/remove_request",methods=['POST'])
def remove_requests():
    id = request.form['id']
    return jsonify(remove_request(id));

if __name__=='__main__':
    app.run(host='192.168.1.6', port=5000, debug=True, threaded=False)
