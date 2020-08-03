from django.db.models import ManyToManyField
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from .models import Album, Image
from .forms import AlbumForm, ImageForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def gallery(request):
    albums = Album.objects.order_by('id')
    # paginator = Paginator(albums, 1)
    # page_value = request.GET.get('page', 1)
    #
    # page = paginator.get_page(page_value)
    # is_page = page.has_other_pages()
    # if page.has_previous():
    #     prev_url = '?page={}'.format(page.previous_page_number())
    # else:
    #     prev_url = ''
    #
    # if page.has_next():
    #     next_url = paginator.page(page_value)
    # else:
    #     next_url = ''
    # context = {'page': page, 'is_page': is_page,
    #            'next_url': next_url,
    #            'prev_url': prev_url}
    return render(request, 'gallery/gallery.html', {'albums': albums})


def album_view(request, pk):
    album = Album.objects.filter(id=pk)
    return render(request, 'gallery/album_view.html', {'album': album})


def about_me(request):
    return render(request, 'gallery/about_me.html')


def create_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = AlbumForm()
    return render(request, 'gallery/create_album.html', {'form': form})


def create_image(request):
    form = ImageForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = ImageForm()
    return render(request, 'gallery/create_image.html', {'form': form})


def edit_image(request, pk):
    image = Image.objects.get(id=pk)
    print(type(image.img))
    if request.method == "POST":
        if 'img' in request.POST:
            request.FILES['img'] = image.img
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image.title = form.cleaned_data['title']
            image.tags = form.cleaned_data['tags']
            image.img = form.cleaned_data['img']
            image.save()
            return redirect('/')
    else:
        form = ImageForm(instance=image)
    return render(request, 'gallery/edit_image.html', {'form': form})


def delete_image(request, pk):
    try:
        image = Image.objects.get(id=pk)
        image.delete()
        return redirect('/')
    except Image.DoesNotExist:
        return HttpResponseNotFound("<h2>Изображение не найдено</h2>")


def delete_album(request, pk):
    try:
        album = Album.objects.get(id=pk)
        album.delete()
        return redirect('/')
    except Album.DoesNotExist:
        return HttpResponseNotFound("<h2>Альбом не найден</h2>")


def edit_album(request, pk):
    album = Album.objects.get(id=pk)
    if request.method == "POST":
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            album.album_title = form.cleaned_data['album_title']
            for album_image in form.cleaned_data['album_image']:
                album.album_image.add(album_image)
            album.save()
            return redirect('/')
    else:
        form = AlbumForm(instance=album)
    return render(request, 'gallery/edit_album.html', {'form': form})
