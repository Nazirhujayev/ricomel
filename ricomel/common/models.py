from django.conf import settings
from django.core.validators import FileExtensionValidator, RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy
from django_resized import ResizedImageField
from ckeditor_uploader.fields import RichTextUploadingField
from helpers.models import BaseModel
from django.utils import timezone
from colorfield.fields import ColorField
import os

class CeoReview(BaseModel):
    full_name = models.CharField("Toliq_ism", max_length=256)
    position = models.CharField("Lavozim", max_length=256)
    image = models.ImageField("Rasmi", upload_to="ceoreview/")
    signature = models.ImageField(("imzo"),
        validators=[FileExtensionValidator(["png","svg","jpg","jpeg"])],
        upload_to ="ceo/%Y/%m"
    )
    comment = models.TextField("Tavsif")

    def __str__(self):
        return f"{self.full_name}"
    
    @property
    def image_url(self):
        return f"{settings.HOST}{self.image.url}" if self.image else""
    
    @property
    def signature_url(self):
        return f"{settings.HOST}{self.signature.url}" if self.signature else ""
    
    class Meta:
        db_table = "ceo_review"
        verbose_name = "Kompaniya egasi tavsiya"
        verbose_name_plural ="Kompaniya egasi tavsifi"


class Twitter(BaseModel):
    tweet = models.TextField("Twit")
    url = models.CharField("Havola", max_length=256)

    def __str__(self):
        return f"{self.tweet}"
    
    class Meta:
        db_table = "twitter"
        verbose_name = "twitter"
        verbose_name_plural = "Twitter"



class Event(BaseModel):
    title = models.CharField("Nomi", max_length=256)
    location = models.CharField("Joylashuvi", max_length=256)
    content = RichTextUploadingField(("Kontent"))
    date = models.DateTimeField(
        ("Sanasi"),
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        db_table = "events"
        verbose_name = "Munim voqea"
        verbose_name_plural =  "Muhim voqealar"
    

class Statistics(BaseModel):
    description = models.TextField("Tavsif", max_length=256)
    video = models.CharField("Video links", max_length=256)
    sold = models.BigIntegerField("Sotilgan mahsulotlar soni")
    sold_year = models.DateField("Sotilgan yil")
    stores = models.IntegerField("Rastalar soni")
    team = models.IntegerField("Jamoa a'zolari soni")
    established_year = models.DateField("Asos solinga yil")
     
    def __str__(self):
        return f"{self.description}"

    class Meta:
        db_table = "statistics"
        verbose_name = "Statistika"
        verbose_name_plural = "Statistika"


class Flavours(BaseModel):
    product = models.CharField("Mahsulot nomi", max_length=256)
    flavour = models.CharField("Ta'mlari", max_length=256)
    order = models.SmallIntegerField("Tartibi", default=0)

    def __str__(self):
        return f"{self.product}"


    class Meta:
        db_table = "flavours"
        verbose_name = "Ta'm"
        verbose_name_plural = "Ta'mlar"


class Awards(BaseModel):
    file = models.FileField(
        'Sertificat',
        validators=[FileExtensionValidator(['png','svg','jpg','jpeg'])],
        upload_to= "awards%Y%m"
    )
    order = models.IntegerField("Tartibi", default=0)
    url = models.CharField("Havol", max_length=256)


    def __str__(self):
        return f"{self.file.name}"
    
    @property
    def file_url(self):
        return f"{settings.HOST}{self.file.url}" if self.file else ""
    

    class Meta:
        db_table = "awards"
        verbose_name = "Xalqaro mukofot va sertifikat"
        verbose_name_plural = "Xalqaro mukofat va sertifikatlar"


class BlogCategory(BaseModel):
    title = models.CharField("nomi", max_length=50)
    slug = models.SlugField("Slug", max_length=256)
    cover = ResizedImageField(
        "Rasm", size=[200,195],  crop=["middle", "center"], upload_to = "blog%Y%M"
    )

    @property
    def cover_url(self):
        return f"{settings.HOST}{self.cover.url}" if self.cover else ""


class Blog(BaseModel):
    title = models.CharField("Nomi", max_length=256)
    slug = models.SlugField("Slug", max_length=256)
    category = models.ForeignKey("common.BlogCategory",on_delete=models.CASCADE)
    cover = ResizedImageField(
        "Rasm", size=[200,195],  crop=["middle", "center"], upload_to = "blog%Y%M"
    )
    image = ResizedImageField(
        "rasm", size = [890,480], crop=["middle", "center"], upload_to = "blog%Y%m"
    )
    content = RichTextUploadingField ("Kontent")
    published_at = models.DateField("Nashr qilingan sana", default=timezone.now)
    
    def __str__(self):
        return f"{self.title}"

    @property
    def image_url(self):
        return f"{settings.HOST}{self.image.url}" if self.image else ""
    @property
    def cover_url(self):
        return f"{settings.HOST}{self.cover.url}" if self.cover else ""
    
    class Meta:
        db_table = "blog"
        verbose_name = "Blog post"
        verbose_name_plural = "Blog Postlar"
        

class Departament(BaseModel):
    title = models.CharField("Nomi", max_length=256)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        db_table = "departament"
        verbose_name = "Bo'lim"
        verbose_name_plural = "Bo'limlar"



class JobTypeChoices(models.IntegerChoices):
    full_time = 1, ("To'liq stavka")
    part_time = 2, ("Yarim stavka")




class WeekdayChoices(models.IntegerChoices):
    monday = 1, ("Dushanba")
    tuesday = 2, ("Seshanba")
    wendesday = 3, ("Chorshanba")
    thursday = 4, ("Payshanba")
    friday = 5, ("Juma")
    saturday = 6, ("Shanba")
    sunday = 7, ("Yakshanba")



class SalaryTypeChoices(models.IntegerChoices):
    fixed = 1, ("Belgilanga")
    by_interview = 2, ("Kelishiladi")


class Career(BaseModel):
    title = models.CharField("Nomi", max_length=256)
    salary = models.IntegerField("Maosh", default=8)
    salary_type = models.IntegerField("Maosh turi", choices=SalaryTypeChoices.choices, default=1)
    location = models.CharField("Joylashuv", max_length=256)
    content = RichTextUploadingField ("Kontent")
    departament = models.ForeignKey(
        Departament, on_delete=models.CASCADE, related_name="careers", verbose_name="Bo'lim"
    )
    from_day = models.IntegerField(
        "Ish boshlanish kuni", choices=WeekdayChoices.choices, default=1)
    to_day = models.IntegerField("ish tugash kuni", choices=WeekdayChoices.choices, default=6)
    from_time = models.TimeField("ish boshlanish vaqti")
    job_type = models.IntegerField("ish turi", choices=JobTypeChoices.choices, default=1)

    def __str__(self):
        db_table = "career"
        verbose_name = "Vakansiya"
        verbose_name_plural = "Vakansiyalar"


class Application(BaseModel):
    name = models.CharField("Ismi", max_length=256)
    phone_regex = RegexValidator("regex=r^\d{9}$", message="wrong_phone_format")
    phone = models.CharField(
        validators=[phone_regex], verbose_name=("Telefon raqami"), max_length=9
    )
    file = models.FileField(
        "Rezyume", validators=[FileExtensionValidator(["pdf", "docx", ])], upload_to="file/%Y%m"
    )
    def __str__(self):
        return f"{self.name}"
    
    def filename(self):
        return os.path.basename(self.file.name)
    
    class Meta:
        db_table = "application"
        verbose_name = "Ariza"
        verbose_name_plural = "Arizalar"


class Contact(BaseModel):
    full_name = models.CharField("Ism familiya", max_length=256)
    email = models.EmailField("Email", max_length=256)
    message = models.TextField("message")

    def __str__(self):
        return f"{self.full_name}"


    class Meta:
        db_table = "contact"
        verbose_name = "Aloqa"
        verbose_name_plural = "Aloqalar"


class ContactDetails(BaseModel):
    title = models.CharField("ism/Nomi", max_length=256)
    description = models.TextField("Tavsif")
    phone = models.CharField("Telefon raqami", max_length=256)
    email = models.EmailField("Email", blank=True)
    twitter = models.CharField("Twitter havolasi", max_length=256)
    facebook = models.CharField("Facebook havolasi", max_length=256)
    telegram  = models.CharField("Telegram havolasi", max_length=256)
    instagram = models.CharField("instgram havolasi", max_length=256)


    def __str__(self):
        return f"{self.title}"
    

    class Meta:
        db_table = "contact_details"
        verbose_name = "Kontakt ma'lumot"
        verbose_name_plural = "Kontakt ma'lumotlari"


class Faq(BaseModel):
    question = models.TextField("Savol")
    answer = models.TextField("Javob")
    active = models.BooleanField(default=True)


    def __str__(self):
        return  f"{self.question}"
    
    class Meta:
        db_table = "faq"
        verbose_name = "F.A.Q"
        verbose_name_plural = "F.A.Q"


class News(BaseModel):
    title = models.CharField("Nomi", max_length=256)
    slug = models.SlugField("Slug", max_length=256)
    cover = ResizedImageField(
        "Rasm", size=[200,195],  crop=["middle", "center"], upload_to = "news%Y%M"
    )
    image = ResizedImageField(
        "rasm", size = [890,480], crop=["middle", "center"], upload_to = "news%Y%m"
    )
    content = RichTextUploadingField ("Kontent")
    published_at = models.DateField("Nashr qilingan sana", default=timezone.now)
    
    def __str__(self):
        return f"{self.title}"

    @property
    def image_url(self):
        return f"{settings.HOST}{self.image.url}" if self.image else ""
    @property
    def cover_url(self):
        return f"{settings.HOST}{self.cover.url}" if self.cover else ""
    
    class Meta:
        db_table = "news"
        verbose_name = "news post"
        verbose_name_plural = "news Postlar"
        


class Partners(BaseModel):
    file = models.FileField(
        ("logo"),
        validators=[FileExtensionValidator(["png", "svg", "jpg", "jpeg"])],
        upload_to= "partners/%Y/%m"
    )

    order = models.IntegerField("Tartibi", default=8)

    def __str__(self):
        return f"{self.file.name}"
    
    
    @property
    def file_url(self):
        return f"{settings.HOST}{self.file.url}" if self.file else ""
    
    class Meta:
        db_table = "partners"
        verbose_name = "Hamkor"
        verbose_name_plural = "Hamkorlar"



class Product(BaseModel):
    title = models.CharField("Nomi", max_length=256)
    description = models.TextField("Tavsif",max_length=256)
    color = ColorField("Rangi")
    hover = ColorField("hover")
    image_center = models.ImageField("Asosiy rasm", upload_to="product/%Y%m")
    image_left = models.ImageField("Birinchi rasm", upload_to="product/%y/%m")
    image_right = models.ImageField("Ikkinchi rasm", upload_to="product/top/%Y%m")

    def __str__(self):
        return f"{self.title}"
    
    def __str__(self):
        return f"{settings.HOST}{self.image_center.url}" if self.image.url else ""
    
    
    def __str__(self):
        return f"{settings.HOST}{self.image_right.url}" if self.image_right.url else ""
    
    
    def __str__(self):
        return f"{settings.HOST}{self.image_left.url}" if self.image.left.url else ""
    

    class Meta:
        db_table = "product"
        verbose_name = "Asosiy mahsulot"
        verbose_name_plural = "Asosiy mahsulotlar"



class ProductTypes(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_type", verbose_name = "Mahuslot04")
    title = models.CharField("Nomi", max_length=256)
    description = models.TextField("Tavsif")
    price = models.IntegerField("Naxi")
    color = ColorField("Rangi")
    hover = ColorField("hover")
    image_main = models.ImageField("Asosiy rasm", upload_to="product/%Y%m")
    image_first = models.ImageField("Birinchi rasm", upload_to="product/%Y%m")
    image_second = models.ImageField("Ikkinchi rasm", upload_to="product/%y/%m")
    image_third = models.ImageField("Uchinchi rasm", upload_to="product/top/%Y%m")
    order = models.IntegerField("Tartib raqami", default=0)
    facts = RichTextUploadingField ("Faktlar")
    buy_now_link = models.CharField("Faktlar", max_length=256, blank=True)

    def __str__(self):
        return f"{self.title}"
    
    def image_main_url(self):
        return f"{settings.HOST}{self.image_main_url}" if self.image_main else ""
    
    class Meta:
        ordering = ("order",)
        db_table = "product_types"
        verbose_name = "Mahsulot turi"
        verbose_name_plural = "Mahsulot turlari"



class Ingredients(BaseModel):
    product = models.ForeignKey(ProductTypes, on_delete=models.CASCADE, related_name="inggredients", verbose_name="Mahsulot")
    title  = models.CharField("Nomi", max_length=256)
    description = RichTextUploadingField ("Tavsif", null=True)
    file = models.FileField(
        ("icon"), validators=[FileExtensionValidator(["svg"])], upload_to="ingredients/%Y/%m"
    )

    def __str__(self):
        return f"{self.title}"
    
    def file_url(self):
        return f"{settings.HOST}{self.file.url}" if self.file else ""
    
    class Meta:
        db_table = "ingredients"
        verbose_name = "ingredients"
        verbose_name_plural = "ingredients"
