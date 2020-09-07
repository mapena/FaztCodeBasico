from flask import Flask

app = Flask(__name__)
app.secret_key = "mysecretkey"  # se crea para crear una session que lo utiliza flash para los mensajes.

#---------------------------------------------------------------------------------------------------------
# main
#---------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    app.run(port=3000, debug=True)
