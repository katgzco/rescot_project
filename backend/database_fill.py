from api_quotation.models.model_basemodel import BaseModel
from api_quotation.models.model_quotation import Quotation
from api_quotation.models.model_artist import Artist
from api_quotation.models.model_user import User
from api_quotation.models.model_body import Body
from api_quotation.models.model_styles import Styles


artist1 = Artist(
    name='Angelica lavidum',
    mail='123@gmail.com',
    phone='3146624567',
    address='Envigado',
)
artist1.save()


styles1 = Styles(name='black', price_cm2=26000)
styles1.save()
styles1.fk_artist.set([artist1])

styles2 = Styles(name='color', price_cm2=31500)
styles2.save()
styles2.fk_artist.set([artist1])

body1 = Body(name='brazo', difficulty='1.3')
body1.save()
body1.fk_artist.set([artist1])

body2 = Body(name='antebrazo', difficulty='1.5')
body2.save()
body2.fk_artist.set([artist1])

# quotation1 = Quotation(size='10', body_part='brazo',
#                        style='black')
# quotation1.save()



# user1 = User(name='Mateo Londono', mail='mat@gmail.com',
#              phone='0123456789', fk_quotation=quotation1)
# user1.save()

# """ QUERIES """

# quotation2 = Quotation(size='50', body_part='back',
#                        style='neotraditional', total_time=0, total_price=0)
# quotation2.save()

# artist1 = artist1 = Artist(name='kat', mail='123@gmail.com', phone='0123456789', address='San Luis')
# artist1.save()

# new_artist = quotation2.artist.create(name='Fabrizio', lastname='Maurizi', mail='fbm@gmail.com', phone='010646469',
#                                       address='Italy')

# quotation2.id
# # UUID('0be1a457-d7cd-44a3-af84-9583d46d1c2b')

# new_artist.fk_quotation
# # <Quotation: [Quotation] (0be1a457-d7cd-44a3-af84-9583d46d1c2b) {'_state': <django.db.models.base.ModelState object at 0x7fdf7c220ac0>, 'id': UUID('0be1a457-d7cd-44a3-af84-9583d46d1c2b'), 'created_at': datetime.datetime(2021, 10, 16, 17, 17, 59, 379870, tzinfo=<UTC>), 'updated_at': datetime.datetime(2021, 10, 16, 17, 17, 59, 379927, tzinfo=<UTC>), 'size': '50', 'body_part': 'back', 'style': 'neotraditional', 'total_time': 0, 'total_price': 0}>

# quotation1.artist.all()
# # <QuerySet [<Artist: [Artist] (904ed5db-5e87-44d2-9ebf-e321ef1ebe01) {'_state': <django.db.models.base.ModelState object at 0x7fdf7c1c7a30>, 'id': UUID('904ed5db-5e87-44d2-9ebf-e321ef1ebe01'), 'created_at': datetime.datetime(2021, 10, 16, 17, 34, 47, 336217, tzinfo=<UTC>), 'updated_at': datetime.datetime(2021, 10, 16, 17, 34, 47, 336310, tzinfo=<UTC>), 'name': 'kat', 'lastname': 'Gomez', 'mail': '123@gmail.com', 'phone': InvalidPhoneNumber(raw_input=0123456789), 'address': 'calle por ahi', 'fk_quotation_id': UUID('5fc7e0d3-a4b7-48cb-8a5a-4fea3c4d81ab')}>]>

# Quotation.objects.all()
# # <QuerySet [<Quotation: [Quotation] (5fc7e0d3-a4b7-48cb-8a5a-4fea3c4d81ab) {'_state': <django.db.models.base.ModelState object at 0x7fdf7c1c7be0>, 'id': UUID('5fc7e0d3-a4b7-48cb-8a5a-4fea3c4d81ab'), 'created_at': datetime.datetime(2021, 10, 16, 17, 5, 57, 725803, tzinfo=<UTC>), 'updated_at': datetime.datetime(2021, 10, 16, 17, 5, 57, 725839, tzinfo=<UTC>), 'size': 10, 'body_part': 'cuello', 'style': 'black work', 'total_time': 20, 'total_price': Decimal('3.00')}>, <Quotation: [Quotation] (0be1a457-d7cd-44a3-af84-9583d46d1c2b) {'_state': <django.db.models.base.ModelState object at 0x7fdf7c1c76a0>, 'id': UUID('0be1a457-d7cd-44a3-af84-9583d46d1c2b'), 'created_at': datetime.datetime(2021, 10, 16, 17, 17, 59, 379870, tzinfo=<UTC>), 'updated_at': datetime.datetime(2021, 10, 16, 17, 17, 59, 379927, tzinfo=<UTC>), 'size': 50, 'body_part': 'back', 'style': 'neotraditional', 'total_time': 0, 'total_price': Decimal('0.00')}>]>

# Artist.objects.filter(fk_quotation__style='black work')
# # <QuerySet [<Artist: [Artist] (904ed5db-5e87-44d2-9ebf-e321ef1ebe01) {'_state': <django.db.models.base.ModelState object at 0x7fdf7c1c7bb0>, 'id': UUID('904ed5db-5e87-44d2-9ebf-e321ef1ebe01'), 'created_at': datetime.datetime(2021, 10, 16, 17, 34, 47, 336217, tzinfo=<UTC>), 'updated_at': datetime.datetime(2021, 10, 16, 17, 34, 47, 336310, tzinfo=<UTC>), 'name': 'kat', 'lastname': 'Gomez', 'mail': '123@gmail.com', 'phone': InvalidPhoneNumber(raw_input=0123456789), 'address': 'calle por ahi', 'fk_quotation_id': UUID('5fc7e0d3-a4b7-48cb-8a5a-4fea3c4d81ab')}>]>

# Artist.objects.all()
# # <QuerySet [<Artist: [Artist] (904ed5db-5e87-44d2-9ebf-e321ef1ebe01) {'_state': <django.db.models.base.ModelState object at 0x7fdf7c1c7ac0>, 'id': UUID('904ed5db-5e87-44d2-9ebf-e321ef1ebe01'), 'created_at': datetime.datetime(2021, 10, 16, 17, 34, 47, 336217, tzinfo=<UTC>), 'updated_at': datetime.datetime(2021, 10, 16, 17, 34, 47, 336310, tzinfo=<UTC>), 'name': 'kat', 'lastname': 'Gomez', 'mail': '123@gmail.com', 'phone': InvalidPhoneNumber(raw_input=0123456789), 'address': 'calle por ahi', 'fk_quotation_id': UUID('5fc7e0d3-a4b7-48cb-8a5a-4fea3c4d81ab')}>, <Artist: [Artist] (5e447934-0d3e-4819-b34b-2fcb5a9a059f) {'_state': <django.db.models.base.ModelState object at 0x7fdf7c120040>, 'id': UUID('5e447934-0d3e-4819-b34b-2fcb5a9a059f'), 'created_at': datetime.datetime(2021, 10, 16, 17, 51, 38, 64459, tzinfo=<UTC>), 'updated_at': datetime.datetime(2021, 10, 16, 17, 51, 38, 64487, tzinfo=<UTC>), 'name': 'Fabrizio', 'lastname': 'Maurizi', 'mail': 'fbm@gmail.com', 'phone': InvalidPhoneNumber(raw_input=010646469), 'address': 'Italy', 'fk_quotation_id': UUID('0be1a457-d7cd-44a3-af84-9583d46d1c2b')}>]>

# Artist.objects.filter(name='Fabrizio')
# # <QuerySet [<Artist: [Artist] (5e447934-0d3e-4819-b34b-2fcb5a9a059f) {'_state': <django.db.models.base.ModelState object at 0x7fdf7c1c7fa0>, 'id': UUID('5e447934-0d3e-4819-b34b-2fcb5a9a059f'), 'created_at': datetime.datetime(2021, 10, 16, 17, 51, 38, 64459, tzinfo=<UTC>), 'updated_at': datetime.datetime(2021, 10, 16, 17, 51, 38, 64487, tzinfo=<UTC>), 'name': 'Fabrizio', 'lastname': 'Maurizi', 'mail': 'fbm@gmail.com', 'phone': InvalidPhoneNumber(raw_input=010646469), 'address': 'Italy', 'fk_quotation_id': UUID('0be1a457-d7cd-44a3-af84-9583d46d1c2b')}>]>

# Quotation.objects.filter(artist__name='Fabrizio')
# # <QuerySet [<Quotation: [Quotation] (0be1a457-d7cd-44a3-af84-9583d46d1c2b) {'_state': <django.db.models.base.ModelState object at 0x7fdf7c1c7a90>, 'id': UUID('0be1a457-d7cd-44a3-af84-9583d46d1c2b'), 'created_at': datetime.datetime(2021, 10, 16, 17, 17, 59, 379870, tzinfo=<UTC>), 'updated_at': datetime.datetime(2021, 10, 16, 17, 17, 59, 379927, tzinfo=<UTC>), 'size': 50, 'body_part': 'back', 'style': 'neotraditional', 'total_time': 0, 'total_price': Decimal('0.00')}>]>



#PRUEBA POST PARA POSTMAN
# { 
#     "artist_id": { 
#         "id" : "02de5769-9926-41d5-9a6e-afe207911ed6"
#     }, 

#     "user": {
#         "name": "Kathe test",
#         "mail": "kathe@gmail.com",
#         "phone": "3146614389"
#         },
#     "quotation": {
#         "style": "black",
#         "body_part": "brazo",
#         "size": "26",
#         "description": "Quiero algo bien bonito" 
#         }
#     } 
