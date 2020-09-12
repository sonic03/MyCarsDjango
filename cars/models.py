from django.db import models

class Marka(models.Model):
    markaName = models.CharField(max_length=120,verbose_name="marka")

    def __str__(self):
        return self.markaName


class Model(models.Model):
    modelName = models.CharField(max_length=120, verbose_name="model")

    def __str__(self):
        return self.modelName


class Gear(models.Model):
    gearName = models.CharField(max_length=120, verbose_name="Vites")

    def __str__(self):
        return self.gearName



class GetMyCars(models.Model):
    title=models.CharField(max_length=120,verbose_name="Başlık")
    owner=models.ForeignKey("auth.User",verbose_name="Kullanıcı",on_delete=models.CASCADE)

    marka=models.ForeignKey(Marka,on_delete=models.CASCADE,verbose_name="Marka")
    model = models.ForeignKey(Model, on_delete=models.CASCADE, verbose_name="Model")
    content=models.TextField()
    km=models.IntegerField(verbose_name="Kilometre")
    add_date=models.DateTimeField(auto_now_add=True)
    gear = models.ForeignKey(Gear, on_delete=models.CASCADE, verbose_name="Vites")
    price=models.IntegerField(verbose_name="Fiyat")
    carYear=models.IntegerField(verbose_name="Yıl")
    car_img1=models.FileField(blank=True,null=True,verbose_name="Görsel")
    car_img2 = models.FileField(blank=True, null=True, verbose_name="Görsel")
    car_img3 = models.FileField(blank=True, null=True, verbose_name="Görsel")
    car_img4 = models.FileField(blank=True, null=True, verbose_name="Görsel")

    def __str__(self):
        return self.title
