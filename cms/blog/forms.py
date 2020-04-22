from django import forms
import re
from blog.models import post

class ContactForm(forms.Form):
    country_list = [("IN","India"),("CH","China"),("US","United States")]
    name = forms.CharField(max_length=50)
    email = forms.EmailField(required=False)
    phone_no = forms.RegexField(regex="^[6-9][0-9]{9}$",error_messages={"invalid":"please provide valid phone number"},required=False)
    message = forms.CharField(widget=forms.Textarea)
    country = forms.ChoiceField(choices=country_list)
    password = forms.CharField(max_length=16,widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=16,widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        phone_no = cleaned_data.get("phone_no")
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if not email and not phone_no:
            # raise forms.ValidationError("Atleast email or phone should be provided",code="invalid")
            self.add_error("email","Atleast email or phone should be provided")

        if password!=confirm_password:
            self.add_error("password","password is mismatching reenter the password")
    
    def clean_password(self):
        password = self.cleaned_data.get("password")
        match = re.search("[A-Z]",password)

        if not match:
            raise forms.ValidationError("atleast one uppercase",code="upper")
        else:
            return password

class PostForm(forms.ModelForm):

    class Meta:
        model = post
        fields = ['title','content','status','image','Catogary']

