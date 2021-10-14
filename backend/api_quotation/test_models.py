from django.db import models
import uuid


class BaseModel(models.Model):
    """[summary]

    Args:
        models ([type]): [description]
    """

    """[summary]

        Args:
            None
        """

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#        class Meta:
#            app_label = 'api_quotation'

    def __str__(self):
        return str(self.name)
