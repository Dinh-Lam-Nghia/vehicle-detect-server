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
    conn = http.client.HTTPSConnection("dkg5x1.api.infobip.com")
    payload = json.dumps({
    "messages": [
        {
            "destinations": [{"to":"84346056590"}],
            "from": "ServiceSMS",
            "text": content
        }
        ]
    })
    headers = {
        'Authorization': 'App 048f8a75bb7036d142afd7687ad4e1fd-f5525043-033b-4384-9736-d9b11a51a378',
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    conn.request("POST", "/sms/2/text/advanced", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))