from django.urls import path
from main.views import show_main, create_fresh_bakes_entry, show_xml, show_json, show_xml_by_id, show_json_by_id, login_user, logout_user, register

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create_fresh_bakes_entry', create_fresh_bakes_entry, name='create_fresh_bakes_entry'),
    path('json/', show_json, name='show_json'),
    path('xml/', show_xml, name='show_xml'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register'),
]

