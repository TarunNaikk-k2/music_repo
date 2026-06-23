#### Repository directly talsk to database

from app.model.user_model import User

class UserRepository:

    def save(self,db,user):
        db.add(user)
        db.commit()
        db.refresh(user)

        return user
    
    # db.get() is used for fetching a single record by primary key.

    # Example:

    # db.get(User, 1)


    def get_all_users(self,db):
        return db.query(User).all()
