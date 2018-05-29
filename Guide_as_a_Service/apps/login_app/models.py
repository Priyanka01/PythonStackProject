from django.db import models
import bcrypt
from datetime import datetime

class UserManager(models.Manager):
    def validate_register(self, postdata):
        errors = {}
        name = postdata['name']
        email = postdata['email']
        password = postdata['pwd']
        confirm_pwd = postdata['confirm_pwd']
        user_type = postdata['user_type']
        contact = postdata['contact']

        if len(name) < 1:
            errors['name'] = "Name cannot be empty"

        if len(name) < 1:
            errors['name'] = "Name should be more than 3 characters"
        
        if len(email) < 1:
            errors['email'] = "Email cannot be empty"

        if len(email) < 1:
            errors['email'] = "Email should be more than 3 characters"
            
        elif User.objects.filter(email=email):
            errors['duplicateemail'] = "Email already used! Try different email"

        if len(password) < 1:
            errors['password'] = "Password cannot be empty"
        elif len(password) < 1:
            errors['password_len'] = "Password should be atleast 8 characters"
        
        if confirm_pwd != password:
            errors['confirm_pwd'] = "password not matched"

        if len(contact) < 1:
            errors['contact'] = "Contact cannot be less than 1 character" 
 
        return errors

    # # Register new user
    def insertuser(self,postdata):
        errors = {}
        message = self.validate_register(postdata)
        if message:
            return message
        else:
            pw_hash = bcrypt.hashpw(postdata['pwd'].encode(), bcrypt.gensalt())
            User.objects.create(name=postdata['name'],email=postdata['email'],password=pw_hash,contact=postdata['contact'],type=postdata['user_type'])
            return {'user': User.objects.last()}

   # Validate login user
    def validate_login(self, postdata):
        errors = {}
        try:
            user = User.objects.get(username=postdata['loginemail'])
        except:
            errors['email'] = "invalid email"
            return errors

        if bcrypt.checkpw(postdata['loginpwd'].encode('utf-8'), user.pwd.encode('utf-8')):
            return {'user': user}
        else:
            errors['pwd'] = "invalid password"
            return errors        

#Model - User Login
class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30)
    contact = models.CharField(max_length=255)
    type = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    
# Model - Guide Login
class Guide(models.Model):
    guide  = models.ForeignKey(User)
    description = models.TextField(max_length=255)
    aboutme = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # objects = GuideManager()

# Model - Tourist Login
class Tourist(models.Model):
    tourist = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)