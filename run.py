from flask import Flask, render_template, jsonify,request, send_from_directory,url_for
from random import *
from flask_cors import CORS
import os
import csv
import logging
import requests
#AES Crypto 
from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto.Util.number import bytes_to_long
from Crypto import Random
import base64
import base62

# ETC
import time
import shutil
import zipfile
#from flask_wtf import FLASKForm
from rstr import xeger

#AES_CTR 암호화 Key
WEB_KEY = b'icrftWEBSQRR0001'
#WEB_KEY = b'Sixteen byte key'
iv = b'brandsaferSQR001' #초기화 벡터
#iv = Random.new().read(AES.block_size)

#Initialization
app = Flask(__name__,
            static_folder = "./dist/static",
            template_folder = "./dist")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

#File Upload Directory path 
UPLOAD_DIRECTORY = os.getcwd()
ALLOWED_EXTENSIONS = set(['csv'])
app.config['UPLOAD_DIRECTORY'] = UPLOAD_DIRECTORY+"//UPLOAD"


if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)
        
#Create zip file upload folder
uploadpath = UPLOAD_DIRECTORY+"//UPLOAD" 
if not os.path.exists(uploadpath):
    os.makedirs(uploadpath)
else :
    #remove last zip files
    for folder, subfolders, files in os.walk(uploadpath):
        for file in files:
            if file.endswith('.zip'):
                os.remove(uploadpath+'//'+file)

#Flask_wtf key value 
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

#AES_CTR Encrytion setting
ctr_e = Counter.new(128, initial_value = bytes_to_long(iv))
encryption_suite = AES.new(WEB_KEY, AES.MODE_CTR, counter=ctr_e)

#Make Blockchain data table
def to_pretty_json(value):
    return json.dumps(value, sort_keys=True,
                      indent=4, separators=(',', ': '))
app.jinja_env.filters['tojson_pretty'] = to_pretty_json # jinja2에서 자신만의 필터 등록
def to_json_data(numbers, company):
  result = []
  for number in numbers:
    result.append({
        "$class": "org.example.mynetwork.RandomNum",
        "number": number,
        "owner": "resource:org.example.mynetwork.Customer#" + company,
        "isConfirmed": "false"
      })
  return result

# #Zip File Upload Logic      
# @app.route('/api/files/',defaults={'path': '/api/files/'})
# def get_file(path):
#     file_list = os.listdir(uploadpath)
#     return send_from_directory(uploadpath, file_list[0], as_attachment=True)

#Zip File Upload Logic      
@app.route('/api/files/',defaults={'path': '/api/files/'}, methods=['GET','POST'])
def get_file(path):
    data = request.get_json()
    zipfilename = data.get('zipfilename')
    file_list = os.listdir(uploadpath)
    for file in file_list:
        if (str(file) == zipfilename):
            rtn = send_from_directory(uploadpath, file, as_attachment=True)
    return rtn

#RD_Num_Generating Logic
@app.route('/api/random',defaults={'path2': '/api/random'}, methods=['GET','POST'])
def random_number(path2):

    #request parsing
    data = request.get_json()
    search = "_"
    #company info
    rawcompany = request.get_json().get('company')
    idxcom = rawcompany.find(search)
    company = rawcompany[:idxcom]
    company_label = rawcompany[idxcom+1:]
    #regex info
    rawregex = request.get_json().get('regex')
    idxcom = rawregex.find(search)
    regex = rawregex[:idxcom]
    regex_label = rawregex[idxcom+1:]
    #number info
    number = int(request.get_json().get('number')) * 10000  #총 생산 난수 갯수 (만개 단위)
    #fileline info
    fileline = int(request.get_json().get('fileline')) * 10000 # 한 파일당 난수 갯수 (만개 단위)
    filetotal = number / fileline # 총 CSV 파일 갯수
    keyval = list(data.keys()) 
    #Generator initialize
    rdGen = [ ]
    filebox = []

    r = None
    filecnt = 0
    now = time.localtime()
    #Result csv file path setting
    companypath = UPLOAD_DIRECTORY+"//"+company_label+"//"
    currentfolder = company_label+"_"+str(number)+"_"+str(now.tm_year)+str(now.tm_mon)+str(now.tm_mday)
    filepath = companypath + currentfolder

    #Make result csv folder
    if not os.path.exists(filepath):
        os.makedirs(filepath)
        
    while filecnt < filetotal:
        #Create CSV file
        file_name = "%s//%s_Number%s_%02d_%s%s%s%s%s.csv" % (filepath,company_label,regex_label,filecnt+1,now.tm_year,now.tm_mon,now.tm_mday,now.tm_hour,now.tm_min)
        f = open(file_name,'w',encoding='utf-8',newline='')
        filebox.append(file_name)
        wr = csv.writer(f)
        #Classification by SQR_Number
        #Write top line in CSV file(statuc url)
        if (int(regex_label) >= 3):
            wr.writerow(["http://g.bsq.kr/api/g?d="])
        elif (int(regex_label) == 2):
            wr.writerow(["HTTP://BSQ.KR/%s" % (company)])
        elif (int(regex_label) == 1):
            wr.writerow(["HTTP://BRANDSAFER.COM//%s" % (company)])

        #Generate Random Number
        while len(rdGen) < fileline:
            rawrd = xeger(regex)
            rd = "%s%s%s" % (rawrd[:3],company,rawrd[3:])
            
            rdGen.append(rd)
            if int(regex_label) ==1:
                secretrd = rd[0:5] + rd[11:]
                ocr = rd[5:11]
                Imgfilename = "%s_%s_%s_%s%s%s" %(company_label,regex_label,ocr,now.tm_year,now.tm_mon,now.tm_mday)
                wr.writerow([ secretrd,ocr, Imgfilename])
            elif int(regex_label) ==2:
                secretrd = rd[0:5] + rd[10:]
                ocr = rd[5:10]
                Imgfilename = "%s_%s_%s_%s%s%s" %(company_label,regex_label,ocr,now.tm_year,now.tm_mon,now.tm_mday)
                wr.writerow([ secretrd,ocr,regex_label, Imgfilename])
            elif int(regex_label) ==3:
                secretrd = rd[0:5] + rd[10:]
                ocr = rd[5:10]
                cipher_text = base64.b64encode(encryption_suite.encrypt(rd.encode('utf-8')))
               # decry_text = base64.b64decode(encryption_suite.decrypt(cipher_text))
                decry_text = base64.b64decode(cipher_text)

                Imgfilename = "%s_%s_%s_%s%s%s" %(company_label,regex_label,ocr,now.tm_year,now.tm_mon,now.tm_mday)
                wr.writerow([ secretrd,ocr,cipher_text.decode("utf-8"),regex_label, Imgfilename])
        data =to_json_data(rdGen,company)
        #r = requests.post('http://ec2-13-124-15-96.ap-northeast-2.compute.amazonaws.com:3000/api/RandomNum',json=data)
        #r = r.json()
        rdGen = []
        filecnt += 1

    f.close()
    
    #Create zip file
    csvzipfile = zipfile.ZipFile(filepath+"//"+currentfolder+".zip","w")
    for folder, subfolders, files in os.walk(filepath):
        for file in files:
            if file.endswith('.csv'):
                csvzipfile.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder, file),filepath),compress_type = zipfile.ZIP_DEFLATED)
    shutil.copy(filepath+"//"+currentfolder+".zip",uploadpath)
    csvzipfile.close()

    response = {
        'randomNumber': randint(1, 100),
        'company': company,
        'regex': regex,
        'number':number,
        'fileline':fileline,
        'zipfilename': currentfolder+".zip"
        #'zipfile': send_from_directory(filepath, currentfolder+".zip", as_attachment=True)
        
    }
    return jsonify(response)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if app.debug:
        return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template("index.html")


if __name__ == '__main__':
   app.run(debug=True)