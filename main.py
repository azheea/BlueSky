from flask import Flask, render_template,request
import json
import re
import os


app = Flask(__name__, static_url_path='/')


#account
@app.route("/account/<route2>", methods=['POST', "GET"])
def idk(route2):
    if request.method == "POST":
        if request.content_type.startswith('application/json'):            
            comment = request.json.get('content')
        print(comment,request.headers)
    try:
        with open(f"./vars/account/account_{route2}.json") as f:
            data = json.load(f)  # 使用 json.load() 读取文件内容
        return data
    except Exception as e:
        return str(e), 400  # 返回错误信息和400状态码
    
@app.route("/account/<route1>/<route2>", methods=['POST', "GET"])
def buff(route1,route2):
    if request.method == "POST":
        if request.content_type.startswith('application/json'):            
            comment = request.json.get('content')
        print(comment,request.headers)
    try:
        with open(f"./vars/account/{route1}/account_{route1}_{route2}.json") as f:
            data = json.load(f)  # 使用 json.load() 读取文件内容
        return data
    except Exception as e:
        return str(e), 400  # 返回错误信息和400状态码

#starwatch
@app.route("/starwatch/auth/api/v1/auth", methods=['POST', "GET"])
def idk2():
    if request.method == "POST":
        if request.content_type.startswith('application/json'):            
            comment = request.json.get('content')
        print(comment,request.headers)
    try:
        with open(f"./vars/starwatch/auth/api/v1/starwatch_auth_api_v1_auth.json") as f:
            data = json.load(f)  # 使用 json.load() 读取文件内容
        return data
    except Exception as e:
        return str(e), 400  # 返回错误信息和400状态码

@app.route("/service/auth/api/v1/token", methods=['POST', "GET"])
def idk3():
    if request.method == "POST":
        if request.content_type.startswith('application/json'):            
            comment = request.json.get('content')
        print(comment,request.headers)
    try:
        with open(f"./vars/service/auth/api/v1/service_auth_api_v1_token.json") as f:
            data = json.load(f)  # 使用 json.load() 读取文件内容
        return data
    except Exception as e:
        return str(e), 400  # 返回错误信息和400状态码

#service
@app.route("/service/<route2>", methods=['POST', "GET"])
def service(route2):
    if request.method == "POST":
        if request.content_type.startswith('application/json'):            
            comment = request.json.get('content')
        print(comment,request.headers)
    try:
        with open(f"./vars/service/service_{route2}.json") as f:
            data = json.load(f)  # 使用 json.load() 读取文件内容
        return data
    except Exception as e:
        return str(e), 400  # 返回错误信息和400状态码
    
@app.route("/service/<route1>/<route2>", methods=['POST', "GET"])
def service1(route1,route2):
    if request.method == "POST":
        if request.content_type.startswith('application/json'):            
            comment = request.json.get('content')
        print(comment,request.headers)
    try:
        with open(f"./vars/service/{route1}/service_{route1}_{route2}.json") as f:
            data = json.load(f)  # 使用 json.load() 读取文件内容
        return data
    except Exception as e:
        return str(e), 400  # 返回错误信息和400状态码

@app.route("/service/<route1>/<route2>/<route3>", methods=['POST', "GET"])
def service2(route1,route2,route3):
    if request.method == "POST":
        if request.content_type.startswith('application/json'):            
            comment = request.json.get('content')
        print(comment,request.headers)
    try:
        with open(f"./vars/service/{route1}/{route2}/service_{route1}_{route2}_{route3}.json") as f:
            data = json.load(f)  # 使用 json.load() 读取文件内容
        return data
    except Exception as e:
        return str(e), 400  # 返回错误信息和400状态码

@app.route("/service/<route1>/<route2>/<route3>/<route4>", methods=['POST', "GET"])
def service3(route1,route2,route3,route4):
    if request.method == "POST":
        if request.content_type.startswith('application/json'):            
            comment = request.json.get('content')
        print(comment,request.headers)
    try:
        with open(f"./vars/service/{route1}/{route2}/{route3}/service_{route1}_{route2}_{route3}_{route4}.json") as f:
            data = json.load(f)  # 使用 json.load() 读取文件内容
        return data
    except Exception as e:
        return str(e), 400  # 返回错误信息和400状态码
    
@app.route("/service/<route1>/<route2>/<route3>/<route4>/<route5>", methods=['POST', "GET"])
def service4(route1,route2,route3,route4,route5):
    if request.method == "POST":
        if request.content_type.startswith('application/json'):            
            comment = request.json.get('content')
        print(comment,request.headers)
    try:
        with open(f"./vars/service/{route1}/{route2}/{route3}/{route4}/service_{route1}_{route2}_{route3}_{route4}_{route5}.json") as f:
            data = json.load(f)  # 使用 json.load() 读取文件内容
        return data
    except Exception as e:
        return str(e), 400  # 返回错误信息和400状态码





if __name__ == '__main__':
    context = ('./certs/cert.pem', './certs/key.pem')  # 替换为你的SSL证书和密钥文件路径
    app.run(host='0.0.0.0', port=443, ssl_context=context)