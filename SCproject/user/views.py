from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import EmailMultiAlternatives, send_mail
from django.shortcuts import redirect, render
from django.template import Context
from django.template.loader import get_template

from .forms import LoanForm, UserRegisterForm
from .predict import X_train, classifier, predict_loan_acceptance, scaler


#################### index####################################### 
def index(request):
	return render(request, 'user/index.html', {'title':'index'})

########### register here ##################################### 
def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			email = form.cleaned_data.get('email')
			######################### mail system #################################### 
			htmly = get_template('user/Email.html')
			d = { 'username': username }
			subject, from_email, to = 'welcome', 'your_email@gmail.com', email
			html_content = htmly.render(d)
			msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
			msg.attach_alternative(html_content, "text/html")
			msg.send()
			################################################################## 
			messages.success(request, f'Your account has been created ! You are now able to log in')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'user/register.html', {'form': form, 'title':'register here'})

################ login forms################################################### 
def Login(request):
	if request.method == 'POST':

		# AuthenticationForm_can_also_be_used__

		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username = username, password = password)
		if user is not None:
			form = login(request, user)
			messages.success(request, f' welcome {username} !!')
			return redirect('creditForm')
		else:
			messages.info(request, f'account done not exit plz sign in')
	form = AuthenticationForm()
	return render(request, 'user/login.html', {'form':form, 'title':'log in'})

def creditForm_page(request):
    form = LoanForm()

    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            # Process the form data here
            form_data = {
                'home_ownership': form.cleaned_data['home_ownership'],
                'annual_inc': form.cleaned_data['annual_inc'],
                'loan_amnt': form.cleaned_data['loan_amnt'],
                'emp_length': form.cleaned_data['emp_length'],
            }

            # Call the prediction function
            prediction_result = predict_loan_acceptance(classifier, scaler, form_data)

            # Print or use the prediction result as needed
            print("Prediction Result:", prediction_result)

            # Check the prediction result and redirect accordingly
            if "ACCEPTED" in prediction_result.upper():
                return redirect('Dashboard')
            else:
                # You can add a message here to display in the form if needed
                form.add_error(None, "Loan application rejected. Please review your details.")

    context = {'title': 'credit Form', 'form': form}
    return render(request, 'user/creditForm.html', context)



def Dashboard_page(request):
    return render(request,'user/dashboard.html')
