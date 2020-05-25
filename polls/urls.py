from django.urls import path, re_path
from .views import \
    index,\
    greetings,\
    redirect_example,\
    current_datetime,\
    upload_file,\
    MyView,\
    MorningGreetingView,\
    ProtectedView,\
    StatementList,\
    StatementDetail,\
    MusicianCreate,\
    MusicianUpdate,\
    MusicianDelete,\
    MusicianDetail,\
    MusicianList
from django.contrib.auth.decorators import login_required, permission_required

app_name = 'polls'
urlpatterns = [
    path('', index.index_page, name='index'),
    path('<int:year>/greet', greetings.greet, name='greet'),
    path('redirect', redirect_example, name='redirect'),
    path('datetime', current_datetime, name='datetime'),
    path('upload', upload_file.upload_file, name='upload'),
    path('upload_for_model', upload_file.model_file_upload, name='model_upload'),

    #class based views
    path('my_view', MorningGreetingView.as_view(), name='my_view'),
    path('decorator', ProtectedView.as_view(), name='decorator'),
    path('statement_list', StatementList.as_view(), name='statement_list'),
    re_path('statement_detail/(?P<pk>\\d+)/$', StatementDetail.as_view(), name='statement_detail'),

    re_path('musician_detail,/(?P<pk>\\d+)/$', MusicianDetail.as_view(), name='musician_detail'),
    path('musician_create', MusicianCreate.as_view(), name='musician_create'),
    path('musician_update/<int:pk>/', MusicianUpdate.as_view(), name='musician_update'),
    path('musician_delete/<int:pk>/delete', MusicianDelete.as_view(), name='musician_delete'),
    path('musician_list', MusicianList.as_view(), name='musician_list'),
]