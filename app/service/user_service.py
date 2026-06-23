from app.model.user_model import User
from app.model.address_model import Address

from app.repository.user_repository import UserRepository

class UserService():

    def __init__(self):
        self.user_repository = UserRepository()

    def create_user(self,db,user_request):

        user=User(
            first_name=user_request.first_name,
            last_name = user_request.last_name,
            email=user_request.email,
            phone_number=user_request.phone_number,
            role=user_request.role,
            password=user_request.password
        )

        for address in user_request.addresses:
            
            user.addresses.append(
                Address(
                    name=address.name,
                    street=address.street,
                    city=address.city,
                    state=address.state,
                    pincode=address.pincode
                )
            )

        return self.user_repository.save(db,user=user)
    
    def get_all_users(self,db):

        return self.user_repository.get_all_users(db)
