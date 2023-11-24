from django.shortcuts import render , redirect
from.forms import *
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import datetime


def log_out(request):
    logout(request)
    return redirect('/home')



def register(request):
    if request.method == 'POST':
        form_reg = verification(request.POST)
        if form_reg.is_valid():
            username = form_reg.cleaned_data.get('username')
            password = form_reg.cleaned_data.get('password')
            user = User.objects.filter(username=username , password = password)
            if user:
                return redirect('/home')
            else:
                User.objects.create_user(username=username , password = password)
                return redirect('/home')
    else:
        form_reg = verification()
    context={
        'form' : form_reg
    }
    return render(request , 'verification/register.html' , context)





def base(request):
    if request.method == 'POST':
        form = verification(request.POST)
        return proc_ver(request , form)
    else:
        form = verification()
    tg = Telegramm_Bots.objects.all()
    res_tg=[]
    res_ds=[]
    for i in tg[::-1]:
        res_tg.append(i)
    ds = Discord_Bots.objects.all()
    for i in ds[::-1]:
        res_ds.append(i)
    context = {
        'form' : form,
        'res_tg' : res_tg[0:3],
        'res_ds': res_ds[0:3]
    }
    return render(request , 'base.html' , context)


def proc_ver(request , form):
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('/home')
        else:
            return redirect('/home')


def ver(request , form_reg):
    if form_reg.is_valid():
        username = form_reg.cleaned_data.get('username')
        password = form_reg.cleaned_data.get('password')
        user = User.objects.filter(username=username, password=password)
        if user:
            return redirect('/home')
        else:
            User.objects.create_user(username=username, password=password)
            return redirect('/home')
@login_required(login_url='/register')
def Tg_post(request):
    if request.method == 'POST':
        form = Telegramm_Form(request.POST)
        if form.is_valid():
            try:
                username = request.user.username
                title = form.cleaned_data.get('title')
                text = form.cleaned_data.get('text')
                url = form.cleaned_data.get('url')
                time = datetime.datetime.now()
                time = f'{time.date()} {time.time()}'[:16]
                Telegramm_Bots.objects.create(username=username , title=title , text=text ,time = time, url = url)
                return redirect('/telegramm')
            except:
                return redirect('/qq')
    else:
        form = Telegramm_Form()
    context = {
        'form' : form,
    }
    return render(request , 'bots/telegramm_post.html' , context)


def tg_all(request):
    if request.method == 'POST':
        form = verification(request.POST)
        return proc_ver(request , form)
    else:
        form = verification()
    tg_search = request.GET.get('search' , '')
    res = []
    if tg_search:
        bd = Telegramm_Bots.objects.filter(title = tg_search)
        for i in bd[::-1]:
            res.append(i)
    else:
        bd = Telegramm_Bots.objects.all()
        for i in bd[::-1]:
            res.append(i)
    context = {
        'product_paginator' : res,
        'form' : form
    }
    return render(request , 'bots/telegramm.html' , context)


@login_required(login_url='/register')
def Ds_post(request):
    if request.method == 'POST':
        form = Discord_Form(request.POST)
        if form.is_valid():
            try:
                username = request.user.username
                title = form.cleaned_data.get('title')
                text = form.cleaned_data.get('text')
                url = form.cleaned_data.get('url')
                Discord_Bots.objects.create(username=username , title=title , text=text , url = url)
                return redirect('/discord')
            except:
                return redirect('/qq')
    else:
        form = Discord_Form()
    context = {
        'form' : form
    }
    return render(request , 'bots/discord_post.html' , context)




def ds_all(request):
    if request.method == 'POST':
        form = verification(request.POST)
        return proc_ver(request , form)
    else:
        form = verification()
    tg_search = request.GET.get('search', '')
    res = []
    if tg_search:
        bd = Discord_Bots.objects.filter(title=tg_search)
        for i in bd[::-1]:
            res.append(i)
    else:
        bd = Discord_Bots.objects.all()
        for i in bd[::-1]:
            res.append(i)
    context = {
        'product_paginator' : res,
        'form' : form,
    }
    return render(request , 'bots/discord.html' , context)

@login_required(login_url='/home')
def reviews_tg_add(request):
    if request.method == 'POST':
        form = Telegramm_Reviews_Form(request.POST)
        if form.is_valid():
            text =form.cleaned_data.get('text')
            reporter = form.cleaned_data.get('reporter')
            username = request.user.username
            Telegramm_Reviews.objects.create(text=text , reporter=reporter , username = username)
            return redirect('/tg_reviews')
    else:
        form = Telegramm_Reviews_Form()
    # reviews = Telegramm_Reviews.objects.all()
    context = {
        # 'reviews':reviews,
        'form':form
    }
    return render(request , 'reviews/tg_reviews_add.html' , context)

    # if tg_search:
    #     reviews = Telegramm_Reviews.objects.filter(reporter=tg_search)
    #     for i in reviews[::-1]:
    #         res.append(i)
    # else:
    #     reviews = Telegramm_Reviews.objects.all()
    #     for i in reviews[::-1]:
    #         res.append(i)

def reviews_tg(request):
    tg_search = request.GET.get('search', '')
    title = []
    res = []
    if tg_search:
        reviews = Telegramm_Reviews.objects.all()
        for i in reviews[::-1]:
            print(tg_search , i.reporter)
            if str(i.reporter) == str(tg_search):
                res.append(i)
    else:
        reviews = Telegramm_Reviews.objects.all()
        for i in reviews[::-1]:
            res.append(i)
    for i in res:
        print(i.reporter)
        if i.reporter not in title:
            title.append(i.reporter)
    context = {
        'title' : title ,
        'reviews':  res
    }
    return render(request , 'reviews/tg_reviews.html' , context)


@login_required(login_url='/home')
def reviews_ds_add(request):
    if request.method == 'POST':
        form = Discord_Reviews_Form(request.POST)
        if form.is_valid():
            text =form.cleaned_data.get('text')
            reporter = form.cleaned_data.get('reporter')
            username = request.user.username
            Discord_Reviews.objects.create(text=text , reporter=reporter , username = username)
            return redirect('/ds_reviews')
    else:
        form = Discord_Reviews_Form()
    # reviews = Telegramm_Reviews.objects.all()
    context = {
        # 'reviews':reviews,
        'form':form
    }
    return render(request , 'reviews/ds_reviews_add.html' , context)

    # if tg_search:
    #     reviews = Telegramm_Reviews.objects.filter(reporter=tg_search)
    #     for i in reviews[::-1]:
    #         res.append(i)
    # else:
    #     reviews = Telegramm_Reviews.objects.all()
    #     for i in reviews[::-1]:
    #         res.append(i)
def reviews_ds(request):
    tg_search = request.GET.get('search', '')
    title = []
    res = []
    if tg_search:
        reviews = Discord_Reviews.objects.all()
        for i in reviews[::-1]:
            print(tg_search , i.reporter)
            if str(i.reporter) == str(tg_search):
                res.append(i)
    else:
        reviews = Discord_Reviews.objects.all()
        for i in reviews[::-1]:
            res.append(i)
    for i in res:
        print(i.reporter)
        if i.reporter not in title:
            title.append(i.reporter)
    context = {
        'title' : title ,
        'reviews':  res
    }
    return render(request , 'reviews/ds_reviews.html' , context)


