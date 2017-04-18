# from django.shortcuts import render,get_object_or_404
# # request response
# from django.http import HttpResponse
# from .models import Album, Song  # calling the model
#
# #import templates
# from django.template import loader
# # Create your views here.
#
# #Create shortcut for render
# from django.shortcuts import render
# #handle 404
# from django.http import Http404
#
# #music index
#
#
# def index(request):
#
#     all_albums = Album.objects.all()
#     html = ''
#     # for album in all_albums:
#     #     url = '/music/'+str(album.id)+'/'
#     #     html += '<a href = "'+url+'">' + album.album_title +'</a><br>'
#
#     # template = loader.get_template('music/index.html')
#     # create a dictionary to store data and sent to front end
#
#     context = {
#         'all_albums' : all_albums
#     }
#     # return HttpResponse('')
#     # return HttpResponse(template.render(context,request))
#     return render(request,'music/index.html',{'all_albums':all_albums})
# #music detail
#
#
# # def detail(request, album_id):
# #
# #     try:
# #         # get single album
# #         album = Album.objects.get(pk=album_id)
# #     except Album.DoesNotExist:
# #      # return HttpResponse("<h2>Details for Album id : " +  str(album_id)+" </h2>")
# #         raise Http404("Album Does not exist!!")
# #     return render(request,'music/detail.html',{'album':album})
#
# # Clean up the logic and use django shortcut as below
#
# def detail(request,album_id):
#
#     album = get_object_or_404(Album,pk=album_id)
#     return render(request,'music/detail.html',{'album':album})
#
#
# def favorite(request, album_id):
#
#     album = get_object_or_404(Album, pk = album_id)
#     try:
#         selected_song = album.song_set.get(pk=request.POST['song'])
#     except(KeyError,Song.DoesNotExist):
#         return render(request,'music/detail.html',{
#             'album':album,
#             'error_message':"You did not select a valid song"
#         })
#     else:
#         selected_song.is_favorite = True
#         selected_song.save()
#         return render(request, 'music/detail.html', {'album': album})

"""
 USING GENERIC VIEW
"""

from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from models import Album
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login

from django.views import generic
# from .models import Album
from .form import UserForms

from django.views import View


#TODO: Redirect url
from django.core.urlresolvers import reverse_lazy


#TODO: MUSIC INDEX PAGE
class IndexView(generic.ListView):
    template_name = 'music/index.html'
    # context_object_name = 'all_albums'

    def get_queryset(self):
        print("Album object",Album.objects.all())
        return Album.objects.all()

#TODO: ALBUM DETAIL
class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'


#TODO: CREATE ALBUM USING MODEL FORM
class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

#TODO: UPDATE ALBUM

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


#TODO: DELETE ALBUM
class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')


#TODO: USER FORM VIEW
class UserFormView(View):
    form_class = UserForms
    template_name = 'music/registration_form.html'

    #TODO: Handle get and post request with the same url
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    #TODO: Process form data
    def post(self, request):
        form = self.form_class(request.POST)

        #TODO: validate form
        if form.is_valid():

            #TODO: just get value form form but not save to DB yet
            user = form.save(commit=False)

            # cleaned (nomalized) data unify date format etc.
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # we call this func because django automatically convert ur pw to hash value
            user.set_password(password)
            user.save()

            #TODO: return user object if user and pw is correct

            user = authenticate(username=username, password=password)

            if user is not None:

                # check if account is ban or not in django admin
                if user.is_active:
                    login(request,user)
                    return redirect('music:index')

        return render(request, self.template_name, {'form': form})
























