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
    image = models.ImageField(upload_to='constructions/images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    subway_station_location = models.ForeignKey("SubwayStation", on_delete=models.CASCADE, default=None, null=True, blank=True)
    threedimage = models.ForeignKey("ConstructionThreeDImage", on_delete=models.CASCADE, default=None, null=True, blank=True)
    def __str__(self):
        return self.name
    



    def getLocationNumbers(self):
        return self.subway_station_location.getLocationNumbers




class Order(models.Model):
    # name = models.CharField(max_length=200,blank=True, null=True)
    construction = models.ForeignKey(Construction, on_delete=models.CASCADE)
    # user = models.Foreig
    from_date = models.DateTimeField(auto_now_add=True)
    to_date =  models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


class ConstructionThreeDImage(models.Model):
    # construction = models.ForeignKey(Construction, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='construction_three_d_images/')
    neighbours = models.ManyToManyField("self", blank=True, symmetrical=False)
    name = models.CharField(max_length=200,blank=True, null=True)

    def __str__(self):
        return self.name if self.name else self.image.name
    


class SubwayStation(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    addressformatted = models.CharField(max_length=500)
    def __str__(self):
        return self.name
    



    def getLocationNumbers(self):
        return {
            "Lat": self.latitude,
            "Long": self.longitude,
            "AddressFormatted": self.addressformatted
        }

    
