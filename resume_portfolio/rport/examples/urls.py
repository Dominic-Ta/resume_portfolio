from . import views
from django.urls import path

urlpatterns = [
    path('', views.main_view, name='example'),
    path('get-char/<str:index>', views.get_characters, name="character_data"),
    path('get-planet/<str:plan_name>', views.get_planet, name="planet_redirect"),
    path('get-planet_json/<str:plan_name>', views.get_planet_info, name="planet_json_data"),
    path('assets/<str:tval>/<int:id_num>', views.char_img_view, name="assets_images"),
    path("test_page/<int:index>", views.test_view, name="tests"),
    path("table_load/", views.table_load, name="netflix"),
    path("netflix_map/", views.load_map, name="netflix_map"),
    path("table_load/<int:index>", views.indi_info, name="individual_info"),
    path("NF_DB_explanation_and_analysis", views.about_view, name="about_netflix"),
    path("webscraping/", views.web_scrape_request, name="webscrapes"),
    path("Linear_regression/", views.lin_reg_view, name="linear_regression"),
    path("dashboards_examples/", views.dash, name="dashboards"),
    path("dashboards_examples/starwars/", views.starwars, name="starwars")
] 