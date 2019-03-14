from flask import (
    Flask,
    render_template
)

from flask import request, Response
import tailer




# Create the application instance
app = Flask(__name__, template_folder="templates")

# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/

    :return:        the last 20 queries '
    """
    last_lines = tailer.tail(open('/data/queries.txt'), 20)    
    last_lines = ''.join([x+"\n" for x in last_lines])

    return Response(last_lines, mimetype='text/plain') 


@app.route('/api/sink/', methods=['GET', 'POST'])
def sink():
    import datetime
    query = dict()

    content = request.get_json(silent=True)
    query["Timestamp"] = str(datetime.datetime.now())
    query["Type"] = request.method
    query["IP"] = request.remote_addr
    query["Payload"] = content
    

    print(query) # Do your processing 
    with open("/data/queries.txt", "a") as myfile:
    	myfile.write(str(query)+"\n")

    return "ok"


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0',port=5000)

