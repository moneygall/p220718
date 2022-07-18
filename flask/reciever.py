from  flask import Flask, request, abort

app = Flask(__name__)

@app.route('/webhook', methods=["POST", "GET"])
def webhook():
    if request.method == 'POST':
        name= request.json["name"]
        print(name)
        return f'<p>name {name}</p>' 
    
    elif request.method == 'GET':
        name= "helloWorld."
        return f'<p>{name}</p>' 
    
    else:
        abort(400)
    
if __name__ == '__main__':
    app.run()