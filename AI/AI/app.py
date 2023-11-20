from flask import Flask, jsonify, request, make_response
import num_valid
import isms_processing_check
import ismsPlus_processing_check
import json

app = Flask(__name__)
result = "test result"
@app.route('/smsai', methods = ['GET', 'POST'])
def home():
    msisdn = request.args.get('msisdn')
    fsmstime = request.args.get('fdate')
    tsmstime = request.args.get('tdate')
    msisdn_validity = num_valid.valid_num(msisdn)
    if msisdn_validity == True:
        #print("True")
        old = isms_processing_check.isms_bulklog(msisdn, fsmstime, tsmstime)
        new = ismsPlus_processing_check.isms_bulklog(msisdn, fsmstime, tsmstime)
        result = old+new
        #print(result)
        if result == "Response: ":
            return "No SMS request found for the msisdn: "+msisdn+" at the mentioned time."
        else:
            return result
    else:
        return "Invalid MSISDN"
        
    return jsonify({"hello  ": home()})

if __name__ == '__main__':
  
    app.run(debug = True, host = '0.0.0.0', port = 80)