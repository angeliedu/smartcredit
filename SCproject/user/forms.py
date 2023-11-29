from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_no = forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    date_of_birth = forms.DateField(
        required=True,
        widget=forms.TextInput(attrs={'type': 'date'}),
        help_text='Enter your date of birth.'
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'date_of_birth']

class SignUpForm(forms.Form):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'John'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Wick'}))
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'johnwick@hotmail.com'}))
    phone = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder': '+1 613-890-3452'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter your address', 'style': 'height: 80px;'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Create a strong password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Repeat your password'}))
    

class LoanForm(forms.Form):
    HOME_OWNERSHIP_CHOICES = [
        ('', ''),
        ('MORTGAGE', 'Mortgage'),
        ('RENT', 'Rent'),
        ('OWN', 'Own'),
    ]

    ANNUAL_INCOME_CHOICES = [
        ('', ''),
        ('20000', '$20,000-$29,999'),
        ('30000', '$30,000-$39,999'),
        ('40000', '$40,000-$49,999'),
        ('50000', '$50,000-$59,999'),
        ('60000', '$60,000-$69,999'),
        ('70000', '$70,000-$79,999'),
        ('80000', '$80,000-$89,999'),
        ('90000', '$90,000-$99,999'),
        ('100000', '$100,000-$149,999'),
        ('150000', '$150,000+'),
    ]

    LOAN_AMOUNT_CHOICES = [
        ('', ''),
        ('500', '$500-$999'),
        ('1000', '$1,000-$1,999'),
        ('2000', '$2,000-$2,999'),
        ('3000', '$3,000-$3,999'),
        ('4000', '$4,000-$4,999'),
        ('5000', '$5,000-$5,999'),
        ('6000', '$6,000-$6,999'),
        ('7000', '$7,000-$7,999'),
        ('8000', '$8,000-$8,999'),
        ('9000', '$9,000-$9,999'),
        ('10000', '$10,000-$149,999'),
        ('15000', '$150,000+'),
    ]

    EMPLOYMENT_LENGTH_CHOICES = [
        ('', ''),
        ('< 1 year', 'Less than 1 Year'),
        ('1 year', '1 Year'),
        ('2 years', '2 Years'),
        ('3 years', '3 Years'),
        ('4 years', '4 Years'),
        ('5 years', '5 Years'),
        ('6 years', '6 Years'),
        ('7 years', '7 Years'),
        ('8 years', '8 Years'),
        ('9 years', '9 Years'),
        ('10+ years', '10+ Years'),
    ]

    home_ownership = forms.ChoiceField(choices=HOME_OWNERSHIP_CHOICES, label='Home Ownership')
    annual_inc = forms.ChoiceField(choices=ANNUAL_INCOME_CHOICES, label='Annual Income')
    loan_amnt = forms.ChoiceField(choices=LOAN_AMOUNT_CHOICES, label='loan_amnt')
    emp_length = forms.ChoiceField(choices=EMPLOYMENT_LENGTH_CHOICES, label='Employment Length')
