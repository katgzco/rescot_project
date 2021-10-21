from django.contrib import admin
from api_quotation.models.model_artist import Artist
from api_quotation.models.model_styles import Styles
from api_quotation.models.model_quotation import Quotation
from api_quotation.models.model_user import User
from api_quotation.models.model_body import Body

# Register your models here.
admin.site.register(Artist)
admin.site.register(Styles)
admin.site.register(Quotation)
admin.site.register(User)
admin.site.register(Body)
