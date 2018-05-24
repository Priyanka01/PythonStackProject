from django.db import models
import bcrypt
from datetime import datetime
from ..login_app.models import Guide
from ..login_app.models import Tourist


# Model - Guide Offerings
class GuideOffering(models.Model):
    o_date = models.CharField(max_length=255)
    o_time = models.CharField(max_length = 30)
    o_location = models.CharField(max_length=255)
    o_duration = models.CharField(max_length=255)
    o_guide = models.ForeignKey(Guide,related_name="offerings")
    o_created_at = models.DateTimeField(auto_now_add=True)
    o_updated_at = models.DateTimeField(auto_now=True)

# Model - Days
class OfferingDay(models.Model):
    o_day = models.CharField(max_length=20)
    o_guide = models.ForeignKey(Guide,related_name="offering_days")
    t_created_at = models.DateTimeField(auto_now_add=True)
    t_updated_at = models.DateTimeField(auto_now=True)

# Model - Guide Languages
class GuideLanguage(models.Model):
    language = models.CharField(max_length=255)
    gl_guide = models.ForeignKey(Guide,related_name="languages")
    t_created_at = models.DateTimeField(auto_now_add=True)
    t_updated_at = models.DateTimeField(auto_now=True)

# Model - Guide Speciality
class GuideSpeciality(models.Model):
    speciality = models.CharField(max_length=255)
    gs_guide = models.ForeignKey(Guide,related_name="specialitiies")
    t_created_at = models.DateTimeField(auto_now_add=True)
    t_updated_at = models.DateTimeField(auto_now=True)

#Model - Tour
class Tour(models.Model):
    tour_location = models.CharField(max_length=255)
    tour_datetime = models.DateTimeField()
    tour_duration=models.DateTimeField()
    tour_booked_by = models.ForeignKey(Tourist,related_name="booked_tours")
    tour_guide = models.ForeignKey(Guide,related_name="guided_tours")
    t_created_at = models.DateTimeField(auto_now_add=True)
    t_updated_at = models.DateTimeField(auto_now=True)

#Model - Review
class Review(models.Model):
    r_text = models.CharField(max_length=255)
    r_rating = models.IntegerField()
    reviewed_guide = models.ForeignKey(Guide,related_name="reviews")
    review_writer = models.ForeignKey(Tourist,related_name="reviewed_guides")
    r_created_at = models.DateTimeField(auto_now_add=True)
    r_updated_at = models.DateTimeField(auto_now=True)
