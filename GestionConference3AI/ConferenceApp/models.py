from django.db import models
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.utils import timezone

import uuid

# Create your models here.
class Conference(models.Model) :
    conference_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    THEME=[
        ("IA","Computer science & Artificial Intelligence"),
        ("SE","Science & Engineering"),
        ("SC"," Social Sciences & Education"),
        ("IT","Interdisciplinary Themes"),
    ]
    theme=models.CharField(max_length=255,choices=THEME)
    location=models.CharField(max_length=50)
    description=models.TextField(validators=[MinLengthValidator(30,"description trop court !")])
    start_date=models.DateField()
    end_date=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"La conférence a comme titre {self.name}"
    def clean(self):
        if self.start_date and self.end_date :
            if self.start_date > self.end_date:
                raise ValidationError("la date de début doit etre inférieur à la date de fin")

def validate_keywords(value):
    keywords_list = [kw.strip() for kw in value.split(',') if kw.strip()]
    if len(keywords_list) > 10:
        raise ValidationError("Vous ne pouvez pas avoir plus de 10 mots-clés.")
    """
    keyword_list=[]
    if self.keywords:
        for k in self.keywords.split(','):
            k=k.strip()
            if k:
                keyword_list.append(k)

        if len(keywords_list) > 10:
            raise ValidationError("Vous ne pouvez pas avoir plus de 10 mots-clés.")
    """

def generate_submission_id():
    uid = str(uuid.uuid4()).replace("-", "").upper()  
    letters_only = ''.join([ch for ch in uid if ch.isalpha()]) 
    return "SUB-" + letters_only[:8]  

class Submission(models.Model) :
    submission_id=models.CharField(max_length=12,primary_key=True,unique=True,default=generate_submission_id )
    title=models.CharField(max_length=50)
    abstract=models.TextField()
    keywords=models.TextField(validators=[validate_keywords])
    paper=models.FileField(
        upload_to="papers/",
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    
    STATUS=[
        ("submitted","submitted"),
        ("uder review","under review"),
        ("accepted","accepted"),
        ("rejeted","rejected"),
    ]
    status=models.CharField(max_length=50,choices=STATUS)
    payed=models.BooleanField(default=False)
    submission_date=models.DateTimeField(auto_now_add=True)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    user=models.ForeignKey("UserApp.User",on_delete=models.CASCADE,related_name="submissions")
    conference=models.ForeignKey(Conference,on_delete=models.CASCADE,related_name="submissions")
    def save(self, *args, **kwargs):
        if not self.submission_id:
            self.submission_id = generate_submission_id()
        super().save(*args, **kwargs)

    def clean(self):
        if self.conference:
            conference = self.conference
            today = timezone.now().date()
            if conference.start_date < today:
                raise ValidationError("Vous ne pouvez pas soumettre pour une conférence déjà passée.")



        if self.user_id:  
            today = timezone.now().date()
            submissions_today = Submission.objects.filter(
                user=self.user,
                submission_date__date=today
        )

        if self.pk:
            submissions_today = submissions_today.exclude(pk=self.pk)

        if submissions_today.count() >= 3:
            raise ValidationError("Vous ne pouvez pas soumettre plus de 3 conférences par jour.")

         
