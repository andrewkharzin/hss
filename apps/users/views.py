import sweetify
from apps.users.forms import CreateUserForm
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect

# from django.http import HttpResponse
# from django.forms import inlineformset_factory
# from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages


def registerPage(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                sweetify.success(
                    request,
                    "You did it",
                    text="Good job! You successfully showed a SweetAlert message",
                    persistent="Hell yeah",
                )
                form.save()
                user = form.cleaned_data.get("email")
                messages.success(request, "Account was created for " + user)

                return redirect("login")

        context = {"form": form}
        return render(request, "accounts/register.html", context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect("accounts:dashboard")
    else:
        if request.method == "POST":
            email = request.POST.get("email")
            password = request.POST.get("password")

            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect("accounts:dashboard")
            else:
                messages.info(request, "Username OR password is incorrect")

        context = {}
        return render(request, "accounts/login.html", context)


def logoutUser(request):
    logout(request)
    return redirect("accounts:login")


@login_required(login_url="accounts:login")
def home(request):
    # orders = Order.objects.all()
    # customers = Customer.objects.all()

    # total_customers = customers.count()

    # total_orders = orders.count()
    # delivered = orders.filter(status='Delivered').count()
    # pending = orders.filter(status='Pending').count()

    # context = {'orders':orders, 'customers':customers,
    # 'total_orders':total_orders,'delivered':delivered,
    # 'pending':pending }

    return render(request, "dashboard/dashboard.html")
