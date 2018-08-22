from django.db import models
from django import forms
import string
import random
import datetime
# Create your models here.


class Site(models.Model):
    js=models.TextField(default="")
    css=models.TextField(default="")
    html=models.TextField()
    name=models.TextField()
    viewsCount=models.IntegerField()
    usesBootstrap=models.BooleanField(default=False)
    usesJquery=models.BooleanField(default=False)
    endingDate=models.DateTimeField(default=datetime.datetime.now()+datetime.timedelta(days=2))
    hash=models.TextField()
    isPrivate=models.BooleanField(default=True)
    def makeHash(self):
        self.hash=''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10))
    def __str__(self):
        return self.name

class SiteForm(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'required': True,'placeholder':'Page name',"class":"form-control"}),label='', required=True)
    html=forms.CharField(widget=forms.Textarea(attrs={'required': True,"class":"form-control","placeholder":"HTML code"}), label="", required=True)
    css=forms.CharField(widget=forms.Textarea(attrs={"class":"form-control","rows":"3","placeholder":"CSS code (optional, you can paste CSS in <style> tag)"}), label="", required=False)
    js=forms.CharField(widget=forms.Textarea(attrs={"class":"form-control","rows":"3","placeholder":"JavaScript code (optional too, you can paste in <script> tag)"}), label="", required=False)
    usesBootstrap=forms.BooleanField(widget=forms.CheckboxInput(), required=False, label="include Bootstrap?")
    usesJquery=forms.BooleanField(widget=forms.CheckboxInput, required=False, label="include jQuery?")
    isPrivate=forms.BooleanField(widget=forms.CheckboxInput, required=False, label="Private?")
    endingDate=forms.CharField(widget=forms.NumberInput(attrs={"class":"form-control","max":"7","min":"1","value":"2"}),required=False, label="days to expire. Max 7 days")


