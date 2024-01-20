from flask import Blueprint, g, jsonify, make_response
from httpx import delete
from werkzeug.exceptions import Unauthorized
from app.web.hooks import (
    login_required,
    handle_file_upload,
    load_model,
)
from app.web.db.models import Pdf
from app.web.tasks.embeddings import process_document
from app.web import files

bp = Blueprint("pdf", __name__, url_prefix="/api/pdfs")


@bp.route("/", methods=["GET"])
@login_required
def list():
    pdfs = Pdf.where(user_id=g.user.id)

    return Pdf.as_dicts(pdfs)


@bp.route("/", methods=["POST"])
@login_required
@handle_file_upload
def upload_file(file_id, file_path, file_name):
    res, status_code = files.upload(file_path)
    if status_code >= 400:
        return res, status_code

    pdf = Pdf.create(id=file_id, name=file_name, user_id=g.user.id)

    # Defer this to be processed by the worker
    process_document.delay(pdf.id)  # type: ignore

    return pdf.as_dict()


@bp.route("/<string:pdf_id>", methods=["DELETE"])
@login_required
def delete_file(file_id, file_name):
    res, status_code = files.delete(file_name)
    if status_code >= 400:
        return make_response(res, status_code)

    Pdf.delete_by(id=file_id, name=file_name, user_id=g.user.id)

    # Defer this to be processed by the worker
    delete_document.delay(pdf.id)  # type: ignore

    return make_response("", 204)


@bp.route("/<string:pdf_id>", methods=["GET"])
@login_required
@load_model(Pdf)  # type: ignore
def show(pdf):
    return jsonify(
        {
            "pdf": pdf.as_dict(),
            "download_url": files.create_download_url(pdf.id),
        }
    )
