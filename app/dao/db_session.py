from app.database import SessionLocal

def get_db():

    # SessionLocal is a factory for creating the sessions and here db means simgle session and every request  uses one session each 

    db = SessionLocal()

    try: 
        yield db

    finally:
        db.close()