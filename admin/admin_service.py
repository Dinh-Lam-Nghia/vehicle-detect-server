from db import *
from common import convert_to_dict
import http.client
import json

def login(email: str, password: str):
    print(email)
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    sql = f"SELECT * FROM admin WHERE email = '{email}' AND password = '{password}'"
    cursor.execute(sql)
    result = cursor.fetchall() 
    result = convert_to_dict(cursor, result)
    cursor.close()
    return result 



def send_sms(phone: str, content: str):
    conn = http.client.HTTPSConnection("z32nnw.api.infobip.com")
    payload = json.dumps({
    "messages": [
        {
            "destinations": [{"to":phone}],
            "from": "ServiceSMS",
            "text": content
        }
        ]
    })
    headers = {
        'Authorization': 'App 56600f52c33a1eec99d9caf7d04b2980-2eafbbb8-8368-431d-9552-22a31a60df7f',
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    conn.request("POST", "/sms/2/text/advanced", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))