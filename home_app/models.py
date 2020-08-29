from django.db import models
# from .forms import CreateUserForm

# Create your models here.


class Product(models.Model):
    pro_id = models.IntegerField()
    pro_img = models.ImageField
    pro_desc = models.CharField(max_length=150)
    pro_price = models.IntegerField()

    class Meta:
        db_table = "product"


class UserGroup(Product):
    is_admin = models.BooleanField()
    is_customer = models.BooleanField()

    def __str__(self):
        return self.pro_id


class UserAdmin(models.Model):
    user = models.OneToOneField(UserGroup, on_delete=models.CASCADE)
