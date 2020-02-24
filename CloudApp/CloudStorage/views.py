from django.shortcuts import render
from django.http import HttpResponse as httpr
from . models import Post, Document, FileName
from django.core.files.storage import FileSystemStorage
import logging
import boto3
from botocore.exceptions import ClientError
from django.core.files.storage import default_storage
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
# from flask import Flask, render_template
import os


# s3 = boto3.resource('s3')
# my_bucket = os.environ.get('bucket_name')
# s3_client = boto3.client('s3')
# this_bucket = my_bucket.objects.all()
# list_of_keys = []
# bucket_name = os.environ.get('bucket_name')


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    #return httpr('<h1>Application\'s Home Page</h1>')
    return render(request, 'CloudStorage/home.html', context, {'title': 'Home'})

def about(request):
    #return httpr('<h1>Application\'s About Page</h1>')
    return render(request, 'CloudStorage/about.html')


def is_authenticated(user):
    if callable(user.is_authenticated):
        return user.is_authenticated()
    return user.is_authenticated


def bucket_empty(k_list):
    size = len(k_list)

    if size == 0:
        return True
    return False


# def check_list():
#     list_of_keys = []
#     for my_bucket_object in this_bucket:
#         if my_bucket_object.key not in list_of_keys:
#             list_of_keys.append(my_bucket_object.key)
#     return list_of_keys


@login_required
def upload_file(request):
    list_of_keys = check_list()

    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)

        file_name = 'media/' + str(uploaded_file)

        upload(file_name, bucket_name, object_name = None)

        for my_bucket_object in this_bucket:
            if my_bucket_object.key not in list_of_keys:
                list_of_keys.append(my_bucket_object.key)

    return render(request, 'CloudStorage/upload.html', {'context': context, \
    'keys': list_of_keys, 'bucket_empty': bucket_empty(list_of_keys)})


# def upload(file_name, bucket, object_name = None):
#     if object_name is None:
#         object_name = file_name
#
#     try:
#         s3_client.upload_file(file_name, bucket, object_name)
#     except ClientError as e:
#         logging.error(e)


def download_file(request):
    list_of_keys = check_list()

    filename = request.POST.get('file_name', False)
    data = FileName(file_name = filename)
    data.save()

    download(filename, bucket_name)

    print(f'Download File Function has been called. {filename} is downloaded.')

    return render(request, 'CloudStorage/download.html', {'keys': list_of_keys, \
    'bucket_empty': bucket_empty(list_of_keys)})


# def download(file_name, bucket_name):
#     try:
#         object_name = file_name
#         s3.Bucket(bucket_name).download_file(file_name, object_name)
#     except:
#         print('Something went wrong. File was not downloaded.')


def remove_file(request):
    list_of_keys = check_list()

    filename = request.POST.get('file_name', False)
    data = FileName(file_name = filename)
    data.save()

    remove_f(filename, bucket_name)

    list_of_keys = check_list()

    print(f'Remove File Function has been called. {filename} is removed.')

    return render(request, 'CloudStorage/remove.html',  {'keys': list_of_keys, \
    'bucket_empty': bucket_empty(list_of_keys)})


# def remove_f(file_name, bucket_name):
#     file_to_delete = file_name
#     bucket = bucket_name
#     try:
#         obj = s3.Object(bucket, file_to_delete)
#         obj.delete()
#     except:
#         print('Something went wrong. File was not deleted.')
