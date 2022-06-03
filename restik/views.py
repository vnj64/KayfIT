from .models import Order_to_Product, Product, Order, Menu, Client
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import OrderStateForm, LoginForm
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from restik.serializers import ClientSerializer, MenuSerializer, OrderSerializer, ProductSerializer
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse

def home(request):
    products = Product.objects.all()
    return render(request, 'restik/home.html', {'products': products})


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'restik/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currentrestik')
            except IntegrityError:
                return render(request, 'restik/signupuser.html',
                              {'form': UserCreationForm(), 'error': 'That username has already been taken. Please '
                                                                    'choose a new username'})
        else:
            return render(request, 'restik/signupuser.html', {'form': UserCreationForm(), 'error': 'Passwords did not '
                                                                                                   'match'})


def loginuser(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'restik/loginuser.html', {'form': form})


def currentrestik(request):
    return render(request, 'currentrestik.html')


def redirection_signup(request):
    return redirect(request, 'signupuser')


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def google_map(req):
    """Shows page with Google Map.
    Args:
        req : http request.
    """
    return render(req, 'map.html')


def mapbox_map(request):
    """Shows page with MapBox.
    Args:
        req : http request.
    """
    mapbox_access_token = 'pk.eyJ1Ijoic2lyaXVzZGV2cyIsImEiOiJjbDF3YmJ6ZnMwM3Z4M29ta2tjdmNnZHBiIn0.5_AfG0yijkZHd6heg33ChQ'
    return render(request, 'mapbox.html',
                  {'mapbox_access_token': mapbox_access_token})


def createorderstate(request):
    if request.method == 'GET':
        return render(request, 'restik/createorderstate.html', {'form': OrderStateForm()})
    else:
        try:
            form = OrderStateForm(request.POST)
            neworderstate = form.save(commit=False)
            neworderstate.client = request.client
            neworderstate.save()
            return redirect('currentorderstate')
        except ValueError:
            return render(request, 'restik/createorderstate.html',
                          {'form': OrderStateForm(), 'error': 'Bad data passed in. Try again.'})


def currentorderstate(request):
    orderStates = Order.objects.all()
    return render(request, 'restik/currentorderstates.html', {'orderstatesaaaaaa': orderStates})


def vieworderstate(request, orderstate_pk):
    orderstates = get_object_or_404(Order, pk=orderstate_pk)
    form = OrderStateForm(instance=orderstates)
    return render(request, 'restik/vieworderstate.html', {'orderstates': orderstates, 'form': 'form'})


def logged_out(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def basket(request):
    return render(request, 'restik/basket.html')


def profileuser(request):
    return render(request, 'restik/profile.html')


def payment(request):
    return render(request, 'restik/payment.html')

class ClientAPIList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientViewSet(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),
            'auth': str(request.auth)
        }
        return Response(content)

    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        post_client = Client.objects.create(
            first_name=request.data['first_name'],
            second_name=request.data['second_name'],
            address=request.data['address'],
            phone_number=request.data['phone_number'],
            age=request.data['age']
        )
        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Client.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exist"})

        serializer = ClientSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self, request):
        serializer = ClientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        delete_client = Client.objects.delete(
            first_name=request.data['first_name'],
            second_name=request.data['second_name'],
            address=request.data['address'],
            phone_number=request.data['phone_number'],
            age=request.data['age']
        )
        return Response({'delete': serializer.data})


class ProductAPIList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductViewSet(APIView):

    def get(self, request):
        queryset = Product.objects.all()
        return Response({'products': ProductSerializer(queryset, many=True).data})

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        post_product = Product.objects.create(
            title=request.data['title'],
            description=request.data['description'],
            image=request.data['image'],
            price=request.data['price'],
            url=request.data['url']
        )

        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Product.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exist"})

        serializer = ProductSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})


class MenuAPIList(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class MenuViewSet(APIView):

    def get(self, request):
        queryset = Menu.objects.all()
        return Response({'menus': MenuSerializer(queryset, many=True).data})

    def post(self, request):
        serializer = MenuSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        post_menu = Menu.objects.create(
            title=request.data['title'],
            restriction_age=request.data['restriction_age']
        )
        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Menu.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exist"})

        serializer = MenuSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

class OrderAPIList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderViewSet(APIView):

    def get(self, request):
        queryset = Order.objects.all()
        return Response({'orders': OrderSerializer(queryset, many=True).data})

    def post(self, request):
        order = Order(
            product = request.GET(['product']),
            client = request.GET(['client']),
            orderstates = request.GET(['orderstates']),
            important = request.GET(['important']),
            created = request.GET(['created'])
        )
        order.save()

        return render(request, {'msg': 'Succesfully added'})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Order.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exist"})

        serializer = OrderSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})