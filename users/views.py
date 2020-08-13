from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm


def register(request):
    if request.method != 'POST':
        # Display blank registration form.
        form = UserCreationForm()
    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log the user in and then redirect to home page.
            login(request, new_user)
            return redirect('blog:post_list')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'registration/register.html', context)


def logout(request):
    logout(request)
    return render(request, 'registration/logged_out.html')
