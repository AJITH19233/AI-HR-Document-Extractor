import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

UPLOAD_DIR = os.getenv("UPLOAD_DIR", "uploads")

MAX_FILE_SIZE = int(os.getenv("MAX_FILE_SIZE", 10 * 1024 * 1024))

ALLOWED_EXTENSIONS = set(
    os.getenv(
        "ALLOWED_EXTENSIONS",
        ".pdf,.png,.jpg,.jpeg"
    ).split(",")
)

DATABASE_URL = os.getenv("DATABASE_URL")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")