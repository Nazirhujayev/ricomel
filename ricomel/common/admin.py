from django.contrib import admin
from common import models 
@admin.register(models.CeoReview)
class CeoReviewAdmin(admin.ModelAdmin):
    list_display = ["full_name",]


@admin.register(models.Twitter)
class CeoReviewAdmin(admin.ModelAdmin):
    list_display = ["tweet",]

admin.site.register(models.Blog)
admin.site.register(models.BlogCategory)

