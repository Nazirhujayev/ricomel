from rest_framework import serializers

from common import models 

class CeoReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.CeoReview
        fields = ['id', "full_name", "position", "image", "signature", "comment"]


class TwitterSerializers(serializers.ModelSerializer):
   class Meta:
       model = models.Twitter
       fields = ["tweet", "url"] 



class EventSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Event
        fields = ['id', "title", "location", "content", "date"]



class StatisticsSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Statistics
        fields = ['id', "description","video", "sold", "sold_year", "stores", "team" , "established_year"]



class FlavoursSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Flavours
        fields = ['id', "product", "flavour", "order"]




class AwardsSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Awards
        fields = ['id', "file", "order", "url"]


class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BlogCategory
        fields = ('id', 'title', 'slug', 'cover')



class BlogSerializers(serializers.ModelSerializer):
    # category = serializers.StringRelatedField
    category = BlogCategorySerializer() # if m2m (manyto)
    class Meta:
        model = models.Blog
        fields = ['id', "title", "slug", "cover", 'category', "image" , "content", "published_at"]



class DepartamentSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Departament
        fields = ["title"]
        


class CareerSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Career
        fields = ['id', "title", "salary", "salary_type", "location", "content", "departament","from_day", "to_day", "from_time", "job_type"]



class ApplicationSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Application
        fields = ['id', "name", "phone_regex", "phone", "file"]




class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model  = models.Contact
        fields = ['id', "full_name", "email", "message"]



class ContactDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model  = models.ContactDetails
        fields = ['id', "title", "description", "phone", "email", "twitter", "facebook", "telegram", "instagram"]


class FaqSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Faq
        fields = ['id', "question", "answer", "active"]



class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.News
        fields = ['id', "title", "slug", "cover", "image", "content", "published_at"]



class PartnersSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Partners
        fields = ['id', "file", "order"]


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ['id', "title", "description", "color", "hover", "image_center", "image_left" ,"image_right"]




class ProductTypesSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.ProductTypes
        fields= ['id', "title", "description", "price", "color", "hover", "image_main", "image_first", "image_second", "image_third","order", "facts", "buy_now_link"]




class IngredientsSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Ingredients
        fields = ['id', "product", "title", "description", "file"]

