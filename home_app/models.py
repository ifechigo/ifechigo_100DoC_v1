from django.db import models


# Create your models here.
class Login(models.Model):
    loginUsername = models.CharField(max_length=100)
    loginPassword = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.loginUsername, self.loginPassword)


class Signup(models.Model):
    signupUsername = models.CharField(max_length=100)
    signupPassword = models.CharField(max_length=50)
    signupConfirmPassword = models.CharField(max_length=50)
    signupEmail = models.EmailField(max_length=100)
    signup = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.signupConfirmPassword,
                           self.signupEmail,
                           self.signupPassword,
                           self.signupUsername)
