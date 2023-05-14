# Streaming video via RSTP
Spike on streaming video from a remote ip camera

## Requirements
- Python 3
- Pip 3
- IP Camera
- virtual env

## Run project
- `virtualenv .venv`
- `source .venv/bin/activate`
- `pip install -r requirements.txt`
- `python main.py`

Access application interface on browser using the `http://localhost:5000/`

## Use Webcam as IP camera on linux system
```
sudo apt-get install v4l-utils
sudo v4l2-ctl --list-devices

docker run --rm -it --network=host aler9/rtsp-simple-server

sudo ffmpeg -f v4l2 -framerate 25 -video_size 640x480 -i /dev/video0 -f rtsp -rtsp_transport tcp rtsp://localhost:8554/mystream

```

You should be able to access webcam on the address `rtsp://localhost:8554/mystream`