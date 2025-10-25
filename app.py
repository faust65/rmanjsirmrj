from flask import Flask, request, jsonify, render_template
import random

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
    
if __name__ == '__main__':
    app.run(debug=True)