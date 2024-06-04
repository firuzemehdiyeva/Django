from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=35,label="Username")
    password = forms.CharField(max_length=15,label="Password",widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=15,label="Password confirm",widget=forms.PasswordInput)
    
    
    def clean(self):
        username = self.cleaned_data["username"]
        password = self.cleaned_data["password"]
        confirm = self.cleaned_data["confirm"]
        
        if password and confirm and password != confirm:
            raise forms.ValidationError("Şifrələr eyni deyil !!!!")
        
        values = {
            "username":username,
            "password":password
        } 
        
        return values   
    
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=35,label="Username")
    password = forms.CharField(max_length=15,label="Password",widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=15,label="Password confirm",widget=forms.PasswordInput)
    