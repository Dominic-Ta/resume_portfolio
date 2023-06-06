from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import NetflixTitles
from datetime import datetime
import json, requests
from django.core.cache import cache  # This is the memcache cache.
import os
import environ
from django.db.models import Case, CharField, Count, Value, When, Func, Q
from collections import defaultdict
import warnings,heapq
from pathlib import Path
from dotenv import load_dotenv

warnings.filterwarnings("ignore")
# from django.http import HttpResponse
path =  os.path.abspath(os.path.dirname(__file__))
env = environ.Env()
environ.Env.read_env()
relative_path_to_env = Path('../report/.env')
dotenv_path = (path / relative_path_to_env).resolve()
load_dotenv(dotenv_path)
maps_API = os.environ.get('maps_api_key')

# Create your views here.
def main_view(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())

def web_scrape_request(request):
    template = loader.get_template("webscraping_tutorial.html")
    return HttpResponse(template.render())
def lin_reg_view(request):
    template = loader.get_template("Linear_regression.html")
    return HttpResponse(template.render())

def about_view(request):
    total_items = cache.get("total_items")

    if total_items is None:
        top_10_directors_query = (
            NetflixTitles.objects.exclude(director__isnull=True)
            .values("director")
            .annotate(number_of_titles=Count("director"))
            .order_by("-number_of_titles")
            .values("director", "number_of_titles")[:10]
        )
        titles_per_year = (
            NetflixTitles.objects.values(
                year_added=Case(
                    When(date_added__isnull=True, then=Value("2007")),
                    default=Func(
                        "date_added",
                        function="SUBSTR",
                        template="%(function)s(%(expressions)s, -4)",
                    ),
                    output_field=CharField(),
                )
            )
            .annotate(
                number_of_titles_added=Count("*"),
                number_of_tv_shows=Count(Case(When(type__contains="TV", then=1))),
                number_of_movies=Count(Case(When(type__contains="Movie", then=1))),
            )
            .order_by("year_added")
        )

        tpy = {}
        for rank_val, i in enumerate(titles_per_year):
            tpy["{0}".format(rank_val)] = [
                i["year_added"],
                i["number_of_titles_added"],
                i["number_of_tv_shows"],
                i["number_of_movies"],
            ]
        top_10_directors = {}
        for rank_val, i in enumerate(top_10_directors_query):
            top_10_directors["Rank {}".format(rank_val)] = [
                i["director"],
                i["number_of_titles"],
            ]
        genres = NetflixTitles.objects.values("listed_in", "date_added")

        genre_count_all_years = defaultdict(dict)
        for i in genres:
            if i["date_added"] == None:
                i[
                    "date_added"
                ] = "2007"  # 2007 doesn't exist in the db as an upload for some reason. Must'be been there since launche.
            year = i["date_added"][-4:]
            if i["date_added"][-4:] in genre_count_all_years[year]:
                if "," in i["listed_in"]:
                    x = i["listed_in"].split(", ")
                    for j in x:
                        if j in genre_count_all_years[year]:
                            genre_count_all_years[year][j] += 1
                        else:
                            genre_count_all_years[year][j] = 1
                elif i["listed_in"] in genre_count_all_years[year]:
                    genre_count_all_years[year][i["listed_in"]] += 1
                else:
                    genre_count_all_years[year][i["listed_in"]] = 1
            else:
                if "," in i["listed_in"]:
                    x = i["listed_in"].split(", ")
                    for j in x:
                        if j in genre_count_all_years[year]:
                            genre_count_all_years[year][j] += 1
                        else:
                            genre_count_all_years[year][j] = 1
        top_5_genres_by_year = defaultdict(dict)

        for year in genre_count_all_years:
            genres_count = genre_count_all_years[year]
            top_5 = heapq.nlargest(5, genres_count, key=genres_count.get)
            top_5_genres_by_year[year] = [{genre: genres_count[genre] for genre in top_5}]

        netflix_query = NetflixTitles.objects.values("country")
        # netflix_query = NetflixTitles.objects.all() #filter(release_year = 1993)

        available_titles = {}
        for i in netflix_query:
            x = i["country"]
            if x is not None:
                x1 = x.split(",")
                for y in x1:
                    y = y.strip()
                    if y in available_titles.keys():
                        available_titles[y] += 1
                    elif len(y) > 0:
                        available_titles[y] = 1
        total_items = {
            "available_titles": available_titles,
            "top_5_genres_by_year": top_5_genres_by_year,
            "genre_count_all_years": genre_count_all_years,
            "top_10_directors": top_10_directors,
            "titles_per_year": tpy,
        }
        cache.set("total_items", total_items)
    netflix_data = {
        "titles_per_country": json.dumps(total_items["available_titles"]),
        "top_10_directors": json.dumps(total_items["top_10_directors"]),
        "titles_per_year": total_items["titles_per_year"],
        "top_5_genres_by_year": dict(total_items["top_5_genres_by_year"]),
        "genre_count_all_years": dict(total_items["genre_count_all_years"]),
        "maps_API_key": maps_API,
        "years_in_order":  sorted(dict(total_items["top_5_genres_by_year"]).keys(), key=int),
    }
   
    return render(request, "about_netflix_dataset.html", netflix_data)


# def test_view(request):
#     template = loader.get_template("test.html")
#     return HttpResponse(template.render())
def table_load(request):
    title_information = cache.get("netflix_query_cache_message")
    # cache.clear()
    timeout_val = 60 * 60 * 24 * 5
    # timeout_val = 0
    if title_information is None:
        netflix_query = NetflixTitles.objects.all()  # filter(release_year = 1993)
        title_information = return_dict_from_data(netflix_query)
        cache.set("netflix_query_cache_message", title_information, timeout=timeout_val)
    netflix_data = {"meow": title_information}
    return render(request, "netflix_dataset.html", netflix_data)


def return_dict_from_data(dict_val) -> dict:
    """_summary_

    Args:
        dict_val (Query data type): the data we pull from our database.

    Returns:
        dict: a dictionary with a key of an array of each value.
    """
    temp_dict = {}
    for i in dict_val:
        try:
            temp_dict[i.title] = [
                i.index,
                i.type,
                i.country,
                datetime.strptime(i.date_added.strip(), "%B %d, %Y").strftime("%B %Y"),
                i.release_year,
                i.rating,
                i.duration,
            ]
        except Exception as e:
            # print(e)
            continue
    return temp_dict


# def table_load(request):
#     client = Client('localhost', 11211)

#     title_information = client.get('netflix_query_cache_message')

#     if title_information is None:

#         netflix_query = NetflixTitles.objects.all()
#          # filter(release_year = 1993)
#         title_information = return_dict_from_data(netflix_query)

#         temp = json.dumps(title_information, ensure_ascii=False)

#         client.set(key = 'netflix_query_cache_message', value=temp.encode('utf-8'), expire=2592000, noreply=False, flags=0)
#     else:
#         title_information = title_information.decode('utf-8')
#         title_information = json.loads(title_information)
#     netflix_data = {"meow": title_information}
#     return render(request, "netflix_dataset.html", netflix_data)


def load_map(request):
    available_titles = cache.get("title_count_cache")
    if available_titles is None:
        netflix_query = NetflixTitles.objects.values("country")
        # netflix_query = NetflixTitles.objects.all() #filter(release_year = 1993)
        available_titles = {}
        for i in netflix_query:
            x = i["country"]
            if x is not None:
                x1 = x.split(",")
                for y in x1:
                    y = y.strip()
                    if y in available_titles.keys():
                        available_titles[y] += 1
                    elif len(y) > 0:
                        available_titles[y] = 1
        cache.set("title_count_cache", available_titles, timeout=60 * 60 * 24 * 5)
    netflix_data = {"titles_per_country": json.dumps(available_titles), 'maps_API_key': maps_API}
    return render(request, "netflix_map_of_countries.html", netflix_data)


# def indi_info(request, index):
#     netflix_item = NetflixTitles.objects.get(index=index)
#     template = loader.get_template("details.html")
#     x = netflix_item.country.split(",")
#     for i in range(0, len(x), 1):
#         x[i] = x[i].strip()
#     y = {"countries_available": x}
#     context = {
#         "info": netflix_item,
#         "map_json": json.dumps(y),
#     }
#     return HttpResponse(template.render(context, request))


def indi_info(request, index):
    netflix_item = NetflixTitles.objects.get(index=index)
    parameters = {"indi_info": netflix_item}
    if netflix_item.country != None:
        if "," in netflix_item.country:
            x = netflix_item.country.split(",")
            for i in range(0, len(x), 1):
                x[i] = x[i].strip()
            parameters["countries_available"] = x

    key = "b9dac511cea7bf301dd55420d6f3cc98"
    movie = netflix_item.title.strip()
    if ":" in movie:
        parameters["colon_in"] = True
    else:
        parameters["colon_in"] = False
    movie = movie.encode("UTF-8")
    if "TV" in netflix_item.type:
        url = "https://api.themoviedb.org/3/search/tv"
    else:
        url = "https://api.themoviedb.org/3/search/movie"
    params = {"api_key": key, "query": movie, "page": 1}

    y = True
    x = "No Data"
    results = True
    while y == True:
        response = requests.get(url, params=params)
        data = response.json()

        if data["total_results"] == 0:
            results = False
            y = False
            break

        for result in data["results"]:
            if result.__contains__("release_date"):
                if (
                    result["release_date"][0:4] == str(netflix_item.release_year)
                    or result["overview"] == netflix_item.description
                    or netflix_item.title in result["overview"]
                ):
                    x = result
                    results = True
            else:
                if (
                    result["first_air_date"][0:4] == str(netflix_item.release_year)
                    or result["overview"] == netflix_item.description
                    or netflix_item.title in result["overview"]
                ):
                    x = result
                    results = True
            y = False
        params["page"] += 1
    parameters["response"] = x
    # print(parameters)

    if x != "No Data":
        return render(request, "details.html", parameters)
    else:
        template = loader.get_template("not_much_info.html")
        return HttpResponse(template.render())


def test_view(request, index):
    domain = request.get_host().split(":")[0]
    netflix_item = NetflixTitles.objects.get(index=index)

    parameters = {"indi_info": netflix_item, "domain": domain}

    parameters["countries_available"] = update_parameters_for_countries_avail(
        netflix_item
    )

    return render(request, "test.html", parameters)


def update_parameters_for_countries_avail(netflix_item) -> str:
    """_summary_
        This function serves primarily to separate the countries in our database and input them into a readable format for our test cases.
    Args:
        netflix_item (Query Object): This is the query of the information pertaining to the title we are referencing.
        It is unique to that item.
    Returns:
        dict: we're returning a json string so that we can input it into the javascript in our html.
    """
    if netflix_item.country != None:
        if "," in netflix_item.country:
            y = {}
            x = netflix_item.country.split(",")
            for i in range(0, len(x), 1):
                y[x[i].strip()] = 1
            return json.dumps({"countries_available": y})
        else:
            return json.dumps({"countries_available": {netflix_item.country: 1}})
    return json.dumps({"countries_available": {"United States": 1}})


def db_vs_themoviedb_check(netflix_item, params: dict, url: str) -> any:
    y = True
    x = "No Data"
    results = True
    while y == True:
        response = requests.get(url, params=params)

        data = response.json()
        if data["total_results"] == 0:
            results = False
            y = False
            return x

        for result in data["results"]:
            if "release_date" in result:
                if (
                    result["release_date"][0:4] == str(netflix_item.release_year)
                    or result["overview"] == netflix_item.description
                    or netflix_item.title in result["overview"]
                ):
                    return result
            elif "first_air_date" in result:
                if (
                    result["first_air_date"][0:4] == str(netflix_item.release_year)
                    or result["overview"] == netflix_item.description
                    or netflix_item.title in result["overview"]
                ):
                    return result
            y = False
        params["page"] += 1
    return x


def genres(x: str) -> str:
    y = {
        "28": "Action",
        "12": "Adventure",
        "16": "Animation",
        "35": "Comedy",
        "80": "Crime",
        "99": "Documentary",
        "18": "Drama",
        "10751": "Family",
        "14": "Fantasy",
        "36": "History",
        "27": "Horror",
        "10402": "Music",
        "9648": "Mystery",
        "10749": "Romance",
        "878": "Science Fiction",
        "10770": "TV Movie",
        "53": "Thriller",
        "10752": "War",
        "37": "Western",
        "10759": "Action & Adventure",
        "10762": "Kids",
        "10763": "News",
        "10764": "Reality",
        "10765": "Sci-Fi & Fantasy",
        "10766": "Soap",
        "10767": "Talk",
        "10768": "War & Politics",
    }
    if x in y:
        return y[x]
    else:
        return x


def tes_val():
    x = {
        "United States": 3690,
        "South Africa": 62,
        "India": 1046,
        "Ghana": 5,
        "Burkina Faso": 1,
        "United Kingdom": 806,
        "Germany": 226,
        "Ethiopia": 1,
        "Czech Republic": 22,
        "Mexico": 169,
        "Turkey": 113,
        "Australia": 160,
        "France": 393,
        "Finland": 11,
        "China": 162,
        "Canada": 445,
        "Japan": 318,
        "Nigeria": 103,
        "Spain": 232,
        "Belgium": 90,
        "South Korea": 231,
        "Singapore": 41,
        "Italy": 100,
        "Romania": 14,
        "Argentina": 91,
        "Venezuela": 4,
        "Hong Kong": 105,
        "Russia": 27,
        "Ireland": 46,
        "Nepal": 2,
        "New Zealand": 33,
        "Brazil": 97,
        "Greece": 11,
        "Jordan": 9,
        "Colombia": 52,
        "Switzerland": 19,
        "Israel": 30,
        "Taiwan": 89,
        "Bulgaria": 10,
        "Algeria": 3,
        "Poland": 41,
        "Saudi Arabia": 13,
        "Thailand": 70,
        "Indonesia": 90,
        "Egypt": 117,
        "Denmark": 48,
        "Kuwait": 8,
        "Netherlands": 50,
        "Malaysia": 26,
        "Vietnam": 7,
        "Hungary": 11,
        "Sweden": 42,
        "Lebanon": 31,
        "Syria": 3,
        "Philippines": 83,
        "Iceland": 11,
        "United Arab Emirates": 37,
        "Norway": 30,
        "Qatar": 10,
        "Mauritius": 2,
        "Austria": 12,
        "Cameroon": 1,
        "Palestine": 1,
        "Uruguay": 14,
        "Kenya": 6,
        "Chile": 29,
        "Luxembourg": 12,
        "Cambodia": 6,
        "Bangladesh": 4,
        "Portugal": 6,
        "Cayman Islands": 2,
        "Senegal": 3,
        "Serbia": 7,
        "Malta": 3,
        "Namibia": 2,
        "Angola": 1,
        "Peru": 10,
        "Mozambique": 1,
        "Belarus": 1,
        "Zimbabwe": 3,
        "Puerto Rico": 1,
        "Pakistan": 24,
        "Cyprus": 1,
        "Guatemala": 2,
        "Iraq": 2,
        "Malawi": 1,
        "Paraguay": 1,
        "Croatia": 4,
        "Iran": 4,
        "West Germany": 5,
        "Albania": 1,
        "Georgia": 2,
        "Soviet Union": 3,
        "Morocco": 6,
        "Slovakia": 1,
        "Ukraine": 3,
        "Bermuda": 1,
        "Ecuador": 1,
        "Armenia": 1,
        "Mongolia": 1,
        "Bahamas": 1,
        "Sri Lanka": 1,
        "Latvia": 1,
        "Liechtenstein": 1,
        "Cuba": 1,
        "Nicaragua": 1,
        "Slovenia": 3,
        "Dominican Republic": 1,
        "Samoa": 1,
        "Azerbaijan": 1,
        "Botswana": 1,
        "Vatican City": 1,
        "Jamaica": 1,
        "Kazakhstan": 1,
        "Lithuania": 1,
        "Afghanistan": 1,
        "Somalia": 1,
        "Sudan": 1,
        "Panama": 1,
        "Uganda": 1,
        "East Germany": 1,
        "Montenegro": 1,
    }
    return json.dumps({"countries_available": x})


# class send_the_email(forms.Form):
#     contact_name = forms.CharField(max_length=35, label="Name")
#     contact_email = forms.EmailField()
#     Subject = forms.CharField(max_length=35, label="Subject")
#     contact_Message = forms.CharField(
#         widget=forms.Textarea(attrs={"cols": "50", "rows": "15"}), label="Message"
#     )


# def email(request):
#     env = environ.Env()
#     BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     environ.Env.read_env(os.path.join(BASE_DIR, "rport/.env"))
#     email_to = env("app_email")
#     if request.method == "GET":
#         form = send_the_email()
#     else:
#         form = send_the_email(request.POST)
#         if form.is_valid():
#             subject = form.cleaned_data["Subject"]
#             from_email = form.cleaned_data["contact_email"]
#             message = (
#                 "subject: "
#                 + subject
#                 + "\n"
#                 + "message: "
#                 + form.cleaned_data["contact_Message"]
#                 + "\nsent by: "
#                 + form.cleaned_data["contact_name"]
#                 + "\ncontact email: "
#                 + form.cleaned_data["contact_email"]
#             )
#             print(message)
#             try:
#                 send_mail(subject, message, from_email, [email_to])
#             except BadHeaderError:
#                 return HttpResponse("Invalid header found.")
#             return redirect("resume")
#     return render(request, "send_email.html", {"form": form})


# def thanks(request):
#     return HttpResponse("Thank you for your message.")

