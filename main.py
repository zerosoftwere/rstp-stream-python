from flask import Flask, Response, request, render_template
from cv2 import VideoCapture, imencode

app = Flask(__name__, static_folder='assets', static_url_path='/assets')

def get_frames(url):
    camera = VideoCapture(url)
    while True:
        success, frame = camera.read()
        if not success:
            break
        ret, buffer = imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/video_feed', methods=['GET'])
def video_feed():
    cam_url = request.args.get('cam_url')
    try:
        frame = get_frames(cam_url)
        return Response(frame, mimetype='multipart/x-mixed-replace; boundary=frame')
    except:
        return Response(status=404)

if __name__ == '__main__':
    app.run(debug=True)