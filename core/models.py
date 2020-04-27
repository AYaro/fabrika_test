from fabrika.base import BaseModel
from django.db import models

class App(BaseModel):
    name = models.TextField(null=True)
    api = models.TextField(null=True)
