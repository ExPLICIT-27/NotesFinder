from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Subject, Module, Favorite
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import redirect_to_login
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.contrib.auth import logout
from django.contrib.sessions.models import Session
import os

    # def force_logout_on_start():
    #     Session.objects.all().delete()  

    # force_logout_on_start()


def isSubseq(string1, string2, m, n):
    if m == -1:
        return True
    if n == -1:
        return False
    if string1[m] == string2[n]:
        return isSubseq(string1, string2, m-1, n-1)
    return isSubseq(string1, string2, m, n-1)

def fav_search(request):
    query = request.GET.get('q', '').strip()
    subjects = []

    if query:
        # implementing search functionality along with shorthand name acces "cvla", "os"etc
        query = query.lower()
        for subject in Subject.objects.all():
            subject_name = subject.name.lower()
            subject_code = subject.code.lower()
            if isSubseq(query, subject_name, len(query)-1, len(subject_name)-1) or isSubseq(query, subject_code, len(query)-1, len(subject_code)-1):
                subjects.append(subject)
            
            
    favorites = Favorite.objects.filter(user = request.user).select_related('subject')  
    # Check if the request is AJAX by looking at the request header
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        subject_list = [{"id" : subject.id, "name": subject.name, "code": subject.code, "folder_path": subject.folder_path} for subject in subjects]
        return JsonResponse({"subjects": subject_list})

    # For normal GET requests (when the page is first loaded)
    return render(request, 'books/favorites.html', {'subjects': subjects, 'query': query, 'favorites' : favorites})

def subject_search(request):
    query = request.GET.get('q', '').strip()
    subjects = []

    if query:
        # implementing search functionality along with shorthand name acces "cvla", "os"etc
        query = query.lower()
        for subject in Subject.objects.all():
            subject_name = subject.name.lower()
            subject_code = subject.code.lower()
            if isSubseq(query, subject_name, len(query)-1, len(subject_name)-1) or isSubseq(query, subject_code, len(query)-1, len(subject_code)-1):
                subjects.append(subject)
            
            
        
    # Check if the request is AJAX by looking at the request header
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        subject_list = [{"id" : subject.id, "name": subject.name, "code": subject.code, "folder_path": subject.folder_path} for subject in subjects]
        return JsonResponse({"subjects": subject_list})

    # For normal GET requests (when the page is first loaded)
    return render(request, 'books/homePage.html', {'subjects': subjects, 'query': query})



def login_view(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()


        if not username_or_email or not password:
            messages.error(request, "Username/Email and Password are required.")
            return render(request, 'books/login.html')

        user = None

        if '@' in username_or_email:
            try:
                user_obj = User.objects.get(email=username_or_email)
                user = authenticate(request, username=user_obj.username, password=password)
            except User.DoesNotExist:
                user = None
        else:
            user = authenticate(request, username=username_or_email, password=password)

        if user is not None:
            login(request, user)
            
            if "remember_me" in request.POST:
                request.session.set_expiry(1209600)
            else:
                request.session.set_expiry(0)
            return redirect('subject_search')
        else:
            messages.error(request, "Invalid username/email or password.")

    return render(request, 'books/login.html')



def subject_detail(request, code):
    subject = get_object_or_404(Subject, code = code)
    modules = Module.objects.filter(subject = subject)
    return render(request, 'books/subject_detail.html', {'subject' : subject, 'modules' : modules})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash password
            user.save()

            UserProfile.objects.create(user=user)
            messages.success(request, "Your account has been created! You can now log in.")
            login(request, user)
            return redirect('subject_search')  # Redirect to search page
    else:
        form = UserRegistrationForm()  # Only create a blank form for GET requests

    return render(request, 'books/register.html', {'form': form})  # ✅ Always return the same form!


@login_required(login_url='login')
def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user = request.user)
    return render(request, 'books/profile.html', {'user_profile' : user_profile})


@login_required(login_url='login')
def favorites(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Please log in first to access your favorites.")
        return redirect_to_login(request.path, login_url='login')  # Redirects to login page

    user_favorites = Favorite.objects.filter(user = request.user).select_related('subject')
    return render(request, 'books/favorites.html', {'favorites': user_favorites})



def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('login')  

@login_required
def add_to_favorites(request):
    if request.method == "POST":
        subject_id = request.POST.get("subject_id")
        subject = get_object_or_404(Subject, id = subject_id)
        
        favorite, created = Favorite.objects.get_or_create(user = request.user, subject = subject)
        
    return redirect("favorites_page") 

@login_required
def remove_from_favorites(request):
    if request.method == "POST" :
        subject_id = request.POST.get("subject_id")
        subject = get_object_or_404(Subject, id = subject_id)
        
        Favorite.objects.filter(user = request.user, subject = subject).delete()
    return redirect("favorites_page")


@login_required
def update_profile_picture(request):
    if request.method == "POST":
        if request.FILES.get('profile-picture'):
            try:
                # Get or create the user profile
                user_profile, created = UserProfile.objects.get_or_create(user=request.user)
                
                # Delete the old picture if it exists (to save space)
                if user_profile.profile_picture:
                    try:
                        if os.path.isfile(user_profile.profile_picture.path):
                            os.remove(user_profile.profile_picture.path)
                    except Exception as e:
                        # Just log the error, don't stop the process
                        print(f"Error removing old profile picture: {e}")
                
                # Save the new picture
                user_profile.profile_picture = request.FILES['profile-picture']
                user_profile.save()
                
                messages.success(request, "Profile picture updated successfully!")
            except Exception as e:
                messages.error(request, f"Error updating profile picture: {str(e)}")
        else:
            messages.warning(request, "No image file was selected.")
    return redirect('profile')