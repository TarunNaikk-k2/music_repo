## write only the methods you want here without any dependecy since we are not using init
from app.model.music_instrument import Music_Instrument

class MusicRepository:
    def save(db,music_instrument):
        db.add(music_instrument)
        db.commit()
        db.refresh(music_instrument)

        return music_instrument
    
    def get_all(db):
        return db.query(Music_Instrument).all()
    
    def get_instrument_by_name(db,name):
        return db.query(Music_Instrument)\
                 .filter(Music_Instrument.name==name)\
                 .first()
        

    
    
    