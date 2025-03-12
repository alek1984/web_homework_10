from mongoengine import Document, StringField, ListField, ReferenceField

class Author(Document):
    full_name = StringField(required=True, unique=True)
    birth_date = StringField()
    birth_place = StringField()
    description = StringField()

class Quote(Document):
    author = ReferenceField(Author, required=True)
    text = StringField(required=True)
    tags = ListField(StringField())
