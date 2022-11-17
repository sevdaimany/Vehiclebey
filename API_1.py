
import database
import object_storage
import rabbitMQ
from flask import Flask, render_template
from flask import  request
app = Flask(__name__)

def get_last_id():
    unique_id = database.get_last_id()[0]
    if unique_id== None:
        unique_id = 0
    unique_id += 1
    return unique_id

@app.route(f'/showad', methods=["GET"])
def show():
    text = request.args['text']
    url = request.args["image"]
    return render_template('index.html', text=text, image_url=url)
    

@app.route('/add', methods=["GET"])
def main():
    unique_id = get_last_id()
    while(True):
        
        text = request.form['text']
        file = request.files["image"].read()
        email = request.form['email']
        state = 0
        print("")
        print("received text: ", text)
        print("received file", type(file))
        print("received email: ", email)
        record_to_insert = (unique_id, text, email, state, " ")
        database.insert_todb(record_to_insert)
        object_storage.put_object(file, unique_id)
        rabbitMQ.send(f"{unique_id},{text}")
        return_text= "آگهی شما با شناسه "+ str(unique_id) + "ثبت شد"
        print(return_text)
        print(">> Done")
        return return_text, 200
     
if __name__ == '__main__':
    try:
        app.run(debug=True)
    except KeyboardInterrupt:
        print('Interrupted')
    