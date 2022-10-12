import flask
from flask import request, Flask

app = Flask(__name__)

def failed(error_message):
    print(error_message)
    return error_message

def send_data_to_screen(message):
    return True

@app.route("/message", methods=['POST'])
def getMessage():
    try:
        data = request.get_json()
        if(data['message']):
            send_data_to_screen(data['message'])
        else:
            return failed(f'Message required in body payload')
    except Exception as error:
        return failed(f'Failed to send message, received the error: {error}')