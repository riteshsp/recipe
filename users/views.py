from django.shortcuts import render
from rest_framework.views import APIView
from django.shortcuts import render ,redirect
from users.serializer import UserSerializer
# from rest_framework.response import Response
from django.http import HttpResponse
from users.models import User, UserProfile
from django.template.loader import render_to_string
from django.core.mail import send_mail
from recipe.settings import EMAIL_HOST_USER
from django.utils.crypto import get_random_string
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password




class SignUp(APIView):
    def get(self, request):
        # user=User.objects.get(id=35)
        # user.password=make_password('password')
        # user.save()

        return render(request, 'signup.html')

    def send_email(self, subject, sender, receiver, message, link):
        template = render_to_string(
            'email-template.html', {'name': message, 'verificationlink': link})
        send_mail(subject, message=message, from_email=sender,
                  recipient_list=[receiver], html_message=template)

    def post(self, request):
        try:
            data = request.data
            userdata = {
                'first_name': data.get('first_name', ''),
                'last_name':  data.get('last_name', ''),
                'username':  data.get('username', ''),
                'userprofilee': {
                'profession': data.get('profession', ''),
                },
                'password': make_password(data.get('password')),
                'is_active': 0
            }

            serializer = UserSerializer(data=userdata, partial=True)
            username = User.objects.filter(username=request.data['username'])
            if username:
                return render(request, "signup.html", {"message": 'A user with this email already Exists', 'data': data})
            else:
                if serializer.is_valid():
                    user = serializer.save()
                    code = get_random_string(length=10)
                    profile = user.userprofile
                    profile.verification_code = code
                    profile.save()
                    self.send_email('Verify your mail', EMAIL_HOST_USER, request.data['username'], request.data['first_name'], f'http://127.0.0.1:8000/user/verification/{code}')
                    return render(request, "signup.html", {"message": "A verification mail has been sent"})
                else:
                    return render(request, "signup.html", {"errors": serializer.errors})
        except Exception as e:
            msg = {"data": str(
                e), "message": "some error occured", "status": 500}
            return render(request, "signup.html", {"message": str(e)})


class VerifyEmail(APIView):
    def get(self,request,code):
        try:
            userprofile= UserProfile.objects.get(verification_code=code)
            if userprofile:
                print(userprofile)
                userr=userprofile.user
                userr.is_active = True
                userr.save()
                return HttpResponse('Email Verified')
            else:
                return HttpResponse('unable to verify email')
        except Exception as e:
            print(str(e))
            return redirect('/')


class Login(APIView):

    def get(self, request):
        return render(request, "login.html")
    
    def post(self,request):
        try:
            print(request.data)
            username=request.data['username']
            password=request.data['password']
            print('Trying to authenticate User')
            users=authenticate(self,username=username,password=password)
            print('Authentication results,',users)
            print(users)
            if users:
                print('user exists')
                login(request,users)
                return redirect("home/")
            else:
                print('user not authenticated')
                return render(request, "login.html", {"message": "Incorrect Email or Password"})
                # return redirect("/")
        except Exception as e:
            print(str(e))
            return redirect('/')



class Home(APIView):
    def get(self, request):
        return render(request, "navbar_sidebar.html")


class LogOutUser(APIView):
    def get(self,request):
        logout(request)
        return redirect("/website/")
