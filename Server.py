from flask import Flask, request

app = Flask(__name__)

@app.route('/callback')
def callback():
    code = request.args.get('code')
    print(f"Got code: {code}")
    return "Redirect handled" 

if __name__ == '__main__':
   app.run(port=8888)