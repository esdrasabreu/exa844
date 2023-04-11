import functions_framework
import pymysql

import json
import time

@functions_framework.http
def hello_http(request):    
    request_json = request.get_json(silent=True)
    request_args = request.args

    map = {}
    if request_json and 'action' in request_json and request_json['action']=="put":
        try:     
            conn = pymysql.connect(   
                host="ip do servidor MySQL",
                port = 3306,
                user="root",
                password="senha",
                db="Blog",
                cursorclass=pymysql.cursors.DictCursor
            )

            with conn:
                with conn.cursor() as cursor:
                    message = request_json['message']
                    autor = request_json['autor']
                    date = time.strftime('%Y-%m-%d %H:%M:%S')                    
                    cursor.execute("insert into Messages (message,autor,date) values ('{}','{}','{}');".format(message, autor, date))
                    conn.commit()
                    map["message"] = "put executed successfully"     
        except Exception as e:
            map["message"] = 'Error: {}'.format(str(e))            
    elif request_args and 'action' in request_args and request_args['action'] == "get":
        try:
            conn = pymysql.connect(   
                host="ip do servidor MySQL",
                port=3306,
                user="root",
                password="senha",
                db="Blog",
                cursorclass=pymysql.cursors.DictCursor
            )
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute("select * from Messages order by date desc")
                    results = cursor.fetchall()
                    messages = []
                    for row in results:
                        message = {
                            'message': row['message'],
                            'autor': row['autor'],
                            'date': row['date'].strftime('%Y-%m-%d %H:%M:%S')
                        }
                        messages.append(message)
                    map["messages"] = messages
                    map["message"] = "get executed successfully"
        except Exception as e:
            map["message"] = 'Error: {}'.format(str(e))

    else:
        map["message"] = "action missing or with wrong value!"
    
    return json.dumps(map)