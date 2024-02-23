from flask import Flask, request, send_file, jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)
UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"pdf"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


def allowed_file(filename):
    """The allowed_file() function checks if a given file name is allowed based on a list of allowed extensions. It takes a single argument, filename, which should be a string representing the file name. The function returns a boolean value indicating whether the file is allowed or not."""
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/upload", methods=["POST"])
def upload_file():
    """Uploads a file.

    Checks if a file is included in the request, checks the filename is not empty,
    checks the file type is allowed, saves the file to the upload folder, and
    returns a success response with the filename if successful, else returns
    an error response.
    """
    if "file" not in request.files:
        return jsonify({"message": "No file part in the request"}, 400)
    file = request.files["file"]

    if file.filename == "":
        return jsonify({"message": "No selected file"}, 400)
    if file:
        filename = secure_filename(file.filename)  # type: ignore
        print(filename)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        return jsonify({"message": f"File {filename} uploaded successfully"}, 200)
    else:
        return jsonify({"message": "File type not allowed"}, 400)


@app.route(rule="/delete", methods=["DELETE"])
def delete_file():
    """Deletes a file.

    Checks for a 'file' header with the filename.
    Attempts to delete the file from the upload folder.
    Returns a success response if deleted, else an error response.
    """
    if "file" not in request.headers:
        return jsonify({"message": "No file part in the request"}, 400)
    filename = request.headers["file"]
    try:
        os.remove(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        return jsonify({"message": f"File {filename} deleted successfully"}, 200)
    except Exception as e:
        return jsonify({"message": f"Error deleting file: {e}"}, 400)


@app.route("/download/<filename>", methods=["GET"])
def download_file(filename):
    """Downloads a file.

    Checks if the requested file exists in the upload folder.
    If it exists, returns the file contents.
    If not, returns a 404 error.
    """
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    if os.path.exists(filepath):
        return send_file(filepath, as_attachment=False, mimetype="application/pdf")
    else:
        return jsonify({"message": "File not found"}, 404)


if __name__ == "__main__":
    """If this script is run directly, start the Flask app."""
    app.run(debug=True, port=8050)
