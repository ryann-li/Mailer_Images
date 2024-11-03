from flask import Flask, send_file
from io import BytesIO

app = Flask(__name__)

# Initialize the access counter
access_count = 0

@app.route('/')
def main():
    return "hello world"

@app.route('/tracking-image.png')
def tracking_image():
    global access_count
    access_count += 1  # Increment the counter each time the endpoint is accessed
    print(f"Image accessed {access_count} times")

    # Serve a 1x1 transparent pixel image
    img = BytesIO()
    img.write(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\rIDATx\xdacd`\x00\x00\x00\x02\x00\x01\xe2!\xbc\x33\x00\x00\x00\x00IEND\xaeB`\x82')
    img.seek(0)
    
    return send_file(img, mimetype='image/png')

if __name__ == "__main__":
    app.run(port=5000, debug=True)
