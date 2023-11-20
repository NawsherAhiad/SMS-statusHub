import mysql.connector
import datetime

def chk_report(msisdn, send_time):
    result = ""
    flag = 0
    mydb = mysql.connector.connect(
                host="192.168.91.150",
                user="smsai",
                password="SmsAI12k!@%32",
                database="bulkinfo"
    )
    mycursor = mydb.cursor()
    sql = "SELECT infozilion_response_code, mno_response_code, mno_response_message, hittime, masking FROM infozilion_logs WHERE msisdn = %s and hittime = %s"
    val = ('88'+msisdn, send_time,)
    mycursor.execute(sql, val)
    Log=mycursor.fetchall()
    #result = result + Log)
    for x in Log:
        if str(x[1]) != "1000":
            if x[0] !=  "9000":
                result = result + "Masking "+x[4]+" SMS for MSISDN: "+msisdn+" is Failed for Telco end issue at "+str(x[3])+"\n"
            else:
                result = result + "Masking "+x[4]+" SMS for MSISDN: "+msisdn+" is Failed for "+str(x[2])+" at "+str(x[3])+"\n"
        else:
            flag = 1

    val = (msisdn, send_time,)
    mycursor.execute(sql, val)
    Log=mycursor.fetchall()
    #result = result + Log)
    for x in Log:
        if str(x[1]) != "1000":
            if x[0] !=  "9000":
                result = result + "Masking "+x[4]+" SMS for MSISDN: "+msisdn+" is Failed for Telco end issue at "+str(x[3])+"\n"
            else:
                result = result + "Masking "+x[4]+" SMS for MSISDN: "+msisdn+" is Failed for "+str(x[2])+" at "+str(x[3])+"\n"
        else:
            flag = 1

    val = (msisdn[3:], send_time,)
    mycursor.execute(sql, val)
    Log=mycursor.fetchall()
    #result = result + Log)
    for x in Log:
        if str(x[1]) != "1000":
            if x[0] !=  "9000":
                result = result + "Masking "+x[4]+" SMS for MSISDN: "+msisdn+" is Failed for Telco end issue at "+str(x[3])+"\n"
            else:
                result = result + "Masking "+x[4]+" SMS for MSISDN: "+msisdn+" is Failed for "+str(x[2])+" at "+str(x[3])+"\n"
        else:
            flag = 1

    return result

