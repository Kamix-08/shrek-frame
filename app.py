from flask import Flask, request, send_file
from flask_cors import CORS
import cv2
import imageio
import os
import tempfile
import random

app = Flask(__name__)
CORS(app)

@app.route('/get_frame', methods=['GET'])
def get_frame():
    frame_number = request.args.get('frame_number', type=int)

    if frame_number is None:
        return "Frame number is required.", 400

    video_path = "./shrek.avi"

    if not os.path.exists(video_path):
        return "Video file not found.", 404

    cap = cv2.VideoCapture(video_path)
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

    success, frame = cap.read()
    cap.release()

    if not success:
        return "Could not retrieve frame.", 404
    
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    temp_image_path = tempfile.mktemp(suffix='.webp')
    imageio.imwrite(temp_image_path, frame, format='WEBP')

    return send_file(temp_image_path, mimetype='image/webp')

@app.route('/get_random_frame', methods=['GET'])
def get_random_frame():
    video_path = "./shrek.avi"

    if not os.path.exists(video_path):
        return "Video file not found.", 404

    cap = cv2.VideoCapture(video_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    random_frame_number = random.randint(0, total_frames - 1)
    cap.set(cv2.CAP_PROP_POS_FRAMES, random_frame_number)

    success, frame = cap.read()
    cap.release()

    if not success:
        return "Could not retrieve frame.", 404
    
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    temp_image_path = tempfile.mktemp(suffix='.webp')
    imageio.imwrite(temp_image_path, frame, format='WEBP')

    return send_file(temp_image_path, mimetype='image/webp')

@app.route('/get_length', methods=['GET'])
def get_length():
    video_path = "./shrek.avi"

    if not os.path.exists(video_path):
        return "Video file not found.", 404

    cap = cv2.VideoCapture(video_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    cap.release()

    return {"total_frames": total_frames}, 200

if __name__ == '__main__':
    app.run(debug=True)
