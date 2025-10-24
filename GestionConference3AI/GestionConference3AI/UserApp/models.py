from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
import uuid
from django.core.validators import RegexValidator


def generate_user_id():
    return "USER"+uuid.uuid4().hex[:4].upper() 
def verify_email(email):
    domaines=["esprit.tn","sesame.com","tekup.tn","centrale.tn"] 
    email_domaine=email.split("@")[1]
    if email_domaine not in domaines :
        raise ValidationError("l'email est invalide et doit appartenir à un domaine universitaire")

name_validator=RegexValidator(
    regex=r'[a-zA-A\s-]+$',
    message="Ce champs ne doit contenir que des lettres et des espaces "
)



class User(AbstractUser):
    user_id=models.CharField(max_length=8,primary_key=True,unique=True,editable=False)
    first_name=models.CharField(max_length=255,validators=[name_validator])
    last_name=models.CharField(max_length=255,validators=[name_validator])
    ROLE=[
        ("particpant","participant"),
        ("commitee","organizing commitee member "),
    ]
    role=models.CharField(max_length=255,choices=ROLE,default="participant")
    affiliation=models.CharField(max_length=255)
    email=models.EmailField(unique=True,validators=[verify_email])
    nationality=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def save(self,*args,**kwargs):
        if not self.user_id:
            newid=generate_user_id()
            while User.objects.filter(user_id=newid).exists():
                newid=generate_user_id()
            self.user_id=newid
        super().save(*args,**kwargs)


class Organizing_Commitee(models.Model):
    commitee_role=models.CharField(max_length=255,choices=[("chair","chair"),("co-chair","co-chair"),("member","member")])
    date_joined=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    user=models.ForeignKey("UserApp.User",on_delete=models.CASCADE,related_name="committees")
    conference=models.ForeignKey("ConferenceApp.Conference",on_delete=models.CASCADE,related_name="committees")




    