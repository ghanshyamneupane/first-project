from .models import UserProfile
from django.contrib.auth.models import User
from .forms import UserForm, ProfileForm
from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator


class UserRegisterView(View):
    user_form_class = UserForm
    profile_form_class = ProfileForm
    template_name = 'user/user_registration.html'

    def get(self, request):
        user_form = self.user_form_class(None)
        profile_form = self.profile_form_class(None)

        context = {

            'user_form': user_form,
            'profile_form': profile_form
        }

        return render(request, self.template_name, context)

    # def post(self, request):
    # 	user_form = self.user_form_class(request.POST)
    # 	profile_form = self.profile_form_class(request.POST)

    # 	if user_form.is_valid() and profile_form.is_valid():
    # 		user_form.save()
    # 		profile_form.save()
    # 		# username = user_form.cleaned_data["username"] thisi field is to comment
    # 		# password = user_form.cleaned_data["password1"] thisi field is to comment

    # 		# user = authenticate(username = username, password = password) thisi field is to comment
    # 		return redirect('movie:movie-list')

    # 	else:
    # 		return render(request, self.template_name, {

    # 				'user_form' : user_form,
    # 				'profile_form' : profile_form
    # 			})

    @method_decorator(csrf_protect)
    def post(self, request):
        user_created_form = self.user_form_class(request.POST)
        profile_form = self.profile_form_class(request.POST)

        if user_created_form.is_valid() and profile_form.is_valid():
            username = user_created_form.cleaned_data['username']
            firstname = user_created_form.cleaned_data['first_name']
            lastname = user_created_form.cleaned_data['last_name']
            email = user_created_form.cleaned_data['email']
            password = user_created_form.cleaned_data['password1']
            gender = profile_form.cleaned_data['gender']
            phone_number = profile_form.cleaned_data['phone_number']
            location = profile_form.cleaned_data['location']

            try:
                with transaction.atomic():
                    created_user = User.objects.create_user(username=username, password=password, first_name=firstname,
                                                            last_name=lastname, email=email)
                    profile = UserProfile.objects.create(owner=created_user, gender=gender, phone_number=phone_number,
                                                         location=location)
                    created_user.save()
                    profile.save()
                    return redirect('Qfxcinema:movie-list')



            except:
                return render(request, self.template_name, {

                    'user_form': user_created_form,
                    'profile_form': profile_form,
                    'error': 'retry'
                })


class UserProfileView(View):
    template_name = 'user/detail.html'

    def get(request):
        args = {

            'user': request.user
        }

        return render(request, self.template_name, args)
