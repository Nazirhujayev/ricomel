from django.urls import path
from  common import views

urlpatterns = [
    path("ceo-review/", views.CeoReviewAPIView.as_view(), name="ceo-review"),
    path("ceo-review/create", views.CeoReviewAPICreate.as_view(), name="ceo-review-create"),
    path('ceo-review/update/<int:pk>/', views.CeoReviewAPIUpdate.as_view(), name='ceo-review-update'),
    path('ceo-review/delete/<int:pk>/', views.CeoReviewAPIDestroy.as_view(), name='ceo-review-delete'),
    path("twitter/", views.TwitterAPIView.as_view(), name="twitter"),
    path("event/", views.EventAPIView.as_view(), name="event"),
    path("statistics/", views.StatisticsAPIView.as_view(), name="statistics"),
    path("flavours/", views.FlavoursAPIView.as_view(), name="flavours"),
    path("awards/", views.AwardsAPIView.as_view(), name="awards"),
    path("blog/", views.BlogAPIView.as_view(), name="blog"),
    path("departament/", views.DepartamentAPIView.as_view(), name="departament"),
    path("career/", views.CareerAPIView.as_view(), name="career"),
    path("application/", views.ApplicationAPIView.as_view(), name="application"),
    path("contact/", views.ContactAPIView.as_view(), name="contact"),
    # path("contact-destroy/", views.ContactAPIDestroy.as_view(), name="contact-destroy"),
    path("contact-details/", views.ContactDetailsAPIView.as_view(), name="contact-details"),
    path("faq/", views.FaqAPIView.as_view(), name="faq"),
    path("news/", views.NewsAPIView.as_view(), name="news"),
    path("partners/", views.PartnersAPIView.as_view(), name="partners"),
    path("product/", views.ProductAPIView.as_view(), name="product"),
    path("product-type/", views.ProductTypesAPIView.as_view(), name="product-type"),
    path("ingredients/", views.IngredientsAPIView.as_view(), name="ingredients"),

]
