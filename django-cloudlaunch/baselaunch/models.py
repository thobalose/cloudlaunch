# import datetime
# from bson import ObjectId
from django.template.defaultfilters import slugify
# from mongoengine import DateTimeField
from mongoengine import Document
# from mongoengine import EmbeddedDocument
# from mongoengine import EmbeddedDocumentField
from mongoengine import ListField
from mongoengine import ReferenceField
from mongoengine import StringField
from mongoengine import URLField
# from mongoengine.django.auth import User


class Image(Document):
    name = StringField(max_length=50)
    image_id = StringField(max_length=50, required=True)
    description = StringField()
#     infrastructure = ReferenceField(Infrastructure)


class Category(Document):
    name = StringField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Application(Document):
    name = StringField(max_length=60, required=True, unique_with='version')
    slug = StringField(max_length=70)
    version = StringField(max_length=30)
    description = StringField()
    info_url = URLField()
    # categories = ListField(EmbeddedDocumentField(Category))
    categories = ListField(ReferenceField('Category'))
    # image = ReferenceField(Image)
    # user = ReferenceField(User)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Application, self).save(*args, **kwargs)

    def __str__(self):
        return "{0} ({1})".format(self.name, self.version)
