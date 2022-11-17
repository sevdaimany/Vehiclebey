import rabbitMQ
import database
from object_storage import get_object_url
from image_tagging import tag
from sendemail import send_message





def main():   
    rabbitMQ.main(callback)
    
    
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)   
     
    splited_body = body.decode('utf-8').split(",")
    received_id = int(splited_body[0])
    text= splited_body[1]
    image_url = get_object_url(received_id)
    print("image url : ", image_url)
    image_tag = tag(image_url)
    if image_tag != None:
        state = 2
        database.update_row((image_tag, state, received_id))  
        print("آگهی تایید شد")
        print(">>> ACCEPT")
        email_req = send_message("آگهی تایید شد",mail_text(text, image_url))
        print("\n\n mail message: ", mail_text(text, image_url) )
        print("status code email: ", email_req.status_code)

    else:
        state = 1
        database.update_row((None, state, received_id))  
        print("آگهی رد شد")
        print(">>> FAILED")
        email_req = send_message("آگهی رد شد", "متاسفم! آکهی شما رد شد.")
        print("status code email: ", email_req.status_code)
    
  
def mail_text(text, image_url):
    txt= ""
    txt +=      "تبریک آگهی شما در سیستم ثبت شد"
    txt += "\n"
    txt  += "لینک آگهی شما: "
    txt += f"http://127.0.0.1:5000/showad?text={text}&image={image_url}"
    return txt
            
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
    