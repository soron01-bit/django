from django.db import models
from django.utils import timezone

class product(models.Model):
    PRODUCT_STATUS = (
        ('available', 'Available'),
        ('unavailable', 'Unavailable')
    )
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    description = models.TextField()
    status = models.CharField(max_length=20, choices=PRODUCT_STATUS, default='available')
    created_at = models.DateTimeField(default=timezone.now) 

    def __str__(self):
        return self.name
    
    class productReview(models.Model):
        product = models.ForeignKey(product, on_delete=models.CASCADE, related_name='reviews')
        rating = models.IntegerField()
        comment = models.TextField()
        reting = models.IntegerField(max_value=5, min_value=1)
        comment = models.TextField() 
        created_at = models.DateTimeField(default=timezone.now)

        def __str__(self):
            return f"Product: {self.product.name} - User: {self.user.username} - Rating: {self.rating}"
        
        #many to many rltn
        class Store(models.Model):
            name = models.CharField(max_length=100)
            products = models.CharField(max_length=100)
            product_varities = models.ManyToManyField(product, related_name='stores')

            def __str__(self):
                return self.name
            
            #one to one rltn
            class productCertificate(models.Model):
                product = models.OneToOneField(product, on_delete=models.CASCADE, related_name='certificate')
                certificate_number = models.CharField(max_length=100)
                issued_date = models.DateTimeField()
                expiry_date = models.DateTimeField()

                def __str__(self):
                    return f"Certificate for {self.product.name}"