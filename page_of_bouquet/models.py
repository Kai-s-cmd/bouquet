from django.db import models


# Create your models here.
class Prices(models.Model):
    """Edit prices with admin tools"""

    card_title = models.CharField(max_length=80)
    card_text = models.CharField(max_length=500)
    button_text = models.CharField(max_length=20)

    def __str__(self):
        """Return a string representation of the model."""
        return self.card_text, self.card_text, self.button_text
