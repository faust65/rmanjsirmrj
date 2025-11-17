from flask import Flask, request, jsonify, render_template
import random
import math

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data=request.get_json()
    stat=int(data.get('stat', '0'))
    
    g=random.randrange(1, 101)
    
    if(g==1):
        message=f"대성공({g})"
    elif(g==99 or g==100):
        message=f"대실패({g})"
    elif(stat*12<g):
        message=f"실패({g})"
    elif(stat*12>=g):
        message=f"보통 성공({g})"
        if((stat*12)/2>g):
            message=f"어려운 성공({g})"
            if((stat*12)/5>g):
                message=f"극단적 성공({g})"
        
    return jsonify({'message':message})

@app.route('/process2', methods=['POST'])
def process2():
    data=request.get_json()
    stat=int(data.get('stat', '0'))
    
    g=random.randrange(1, 101)

    if(g==99 or g==100):
        message=f"대실패({g})"
    elif((stat==1 and g<=20) or (stat==2 and g<=40) or (stat==3 and g<=50) or (stat==4 and g<=60) or (stat==5 and g<=80)):
        message=f"성공({g})"
    else:
        message=f"실패({g})"
    
    return jsonify({'message':message})

@app.route('/process3', methods=['POST'])
def process3():
    data=request.get_json()
    name=data.get('name', '0').split(sep=" ")
    random.shuffle(name)
    result=[]
    for i in range(0, len(name)-1,2):
        message=f"{name[i]}:{name[i+1]}"
        result.append(message)

    if len(name) % 2 == 1:  
        result.append(name[-1])

    message = "\n".join(result)
    return jsonify({'message':message})
    
    
if __name__ == '__main__':

    app.run(debug=True)

