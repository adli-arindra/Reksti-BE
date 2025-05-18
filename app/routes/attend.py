from fastapi import APIRouter, HTTPException
from app.models.schemas import AttendRequest, AttendResponse
from src.model import get_encoding_base64, compare
from database.sql import Encoding, ClassEntry

router = APIRouter()

@router.post("/attend", response_model=AttendResponse)
async def attend_class(data: AttendRequest):
    try:
        input_encoding = get_encoding_base64(data.foto_wajah)
        print(input_encoding)
        if input_encoding is None:
            raise ValueError("No face detected")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to process photo: {str(e)}")

    matched_nim = Encoding.match(input_encoding)
    if matched_nim == -1:
        return {"status": False, "message": "No matching face found"}

    ClassEntry.update(data.class_uid, matched_nim, True)
    return {"status": True, "message": "Attendance recorded", "student": matched_nim}

