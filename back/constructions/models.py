from django.db import models

subway_statations = (
    ("Paxtakor", "Paxtakor"),
    ("Olmazor", "Olmazor"),
)


Location_Attirbutes = {
    "Paxtakor": {
        "Lat": "41.323",
        "Long": "69.334",
        "AddressFormatted":"Qaysi ko'chani, qaysidir joyi"
    },

}







# Create your models here.
class Construction(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='constructions/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    Location = models.CharField(max_length=200, choices=subway_statations, blank=False, null=True)

    

    def __str__(self):
        return self.name
    



    def getLocationNumbers(self):
        pass




class Order(models.Model):
    construction = models.ForeignKey(Construction, on_delete=models.CASCADE)
    # user = models.Foreig
    from_date = models.DateTimeField(auto_now_add=True)
    to_date =  models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username + ' - ' + self.construction.name


class ConstructionThreeDImage(models.Model):
    construction = models.ForeignKey(Construction, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='construction_three_d_images/')
    neighbours = models.ManyToManyField("self", blank=True, symmetrical=False)



    def __str__(self):
        return self.construction.name