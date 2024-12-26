from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveUpdateAPIView, UpdateAPIView
from common import serializers
from common import models
from helpers import pagination
from rest_framework.permissions import AllowAny
from rest_framework.parsers import MultiPartParser

class CeoReviewAPIView(ListAPIView):
    queryset = models.CeoReview.objects.all()
    serializer_class  = serializers.CeoReviewSerializers
    pagination_class = pagination.ByOne
    lookup_field = 'pk'



class CeoReviewAPICreate(CreateAPIView):
    queryset = models.CeoReview.objects.all()
    serializer_class  = serializers.CeoReviewSerializers
    permission_classes = [AllowAny]  
    parser_classes = (MultiPartParser,)
  


class CeoReviewAPIUpdate(RetrieveUpdateAPIView):
    queryset = models.CeoReview.objects.all()
    serializer_class  = serializers.CeoReviewSerializers
    pagination_class = None
    parser_classes = (MultiPartParser,)
    lookup_field = 'pk'



class CeoReviewAPIDestroy(DestroyAPIView):
    queryset = models.CeoReview.objects.all()
    serializer_class  = serializers.CeoReviewSerializers
    lookup_field = 'pk'
    permission_classes = (AllowAny, )




class TwitterAPIView(ListAPIView):
    queryset = models.Twitter.objects.all()
    serializer_class  = serializers.TwitterSerializers
    pagination_class = None



class EventAPIView(ListAPIView):
    queryset = models.Event.objects.all()
    serializer_class  = serializers.EventSerializers
    pagination_class = None


class StatisticsAPIView(ListAPIView):
    queryset = models.Statistics.objects.all()
    serializer_class  = serializers.StatisticsSerializers
    pagination_class = None


class FlavoursAPIView(ListAPIView):
    queryset = models.Flavours.objects.all()
    serializer_class  = serializers.FlavoursSerializers
    pagination_class = None



class AwardsAPIView(ListAPIView):
    queryset = models.Awards.objects.all()
    serializer_class = serializers.AwardsSerializers
    pagination_class = None



class BlogAPIView(ListAPIView):
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializers
    pagination_class = None


class DepartamentAPIView(ListAPIView):
    queryset = models.Departament.objects.all()
    serializer_class = serializers.DepartamentSerializers
    pagination_class = None


class CareerAPIView(ListAPIView):
    queryset = models.Career.objects.all()
    serializer_class = serializers.CareerSerializers
    pagination_class = None


class ApplicationAPIView(ListAPIView):
    queryset = models.Application.objects.all()
    serializer_class = serializers.ApplicationSerializers
    pagination_class = None


class ContactAPIView(CreateAPIView):
    queryset = models.Contact.objects.all()
    seriazlier_class = serializers.ContactSerializers
    pagination_class = None

# class ContactAPIDestroy(DestroyAPIView):
#     queryset = models.Contact.objects.all().order_by("-id")
#     seriazlier_class = serializers.ContactSerializers
#     pagination_class = None


class ContactDetailsAPIView(ListAPIView):
    queryset = models.ContactDetails.objects.all()
    seriazlier_class = serializers.ContactDetailsSerializers
    pagination_class = None



class FaqAPIView(ListAPIView):
    queryset = models.Faq.objects.all()
    seriazlier_class = serializers.FaqSerializers
    pagination_class = None



class NewsAPIView(ListAPIView):
    queryset = models.News.objects.all()
    seriazlier_class = serializers.NewsSerializers
    pagination_class = None



class PartnersAPIView(ListAPIView):
    queryset = models.Partners.objects.all()
    seriazlier_class = serializers.PartnersSerializers
    pagination_class = None



class ProductAPIView(ListAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializers
    pagination_class = None


class ProductTypesAPIView(ListAPIView):
    queryset = models.ProductTypes.objects.all()
    seriazlier_class = serializers.ProductTypesSerializers
    pagination_class = None
    parser_classes = (MultiPartParser,)

    def get_serializer_class(self):
        return serializers.ProductTypesSerializers



class IngredientsAPIView(ListAPIView):
    queryset = models.Ingredients.objects.all()
    seriazlier_class = serializers.IngredientsSerializers
    pagination_class = None

