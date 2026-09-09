from pathlib import Path

import pdfplumber
from docx import Document


def extract_text(file_path):
	"""Extract readable text from a PDF or DOCX resume."""
	path = Path(file_path)

	if path.suffix.lower() == ".pdf":
		with pdfplumber.open(path) as pdf:
			return "\n".join(
				page.extract_text() or ""
				for page in pdf.pages
			).strip()

	if path.suffix.lower() == ".docx":
		document = Document(path)
		return "\n".join(
			paragraph.text
			for paragraph in document.paragraphs
			if paragraph.text.strip()
		).strip()

	raise ValueError("Unsupported file type. Only PDF and DOCX files are supported.")
