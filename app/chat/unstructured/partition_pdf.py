from unstructured.partition.pdf import partition_pdf

pdf_elements = partition_pdf(
    filename="pdf_path",
    strategy="hi_res",
    extract_images_in_pdf=True,
    extract_image_block_types=["Image", "Table"],
    extract_image_block_to_payload=False,
    extract_image_block_output_dir="../images",
)
