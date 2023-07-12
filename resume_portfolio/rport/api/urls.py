"""test_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework import routers
from . import views
from django.urls import path, include

router = routers.DefaultRouter()
router.register("users", views.UserViewSet)
router.register("Student_Performance", views.StudentPerformanceViewSet)
router.register("SQLExamples", views.SQLExampleViewSet)
router.register(
    "Animal_crossing_New_Horizons_Accessories_Catalog",
    views.AnimalCrossingNewHorizonCatalogAccessoriesViewSet,
)
router.register(
    "Animal Crossing New Horizon Catalog Achievements",
    views.AnimalCrossingNewHorizonCatalogAchievementsViewSet,
)
router.register(
    "Animal Crossing New Horizon Catalog Art",
    views.AnimalCrossingNewHorizonCatalogArtViewSet,
)
router.register(
    "Animal Crossing New Horizon Catalog Bags",
    views.AnimalCrossingNewHorizonCatalogBagsViewSet,
)
router.register(
    "Animal Crossing New Horizon Catalog Bottoms",
    views.AnimalCrossingNewHorizonCatalogBottomsViewSet,
)
router.register(
    "Animal Crossing New Horizon Catalog Dress Up",
    views.AnimalCrossingNewHorizonCatalogDressUpViewSet,
)
router.register(
    "Animal Crossing New Horizon Catalog Construction",
    views.AnimalCrossingNewHorizonCatalogConstructionViewSet,
)
router.register(
    "Animal Crossing New Horizon Catalog Fencing",
    views.AnimalCrossingNewHorizonCatalogFencingViewSet,
)
router.register(
    "Animal Crossing New Horizon Catalog Fish",
    views.AnimalCrossingNewHorizonCatalogFishViewSet,
)
router.register(
    "Animal Crossing New Horizon Catalog Floors",
    views.AnimalCrossingNewHorizonCatalogFloorsViewSet,
)
router.register(
    "Animal Crossing New Horizon Catalog Fossils",
    views.AnimalCrossingNewHorizonCatalogFossilsViewSet,
)
router.register(
    "Animal Crossing New Horizon Catalog Headwear",
    views.AnimalCrossingNewHorizonCatalogHeadwearViewSet,
)
router.register(
    "Animal Crossing New Horizon Catalog Housewares",
    views.AnimalCrossingNewHorizonCatalogHousewaresViewSet,
)
router.register(
    "Animal Crossing New Horizon Catalog Insects",
    views.AnimalCrossingNewHorizonCatalogInsectsViewSet,
)
router.register(
    "Animal Crossing New Horizon Catalog Miscellaneous",
    views.AnimalCrossingNewHorizonCatalogMiscellaneousViewSet,
)
router.register(
    "Animal Crossing New Horizon Catalog Music",
    views.AnimalCrossingNewHorizonCatalogMusicViewSet,
)
router.register(
    "Animal Crossing New Horizon Catalog Other",
    views.AnimalCrossingNewHorizonCatalogOtherViewSet,
)
router.register(
    "Animal Crossing New Horizon Catalog Photos",
    views.AnimalCrossingNewHorizonCatalogPhotosViewSet,
)
router.register(
    "Animal Crossing New Horizon Catalog Posters",
    views.AnimalCrossingNewHorizonCatalogPostersViewSet,
)
router.register(
    "Animal Crossing New Horizon Catalog Reactions",
    views.AnimalCrossingNewHorizonCatalogReactionsViewSet,
)
router.register(
    "Animal Crossing New Horizon Catalog Recipes",
    views.AnimalCrossingNewHorizonCatalogRecipesViewSet,
)
router.register(
    "Animal Crossing New Horizon Catalog Rugs",
    views.AnimalCrossingNewHorizonCatalogRugsViewSet,
)
router.register(
    "Animal Crossing New Horizon Catalog Shoes",
    views.AnimalCrossingNewHorizonCatalogShoesViewSet,
)

router.register(
    "Animal Crossing New Horizon Catalog Socks",
    views.AnimalCrossingNewHorizonCatalogSocksViewSet,
)
router.register(
    "Animal Crossing New Horizon Catalog Tools",
    views.AnimalCrossingNewHorizonCatalogToolsViewSet,
)
router.register(
    "Animal Crossing New Horizon Catalog Tops",
    views.AnimalCrossingNewHorizonCatalogTopsViewSet,
)
router.register(
    "Animal Crossing New Horizon Catalog Umbrellas",
    views.AnimalCrossingNewHorizonCatalogUmbrellasViewSet,
)
router.register(
    "Animal Crossing New Horizon Catalog Villagers",
    views.AnimalCrossingNewHorizonCatalogVillagersViewSet,
)
router.register(
    "Animal Crossing New Horizon Catalog Wall Mounted",
    views.AnimalCrossingNewHorizonCatalogWallMountedViewSet,
)
router.register(
    "Animal Crossing New Horizon Catalog Wallpaper",
    views.AnimalCrossingNewHorizonCatalogWallpaperViewSet,
)
router.register("Netflix_Titles", views.NetflixTitlesViewSet)
router.register("Starwars_Character_Data", views.CharacterDataViewSet)
router.register("Starwars_Film_Data", views.StarwarsFilmsViewSet)
router.register("Starwars_Planets_Data", views.StarwarsPlanetsViewSet)
router.register("Starwars_Species_Data", views.StarwarsSpeciesViewSet)
router.register("Starwars_Starships_Data", views.StarwarsStarshipsViewSet)
router.register("Starwars_Vehicles_Data", views.StarwarsVehiclesViewSet)
urlpatterns = [
    path("", include(router.urls)),
    path(
        "/Starwars_Character_data/",
        include("rest_framework.urls", namespace="Starwars_Character_Data"),
    ),
    path(
        "/Starwars_Film_Data/",
        include("rest_framework.urls", namespace="Starwars_Film_Data"),
    ),
    path(
        "/Starwars_Planets_Data/",
        include("rest_framework.urls", namespace="Starwars_Planets_Data"),
    ),
    path(
        "/Starwars_Species_Data/",
        include("rest_framework.urls", namespace="Starwars_Species_Data"),
    ),
    path(
        "/Starwars_Starships_Data/",
        include("rest_framework.urls", namespace="Starwars_Starships_Data"),
    ),
    path(
        "/Starwars_Vehicles_Data/",
        include("rest_framework.urls", namespace="Starwars_Vehicles_Data"),
    ),
    path(
        "/student_performance/",
        include("rest_framework.urls", namespace="student_framework"),
    ),
    path(
        "/sql_examples/",
        include("rest_framework.urls", namespace="sql_examples"),
    ),
    path(
        "/Animal_crossing_New_Horizons_Accessories_Catalog/",
        include(
            "rest_framework.urls",
            namespace="Animal_crossing_New_Horizons_Accessories_Catalog",
        ),
    ),
    path(
        "/Animal Crossing New Horizon Catalog Achievements/",
        include(
            "rest_framework.urls",
            namespace="Animal Crossing New Horizon Catalog Achievements",
        ),
    ),
    path(
        "/Animal Crossing New Horizon Catalog Art/",
        include(
            "rest_framework.urls", namespace="Animal Crossing New Horizon Catalog Art"
        ),
    ),
    path(
        "/Animal Crossing New Horizon Catalog Bags/",
        include(
            "rest_framework.urls", namespace="Animal Crossing New Horizon Catalog Bags"
        ),
    ),
    path(
        "/Animal Crossing New Horizon Catalog Bottoms/",
        include(
            "rest_framework.urls",
            namespace="Animal Crossing New Horizon Catalog Bottoms",
        ),
    ),
    path(
        "/Animal Crossing New Horizon Catalog Dress Up/",
        include(
            "rest_framework.urls",
            namespace="Animal Crossing New Horizon Catalog Dress Up",
        ),
    ),
    path(
        "/Animal Crossing New Horizon Catalog Construction/",
        include(
            "rest_framework.urls",
            namespace="Animal Crossing New Horizon Catalog Construction",
        ),
    ),
    path(
        "/Animal Crossing New Horizon Catalog Fencing/",
        include(
            "rest_framework.urls",
            namespace="Animal Crossing New Horizon Catalog Fencing",
        ),
    ),
    path(
        "/Animal Crossing New Horizon Catalog Fish/",
        include(
            "rest_framework.urls", namespace="Animal Crossing New Horizon Catalog Fish"
        ),
    ),
    path(
        "/Animal Crossing New Horizon Catalog Floors/",
        include(
            "rest_framework.urls",
            namespace="Animal Crossing New Horizon Catalog Floors",
        ),
    ),
    path(
        "/Animal Crossing New Horizon Catalog Fossils/",
        include(
            "rest_framework.urls",
            namespace="Animal Crossing New Horizon Catalog Fossils",
        ),
    ),
    path(
        "/Animal Crossing New Horizon Catalog Headware/",
        include(
            "rest_framework.urls",
            namespace="Animal Crossing New Horizon Catalog Headware",
        ),
    ),
    path(
        "/Animal Crossing New Horizon Catalog Housewares/",
        include(
            "rest_framework.urls",
            namespace="Animal Crossing New Horizon Catalog Housewares",
        ),
    ),
    path(
        "/Animal Crossing New Horizon Catalog Insects/",
        include(
            "rest_framework.urls",
            namespace="Animal Crossing New Horizon Catalog Insects",
        ),
    ),
    path(
        "/Animal Crossing New Horizon Catalog Miscellaneous/",
        include(
            "rest_framework.urls",
            namespace="Animal Crossing New Horizon Catalog Miscellaneous",
        ),
    ),
    path(
        "/Animal Crossing New Horizon Catalog Music/",
        include(
            "rest_framework.urls", namespace="Animal Crossing New Horizon Catalog Music"
        ),
    ),
    path(
        "/Animal Crossing New Horizon Catalog Other/",
        include(
            "rest_framework.urls", namespace="Animal Crossing New Horizon Catalog Other"
        ),
    ),
    path(
        "/Animal Crossing New Horizon Catalog Photos/",
        include(
            "rest_framework.urls",
            namespace="Animal Crossing New Horizon Catalog Photos",
        ),
    ),
    path(
        "/Animal Crossing New Horizon Catalog Posters/",
        include(
            "rest_framework.urls",
            namespace="Animal Crossing New Horizon Catalog Posters",
        ),
    ),
    path(
        "/Animal Crossing New Horizon Catalog Reactions/",
        include(
            "rest_framework.urls",
            namespace="Animal Crossing New Horizon Catalog Reactions",
        ),
    ),
    path(
        "/Animal Crossing New Horizon Catalog Recipes/",
        include(
            "rest_framework.urls",
            namespace="Animal Crossing New Horizon Catalog Recipes",
        ),
    ),
    path(
        "/Animal Crossing New Horizon Catalog Rugs/",
        include(
            "rest_framework.urls", namespace="Animal Crossing New Horizon Catalog Rugs"
        ),
    ),
    path(
        "/Animal Crossing New Horizon Catalog Shoes/",
        include(
            "rest_framework.urls", namespace="Animal Crossing New Horizon Catalog Shoes"
        ),
    ),
    path(
        "/Animal Crossing New Horizon Catalog Socks/",
        include(
            "rest_framework.urls", namespace="Animal Crossing New Horizon Catalog Socks"
        ),
    ),
    path(
        "/Animal Crossing New Horizon Catalog Tools/",
        include(
            "rest_framework.urls", namespace="Animal Crossing New Horizon Catalog Tools"
        ),
    ),
    path(
        "/Animal Crossing New Horizon Catalog Tops/",
        include(
            "rest_framework.urls", namespace="Animal Crossing New Horizon Catalog Tops"
        ),
    ),
    path(
        "/Animal Crossing New Horizon Catalog Umbrellas/",
        include(
            "rest_framework.urls",
            namespace="Animal Crossing New Horizon Catalog Umbrellas",
        ),
    ),
    path(
        "/Animal Crossing New Horizon Catalog Villagers/",
        include(
            "rest_framework.urls",
            namespace="Animal Crossing New Horizon Catalog Villagers",
        ),
    ),
    path(
        "/Animal Crossing New Horizon Catalog Wall Mounted/",
        include(
            "rest_framework.urls",
            namespace="Animal Crossing New Horizon Catalog Wall Mounted",
        ),
    ),
    path(
        "/Animal Crossing New Horizon Catalog Wallpaper/",
        include(
            "rest_framework.urls",
            namespace="Animal Crossing New Horizon Catalog Wallpaper",
        ),
    ),
    path(
        "/Netflix_Titles/",
        include("rest_framework.urls", namespace="Netflix_Titles"),
        name="netflix_titles",
    ),
]
