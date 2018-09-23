from tortoise.models import Model
from tortoise import fields


class MyModel(Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()
