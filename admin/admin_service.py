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
    conn = http.client.HTTPSConnection("e1xxpn.api.infobip.com")
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
        'Authorization': 'App b49263e7c0054c1d5a6e93fe951c61fd-29312641-ca94-4a92-8ea6-2c1b3bf8e23e',
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    conn.request("POST", "/sms/2/text/advanced", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))