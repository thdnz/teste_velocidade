from flask import Flask, request, render_template
import speedtest

app = Flask(__name__) 

@app.route('/') 
def index():
    return render_template('index.html') # renderiza o template index.html

@app.route('/start', methods=['POST']) # define a rota para o método POST
def start():
    s = speedtest.Speedtest()
    download_speed = s.download() / 1000000 # converte para megabytes
    upload_speed = s.upload() / 1000000 
    return f"Download speed: {download_speed:.2f} Mbps <br> Upload speed: {upload_speed:.2f} Mbps"

if __name__ == '__main__':
    app.run(debug=True)