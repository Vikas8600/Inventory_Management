from django.db import models

# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length=30)
    location_id = models.CharField(max_length=20, primary_key=True,default=0)

    def __str__(self):
        return self.location


class Product(models.Model):
    name = models.CharField(max_length=30)
    product_id = models.CharField(max_length=20, primary_key=True,default=0)
    pro_qty = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class ProductMovement(models.Model):
    movement_id = models.IntegerField(primary_key=True)
    from_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='Location_at',blank=True, null=True)
    to_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='Location_to_be',blank=True, null=True)
    p_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ProductMovement')
    timestamp = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(null=False)


    # def __str__(self):
    #     return '{} - {} : ID = {}'.format(self.from_location, self.to_location, self.movement_id)
