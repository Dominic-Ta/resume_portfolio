from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from django.contrib.auth.models import User
from . import serializer, models


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializer.UserSerializer
    http_method_names = ["get", "head"]


class StudentPerformanceViewSet(viewsets.ModelViewSet):
    queryset = models.StudentPerformance.objects.all()
    serializer_class = serializer.StudentPerformanceSerializer
    http_method_names = ["get", "head"]


class SQLExampleViewSet(viewsets.ModelViewSet):
    queryset = models.SqlExamples.objects.all()
    serializer_class = serializer.SqlExamplesSerializer
    http_method_names = ["get", "head"]


class AnimalCrossingNewHorizonCatalogAccessoriesViewSet(viewsets.ModelViewSet):
    queryset = models.AnimalCrossingNewHorizonCatalogAccessories.objects.all()
    serializer_class = serializer.AnimalCrossingNewHorizonCatalogAccessoriesSerializer
    http_method_names = ["get", "head"]


class AnimalCrossingNewHorizonCatalogAchievementsViewSet(viewsets.ModelViewSet):
    queryset = models.AnimalCrossingNewHorizonCatalogAchievements.objects.all()
    serializer_class = serializer.AnimalCrossingNewHorizonCatalogAchievementsSerializer
    http_method_names = ["get", "head"]


class AnimalCrossingNewHorizonCatalogArtViewSet(viewsets.ModelViewSet):
    queryset = models.AnimalCrossingNewHorizonCatalogArt.objects.all()
    serializer_class = serializer.AnimalCrossingNewHorizonCatalogArtSerializer
    http_method_names = ["get", "head"]


class AnimalCrossingNewHorizonCatalogBagsViewSet(viewsets.ModelViewSet):
    queryset = models.AnimalCrossingNewHorizonCatalogBags.objects.all()
    serializer_class = serializer.AnimalCrossingNewHorizonCatalogBagsSerializer
    http_method_names = ["get", "head"]


class AnimalCrossingNewHorizonCatalogBottomsViewSet(viewsets.ModelViewSet):
    queryset = models.AnimalCrossingNewHorizonCatalogBottoms.objects.all()
    serializer_class = serializer.AnimalCrossingNewHorizonCatalogBottomsSerializer
    http_method_names = ["get", "head"]


class AnimalCrossingNewHorizonCatalogDressUpViewSet(viewsets.ModelViewSet):
    queryset = models.AnimalCrossingNewHorizonCatalogDressUp.objects.all()
    serializer_class = serializer.AnimalCrossingNewHorizonCatalogDressUpSerializer
    http_method_names = ["get", "head"]


class AnimalCrossingNewHorizonCatalogConstructionViewSet(viewsets.ModelViewSet):
    queryset = models.AnimalCrossingNewHorizonCatalogConstruction.objects.all()
    serializer_class = serializer.AnimalCrossingNewHorizonCatalogConstructionSerializer
    http_method_names = ["get", "head"]


class AnimalCrossingNewHorizonCatalogFencingViewSet(viewsets.ModelViewSet):
    queryset = models.AnimalCrossingNewHorizonCatalogFencing.objects.all()
    serializer_class = serializer.AnimalCrossingNewHorizonCatalogFencingSerializer
    http_method_names = ["get", "head"]


class AnimalCrossingNewHorizonCatalogFishViewSet(viewsets.ModelViewSet):
    queryset = models.AnimalCrossingNewHorizonCatalogFish.objects.all()
    serializer_class = serializer.AnimalCrossingNewHorizonCatalogFishSerializer
    http_method_names = ["get", "head"]


class AnimalCrossingNewHorizonCatalogFloorsViewSet(viewsets.ModelViewSet):
    queryset = models.AnimalCrossingNewHorizonCatalogFloors.objects.all()
    serializer_class = serializer.AnimalCrossingNewHorizonCatalogFloorsSerializer
    http_method_names = ["get", "head"]


class AnimalCrossingNewHorizonCatalogFossilsViewSet(viewsets.ModelViewSet):
    queryset = models.AnimalCrossingNewHorizonCatalogFossils.objects.all()
    serializer_class = serializer.AnimalCrossingNewHorizonCatalogFossilsserializer
    http_method_names = ["get", "head"]


class AnimalCrossingNewHorizonCatalogHeadwearViewSet(viewsets.ModelViewSet):
    queryset = models.AnimalCrossingNewHorizonCatalogHeadwear.objects.all()
    serializer_class = serializer.AnimalCrossingNewHorizonCatalogHeadwearserializer
    http_method_names = ["get", "head"]


class AnimalCrossingNewHorizonCatalogHousewaresViewSet(viewsets.ModelViewSet):
    queryset = models.AnimalCrossingNewHorizonCatalogHousewares.objects.all()
    serializer_class = serializer.AnimalCrossingNewHorizonCatalogHousewaresserializer
    http_method_names = ["get", "head"]


class AnimalCrossingNewHorizonCatalogInsectsViewSet(viewsets.ModelViewSet):
    queryset = models.AnimalCrossingNewHorizonCatalogInsects.objects.all()
    serializer_class = serializer.AnimalCrossingNewHorizonCatalogInsectsserializer
    http_method_names = ["get", "head"]


class AnimalCrossingNewHorizonCatalogMiscellaneousViewSet(viewsets.ModelViewSet):
    queryset = models.AnimalCrossingNewHorizonCatalogMiscellaneous.objects.all()
    serializer_class = serializer.AnimalCrossingNewHorizonCatalogMiscellaneousserializer
    http_method_names = ["get", "head"]


class AnimalCrossingNewHorizonCatalogMusicViewSet(viewsets.ModelViewSet):
    queryset = models.AnimalCrossingNewHorizonCatalogMusic.objects.all()
    serializer_class = serializer.AnimalCrossingNewHorizonCatalogMusicserializer
    http_method_names = ["get", "head"]


class AnimalCrossingNewHorizonCatalogOtherViewSet(viewsets.ModelViewSet):
    queryset = models.AnimalCrossingNewHorizonCatalogOther.objects.all()
    serializer_class = serializer.AnimalCrossingNewHorizonCatalogOtherserializer
    http_method_names = ["get", "head"]


class AnimalCrossingNewHorizonCatalogPhotosViewSet(viewsets.ModelViewSet):
    queryset = models.AnimalCrossingNewHorizonCatalogPhotos.objects.all()
    serializer_class = serializer.AnimalCrossingNewHorizonCatalogPhotosserializer
    http_method_names = ["get", "head"]


class AnimalCrossingNewHorizonCatalogPostersViewSet(viewsets.ModelViewSet):
    queryset = models.AnimalCrossingNewHorizonCatalogPosters.objects.all()
    serializer_class = serializer.AnimalCrossingNewHorizonCatalogPostersserializer
    http_method_names = ["get", "head"]


class AnimalCrossingNewHorizonCatalogReactionsViewSet(viewsets.ModelViewSet):
    queryset = models.AnimalCrossingNewHorizonCatalogReactions.objects.all()
    serializer_class = serializer.AnimalCrossingNewHorizonCatalogReactionsserializer
    http_method_names = ["get", "head"]


class AnimalCrossingNewHorizonCatalogRecipesViewSet(viewsets.ModelViewSet):
    queryset = models.AnimalCrossingNewHorizonCatalogRecipes.objects.all()
    serializer_class = serializer.AnimalCrossingNewHorizonCatalogRecipesserializer
    http_method_names = ["get", "head"]


class AnimalCrossingNewHorizonCatalogRugsViewSet(viewsets.ModelViewSet):
    queryset = models.AnimalCrossingNewHorizonCatalogRugs.objects.all()
    serializer_class = serializer.AnimalCrossingNewHorizonCatalogRugsserializer
    http_method_names = ["get", "head"]


class AnimalCrossingNewHorizonCatalogShoesViewSet(viewsets.ModelViewSet):
    queryset = models.AnimalCrossingNewHorizonCatalogShoes.objects.all()
    serializer_class = serializer.AnimalCrossingNewHorizonCatalogShoesserializer
    http_method_names = ["get", "head"]


class AnimalCrossingNewHorizonCatalogSocksViewSet(viewsets.ModelViewSet):
    queryset = models.AnimalCrossingNewHorizonCatalogSocks.objects.all()
    serializer_class = serializer.AnimalCrossingNewHorizonCatalogSocksserializer
    http_method_names = ["get", "head"]


class AnimalCrossingNewHorizonCatalogToolsViewSet(viewsets.ModelViewSet):
    queryset = models.AnimalCrossingNewHorizonCatalogTools.objects.all()
    serializer_class = serializer.AnimalCrossingNewHorizonCatalogToolsserializer
    http_method_names = ["get", "head"]


class AnimalCrossingNewHorizonCatalogTopsViewSet(viewsets.ModelViewSet):
    queryset = models.AnimalCrossingNewHorizonCatalogTops.objects.all()
    serializer_class = serializer.AnimalCrossingNewHorizonCatalogTopsserializer
    http_method_names = ["get", "head"]


class AnimalCrossingNewHorizonCatalogUmbrellasViewSet(viewsets.ModelViewSet):
    queryset = models.AnimalCrossingNewHorizonCatalogUmbrellas.objects.all()
    serializer_class = serializer.AnimalCrossingNewHorizonCatalogUmbrellasserializer
    http_method_names = ["get", "head"]


class AnimalCrossingNewHorizonCatalogVillagersViewSet(viewsets.ModelViewSet):
    queryset = models.AnimalCrossingNewHorizonCatalogVillagers.objects.all()
    serializer_class = serializer.AnimalCrossingNewHorizonCatalogVillagersserializer
    http_method_names = ["get", "head"]


class AnimalCrossingNewHorizonCatalogWallMountedViewSet(viewsets.ModelViewSet):
    queryset = models.AnimalCrossingNewHorizonCatalogWallMounted.objects.all()
    serializer_class = serializer.AnimalCrossingNewHorizonCatalogWallMountedserializer
    http_method_names = ["get", "head"]


class AnimalCrossingNewHorizonCatalogWallpaperViewSet(viewsets.ModelViewSet):
    queryset = models.AnimalCrossingNewHorizonCatalogWallpaper.objects.all()
    serializer_class = serializer.AnimalCrossingNewHorizonCatalogWallpaperserializer
    http_method_names = ["get", "head"]


class NetflixTitlesViewSet(viewsets.ModelViewSet):
    queryset = models.NetflixTitles.objects.all()
    serializer_class = serializer.NetflixTitlesserializer
    http_method_names = ["get", "head"]


class CharacterDataViewSet(viewsets.ModelViewSet):
    queryset = models.CharacterData.objects.all()
    serializer_class = serializer.CharacterDataSerializer
    http_method_names = ["get", "head"]


class StarwarsFilmsViewSet(viewsets.ModelViewSet):
    queryset = models.StarwarsFilms.objects.all()
    serializer_class = serializer.StarwarsFilmsSerializer
    http_method_names = ["get", "head"]


class StarwarsPlanetsViewSet(viewsets.ModelViewSet):
    queryset = models.StarwarsPlanets.objects.all()
    serializer_class = serializer.StarwarsPlanetsSerializer
    http_method_names = ["get", "head"]


class StarwarsSpeciesViewSet(viewsets.ModelViewSet):
    queryset = models.StarwarsSpecies.objects.all()
    serializer_class = serializer.StarwarsSpeciesSerializer
    http_method_names = ["get", "head"]


class StarwarsStarshipsViewSet(viewsets.ModelViewSet):
    queryset = models.StarwarsStarships.objects.all()
    serializer_class = serializer.StarwarsStarshipsSerializer
    http_method_names = ["get", "head"]


class StarwarsVehiclesViewSet(viewsets.ModelViewSet):
    queryset = models.StarwarsVehicles.objects.all()
    serializer_class = serializer.StarwarsVehiclesSerializer
    http_method_names = ["get", "head"]
