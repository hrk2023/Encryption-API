from flask import Blueprint,jsonify,request
 
enc=Blueprint('enc',__name__)

@enc.route('/enc_rtype3f',methods=['POST'])
def enc_rtype3f():
    str_list=request.json["plainText"]
    length=len(str_list)
    cipher=''
    for i in range(3):
        index=i
        interval=3
        while index<length:
            cipher=cipher+str_list[index]
            index+=interval
    return jsonify({'cipher':cipher})
@enc.route('/dec_rtype3f',methods=['POST'])
def dec_rtype3f():
    str_list=request.json["cipher"]
    length=len(str_list)
    log=[0]*length
    rem=length%3
    quo=(int)(length/3)
    limit=0
    interval=[]
    plainText=''
    if rem==0:
        limit+=quo
        interval.extend([limit,limit,limit])
    elif rem==1:
        limit+=(quo+1)
        interval.extend([limit,limit-1,limit-1])
    elif rem==2:
        limit+=(quo+1)
        interval.extend([limit,limit-1,limit-1])
    for i in range(limit):
        flag=0
        index=i
        while index<length:
            step=interval[flag]
            if log[index]!=1:
                plainText=plainText+str_list[index]
                log[index]=1
            else:
                break
            flag+=1
            index+=step
    return jsonify({"plainText":plainText})


#-------------TEST ROUTES----------------
@enc.route('/dec_rtype3f/<cipher>',methods=['GET'])
def dec_test(cipher):
    str_list=cipher
    length=len(str_list)
    log=[0]*length
    rem=length%3
    quo=(int)(length/3)
    limit=0
    interval=[]
    plainText=''
    if rem==0:
        limit+=quo
        interval.extend([limit,limit,limit])
    elif rem==1:
        limit+=(quo+1)
        interval.extend([limit,limit-1,limit-1])
    elif rem==2:
        limit+=(quo+1)
        interval.extend([limit,limit-1,limit-1])
    for i in range(limit):
        flag=0
        index=i
        while index<length:
            step=interval[flag]
            if log[index]!=1:
                plainText=plainText+str_list[index]
                log[index]=1
            else:
                break
            flag+=1
            index+=step
    return jsonify({"plainText":plainText})

@enc.route('/enc_rtype3f/<plainText>',methods=['GET'])
def enc_test(plainText):
    str_list=plainText
    length=len(str_list)
    cipher=''
    for i in range(3):
        index=i
        interval=3
        while index<length:
            cipher=cipher+str_list[index]
            index+=interval
    return jsonify({'cipher':cipher})
