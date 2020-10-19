from flask import Flask
import aws_s3_image

aws_flask = Flask(__name__)


@aws_flask.route("/mango", methods=["GET"])
def cricket():
    phone=aws_s3_image.salt()
    return phone




if __name__=="__main__":
    aws_flask.run(host="0.0.0.0")
