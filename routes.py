import time
from base64 import b64encode

from fastapi import APIRouter, UploadFile

from ocr import extract_ocr_data_from_id_card

router = APIRouter()


@router.post("/ocr/id-card")
async def ocr(file: UploadFile):
    image_content = await file.read()
    encoded_image = b64encode(image_content).decode("utf-8")
    ocr_time = time.perf_counter()
    data = extract_ocr_data_from_id_card(f"data:image/jpeg;base64,{encoded_image}")
    ocr_time = time.perf_counter() - ocr_time

    return {
        "data": data,
        "ocr_time": ocr_time
    }
