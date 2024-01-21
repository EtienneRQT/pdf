from celery import shared_task
from app.web.db.models import Pdf
from app.web.files import download
from app.chat.manage_embeddings import (
    create_embeddings_for_pdf,
    delete_embeddings_for_pdf,
)


@shared_task()
def process_document(pdf_id: int):
    pdf = Pdf.find_by(id=pdf_id)
    with download(pdf.id) as pdf_path:
        create_embeddings_for_pdf(pdf.id, pdf_path)


@shared_task()
def delete_document(pdf_id: int):
    pdf = Pdf.find_by(id=pdf_id)
    delete_embeddings_for_pdf(pdf.id)
