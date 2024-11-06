from flask import Flask, send_file, request, jsonify
from io import BytesIO

app = Flask(__name__)

# Dictionary to store access counts by department
access_counts_by_department = {}

@app.route('/')
def main():
    return "hello world"

@app.route('/tracking-image.png')
def tracking_image():
    # Get department from query parameters, defaulting to "unknown" if not provided
    department = request.args.get('department', 'unknown')
    
    # Increment the count for the department
    if department in access_counts_by_department:
        access_counts_by_department[department] += 1
    else:
        access_counts_by_department[department] = 1

    print(f"Image accessed for department '{department}', total count: {access_counts_by_department[department]}")

    # Serve a 1x1 transparent pixel image
    img = BytesIO()
    img.write(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\rIDATx\xdacd`\x00\x00\x00\x02\x00\x01\xe2!\xbc\x33\x00\x00\x00\x00IEND\xaeB`\x82')
    img.seek(0)
    
    return send_file(img, mimetype='image/png')

# New endpoint to get the access count for a specific department
@app.route('/get-department-email-count')
def get_department_email_count():
    department = request.args.get('department')
    
    # Check if the department exists in the dictionary
    if department in access_counts_by_department:
        count = access_counts_by_department[department]
        return jsonify({department: count})
    else:
        # If the department is not found, return 0 or an error message
        return jsonify({department: 0}), 404

if __name__ == "__main__":
    app.run(port=5000, debug=True)
