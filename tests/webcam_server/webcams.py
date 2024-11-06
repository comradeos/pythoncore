import cv2
from flask import Flask, Response

app = Flask(__name__)

def generate_frames_0():
    camera = cv2.VideoCapture(0)  # 0 для первой веб-камеры, 1 для второй и т.д.
    
    while True:
        success, frame = camera.read()  # Захват кадра
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)  # Кодирование кадра в JPEG формат
            frame = buffer.tobytes()
            
            # Передача кадра
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


def generate_frames_1():
    camera = cv2.VideoCapture(1)
    
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            
            # Передача кадра
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_0')
def video_feed_0():
    return Response(generate_frames_0(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_1')
def video_feed_1():
    return Response(generate_frames_1(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8880)
