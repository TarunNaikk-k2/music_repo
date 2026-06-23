from sqlalchemy.orm import Session
from app.repository.music_repository import MusicRepository
from app.model.music_instrument import Music_Instrument

class MusicInstrumentrService:
    def __init__(self):
        # init will directly pass into repository
        self.music_repository=MusicRepository

    def music_create(self,db:Session,music_instrument: Music_Instrument):

        # ila objects pampinchu object ni decode chesi appudu send cheye
        instrument=Music_Instrument(
            name=music_instrument.name,
            category=music_instrument.category,
            price=music_instrument.price,
            quantity=music_instrument.quantity
        )

        return self.music_repository.save(db,music_instrument=instrument)
    
    def get_music_items(self,db:Session):
        return self.music_repository.get_all(db)

    def get_instrument_by_name(self,db,name):
        return self.music_repository.get_instrument_by_name(db,name)