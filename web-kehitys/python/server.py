import json
from flask import Flask ,Response

app = Flask (__name__)
@app.route("/sum")
def calculate_sum(number1 , number2 ):
    try:
        number1 = float(number1)
        number2 = float(number2)
        total_sum = number2 + number1

        response ={
            "number1" : number1,
            "number2" : number2,
            "total_sum" : total_sum
        }
        return response
    except ValueError:
        response= {
            "message " : "Invalid number as addednd" ,
            "status" : 400
        }

    json_response = json.dump(response)
    http_response = Response(response= json_response , status= 400 )
    return http_response

if __name__ == "main" :
    app.run(use_reloader = True , host = "127.0.0.1" , port=3000)