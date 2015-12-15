from bson import ObjectId
from django.template.defaultfilters import slugify
from mongoengine import Document
# from mongoengine import ReferenceField
from mongoengine import StringField


class Image(Document):
    name = StringField(max_length=50)
    image_id = StringField(max_length=50, required=True)
    description = StringField()
#     infrastructure = ReferenceField(Infrastructure)


class Category(Document):
    name = StringField(max_length=50)


class Application(Document):
    app_id = StringField()
    name = StringField(max_length=60, required=True)
    slug = StringField(max_length=70)
    version = StringField(max_length=30)
    description = StringField()
    info_url = StringField()
    # categories = ReferenceField(Category)
    # image = ReferenceField(Image)

    def save(self, *args, **kwargs):
        if self.app_id is None:
            self.app_id = str(ObjectId())
        self.slug = slugify(self.name)
        return super(Application, self).save(*args, **kwargs)
