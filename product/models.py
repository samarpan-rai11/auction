from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
from taggit.managers import TaggableManager
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils import timezone

# Create your models here.

AUCTION_DURATION = [
        (3, '3 days'),
        (5, '5 days'),
        (7, '7 days')
]

STATUS_CHOICE = (
    ('process','Processing'),
    ('shipped','Shipped'),
    ('delivered','Delivered')
)

RATING = (
    (1, "⭐️"),
    (2, "⭐️⭐️"),
    (3, "⭐️⭐️⭐️"),
    (4, "⭐️⭐️⭐️⭐️"),
    (5, "⭐️⭐️⭐️⭐️⭐️"),
)


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='category_images', default='default.png')

    class Meta():
        ordering = ('name',)
        verbose_name_plural = "Categories"

    #This makes django admin readable for category
    def __str__(self):   
        return self.name
    

class Vendor(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='vendor_images', default='user-default.png')
    description = models.TextField(blank=True, null=True)

    address = models.CharField(max_length=100, default="1")
    contact = models.CharField(max_length=100, default="+123 456 789")

    authentic_rating = models.CharField(max_length=50, default="100")
    warrenty_period = models.CharField(max_length=50, default="100")

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
    


class Auctioneer(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='auctioneer_images', blank=True,default='user-default.png')
    description = models.TextField(blank=True, null=True)

    address = models.CharField(max_length=100, default="1")
    contact = models.CharField(max_length=100, default="+123 456 789")

    authentic_rating = models.CharField(max_length=50, default="100")
    warrenty_period = models.CharField(max_length=50, default="100")

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
    


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    old_price = models.DecimalField(max_digits=10, decimal_places=0,default=0)
    image = models.ImageField(upload_to='product_images', blank=False, null=False)
    
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True, related_name='vendor')
    is_sold = models.BooleanField(default=False)

    tags = TaggableManager(blank=True)
    on_stock = models.BooleanField(default=True)
    product_status = models.CharField(choices=STATUS_CHOICE, max_length=10, default="in_review")

    date = models.DateTimeField(default=timezone.now,blank=True)
    update = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.title
    
    def get_percent(self):
        new_price = (self.price/self.old_price)*100
        return new_price



class Auction(models.Model):
    categori = models.ForeignKey(Category, related_name='auctions', on_delete=models.CASCADE)

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    bid = models.DecimalField(max_digits=10, decimal_places=0)
    image = models.ImageField(upload_to='auction_images', default='default-product-image.png')

    auctioneer = models.ForeignKey(Auctioneer, on_delete=models.CASCADE, null=True, related_name='auctioneer')

    duration= models.PositiveIntegerField(choices=AUCTION_DURATION, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    auction_status = models.CharField(choices=STATUS_CHOICE, max_length=10, default="in_review")


    live = models.BooleanField(default=True)

    tags = TaggableManager(blank=True)

    date = models.DateTimeField(default=datetime.now,blank=True)
    update = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.name
    


class BidT(models.Model):
    start_time =  models.DateTimeField(auto_now=True)
    end_time =  models.DateTimeField(auto_now=False,default=datetime.now)

    auction = models.OneToOneField(Auction, on_delete=models.CASCADE, related_name="auction")

    class Meta():
        verbose_name_plural = "Bid Time"
    
    
    def __str__(self):
        return self.auction.name
    


class Bids(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    # listingid is for the id of the auction that user bids for 
    listingid = models.IntegerField()
    bid = models.IntegerField()

    class Meta():
        verbose_name_plural = "Bids"


########################## Order, Cart , Payment ###################
########################## Order, Cart , Payment ###################
########################## Order, Cart , Payment ###################


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,default=1)
    paid_status = models.BooleanField(default=False)

    order_date = models.DateTimeField(default=datetime.now,blank=True)
    order_status = models.CharField(choices=STATUS_CHOICE, max_length=30, default="processing")

    quantity = models.PositiveIntegerField(default=1)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    order_time = models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.title}"



class Auction_Win(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE,default=1)
    paid_status = models.BooleanField(default=False)

    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.auction.name}"




class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/',default='user-default.png')
    contact = models.CharField(max_length=70,default="+123 456 789", blank=True)

    is_vendor = models.BooleanField(default=False)
    is_auctioneer = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)

    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    

#####################################################################
############################ Product Review #########################
#####################################################################


class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    review = models.TextField()
    rating = models.IntegerField(choices=RATING, default=None)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.product.title
    
    def get_rating(self):
        return self.rating    


#####################################################################
########################## Coupon Code ##############################
#####################################################################

class CouponCode(models.Model):
    code = models.CharField(max_length=100)
    discount = models.IntegerField()


    def __str__(self):
        return self.code
    


class Winner(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    winner_name = models.CharField(max_length=100)
    winner_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Winner of {self.auction}: {self.winner_name}"

 
    

### This signal will automatically create instance of UserProfile when user is registerd(signup). 

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    # there is a one-to-one relationship between the User model and a UserProfile model, and profile is the related name for the one-to-one field in the User model. 
    if hasattr(instance, 'profile'):
        instance.profile.save()


post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)



##########################################################################################################################################
# these signals are there so that when Auctioneer or Vendor is deleted the userprofile of these users are also deleted
@receiver(post_delete, sender=Auctioneer)
def delete_related_user_and_profile(sender, instance, **kwargs):
    instance.user.delete()


@receiver(post_delete, sender=Vendor)
def delete_related_user_and_profile(sender, instance, **kwargs):
    instance.user.delete()



############################################################################################################################################################################################################
#This signal will automatically create instance of BidT when user creates Auction
@receiver(post_save, sender=Auction)
def bid_time(sender, instance, created, **kwargs):
    if created:
        for duration, _ in AUCTION_DURATION:
            if instance.duration == duration:
                end_time = timezone.now() + timezone.timedelta(days=duration)
                break
        else:
            raise ValueError("Invalid auction duration")

        BidT.objects.create(
            start_time=timezone.now(),
            end_time=end_time,
            auction=instance,
        )


# Connect the signals
post_save.connect(bid_time, sender=Auction)
