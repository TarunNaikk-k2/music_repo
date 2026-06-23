from fastapi import APIRouter,Depends,HTTPException
from typing import List
# Every type of controller requires Session first
from sqlalchemy.orm import Session

# validation Types
from app.schemas.music_instrument_create import MusicInstrumentCreate
from app.schemas.music_instrument_response import MusicInstrumentResponse

# service
from app.service.music_instrument_service import MusicInstrumentrService

from app.dao.db_session import get_db

router=APIRouter()

music_service=MusicInstrumentrService()

@router.post("/create_instrument")
def create_instrument(
    music_instrument:MusicInstrumentCreate,
    db:Session = Depends(get_db),
):
    return music_service.music_create(
        db,
        music_instrument
    )
    

@router.get("/all_music_instruments",response_model=List[MusicInstrumentResponse])
def get_items(db:Session=Depends(get_db)):
    return music_service.get_music_items(db)

@router.get("/music_by_name/{name}",response_model=MusicInstrumentResponse)
def get_instrument_name(name:str,db:Session = Depends(get_db)):
    instrument=music_service.get_instrument_by_name(db,name.lower())
    if instrument is None:
        raise HTTPException(
            status_code=404,
            detail="Instrument Not Found"
        )
    
    return instrument