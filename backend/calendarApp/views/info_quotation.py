""" Module containing info_quotation module """

from api_quotation.models.model_artist import Artist
from api_quotation.models.model_quotation import Quotation
from api_quotation.models.model_user import User


#id_prueba = "c6d08140-ec2e-403a-9bcf-187ff68fa47f" -> Mi base de datos
def info_quotation(id_quotation):
    """Function to retrieve quotation information from database

    Args:
        id_quotation (str): quotation id to get object quoatition from database

    Returns:
        dict: quotation information
    """
    quotation = Quotation.objects.filter(id = id_quotation)

    id_artist = quotation.values('fk_artist')[0]['fk_artist']

    artist = Artist.objects.filter(id = id_artist)

    id_user = quotation.values('fk_user')[0]['fk_user']

    user = User.objects.filter(id = id_user)

    calendar_data = {"user_data": user, "quotation_data": quotation, "artist_data": artist}

    return calendar_data
    #Query set objects
