import mysql.connector
import datetime


def chk_report(msisdn, send_time):
    result = ""
    flag = 0
    mydb = mysql.connector.connect(
                host="192.168.91.41",
                user="smsai",
                password="SmsAI12k!@%32",
                database="bulkinfo"
    )


    mycursor = mydb.cursor()
    sql = "SELECT infozilion_response_code, mno_response_code, mno_response_message, hittime, masking FROM infozilion_logs WHERE msisdn = %s and hittime = %s"
    #note
    val = ('88'+msisdn, send_time,)

    mycursor.execute(sql, val)
    Log=mycursor.fetchall()
    #result = result + Log
    print("log: asol ", Log)

    for x in Log:
        print("1st", str(x))
        if str(x[1]) != "1000":
            if str(x[0]) !=  "9000":
                result = result + "Masking "+x[4]+" SMS for MSISDN: "+msisdn+" is Failed for Telco end issue at "+str(x[3])+"\n"
            else:
                result = result + "Masking "+x[4]+" SMS for MSISDN: "+msisdn+" is Failed for "+str(x[2])+" at "+str(x[3])+"\n"
        else:
            result = " ".join(map(str, x))
            flag = 1

    val = (msisdn, send_time,)
    mycursor.execute(sql, val)
    Log=mycursor.fetchall()
    #result = result + Log)
    for x in Log:
        print("2st", str(x))
        if str(x[1]) != "1000":
            if x[0] !=  "9000":
                result = result + "Masking "+x[4]+" SMS for MSISDN: "+msisdn+" is Failed for Telco end issue at "+str(x[3])+"\n"
            else:
                result = result + "Masking "+x[4]+" SMS for MSISDN: "+msisdn+" is Failed for "+str(x[2])+" at "+str(x[3])+"\n"
        else:
            result =  " ".join(map(str, x))
            flag = 1

    val = (msisdn[3:], send_time,)
    mycursor.execute(sql, val)
    Log=mycursor.fetchall()
    #result = result + Log)
    for x in Log:
        print("3rd", str(x))
        if str(x[1]) != "1000":
            if x[0] !=  "9000":
                result = result + "Masking "+x[4]+" SMS for MSISDN: "+msisdn+" is Failed for Telco end issue at "+str(x[3])+"\n"
            else:
                result = result + "Masking "+x[4]+" SMS for MSISDN: "+msisdn+" is Failed for "+str(x[2])+" at "+str(x[3])+"\n"
        else:
            result = " ".join(map(str, x))
            flag = 1

    type(result)
    print("check report result", result)
    return  result 

def infozilion_logs_report(msisdn, fdate,tdate):
    result = ""
    mydb = mysql.connector.connect(
                host="192.168.91.41",
                user="smsai",
                password="SmsAI12k!@%32",
                database="bulkinfo"
    )

    mycursor = mydb.cursor()
    sql = "SELECT masking, request, response, hittime, response_time, msisdn FROM ( SELECT i.masking AS masking, i.request AS request, i.response AS response , i.hittime AS hittime, i.response_time AS response_time, i.msisdn AS msisdn FROM infozilion_logs v JOIN infozilion_logs_backup i ON i.msisdn = v.msisdn WHERE DATE(i.hittime) BETWEEN %s AND  %s) AS infozilion WHERE msisdn_no = %s "
    #DATE(in_time) Between %s and %s ORDER BY in_time DESC"
    val = (fdate, tdate, '88'+msisdn)

    mycursor.execute(sql, val)
    Log=mycursor.fetchall()
    #result = result + Log
    print("log: infozilion ", Log)
