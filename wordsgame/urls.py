from django.urls import path
from .views import *

urlpatterns = [
    path('', MainPage.as_view() ,name='index_page_url'),
    path('play/',GamePage.as_view(), name='main_game_url'),
    path('words/', WordsList, name='words_list_url'),
    path('ovaeva/', OvaGame.as_view(), name='ova_game_url'),
    path('prepri/', PreGame.as_view(), name='pre_game_url'),
    path('iorii/', IiGame.as_view(), name='ii_game_url'),
    path('znak/', ZnakGame.as_view(), name='znak_game_url'),
    path('chik/', ChiGame.as_view(), name='chi_game_url'),
    path('oyo/', OyoGame.as_view(), name='oyo_game_url'),
    
    
    path('random/', RandomGame.as_view(), name='random_game_url'),
    
    
    path('profile/<str:current_user_page_name>/', MyProfile.as_view(), name='profile_url'),
    path('login/', MyLogin.as_view(), name='login_url'),
    path('register/', RegisterUser.as_view(), name='auth_url'),
    path('regout/', MyLogout.as_view(), name='logout_url'),
]