let isAlphaVisible = true;
const movie_list = [
  "Episode IV", 
  "Episode V",
  "Episode VI",
  "Episode I", 
  "Episode II", 
  "Episode III", 
  "Episode VII",
  "Episode VIII",
  "Episode IX"];
const num_theaters=[43,126,1002,2970,3161,3661,4134,4232,4406];
const opening_profit=[1554475,4910483,23019618,64820970,80027814,108435841,247966675,220009584,177383684];
const allData={
  "data":
    [{
      "Release Date":
        [
          "Dec 20, 2019",
          "May 25, 2018",
          "Dec 15, 2017",
          "Dec 16, 2016",
          "Dec 18, 2015",
          "Aug 15, 2008",
          "May 19, 2005",
          "May 16, 2002",
          "May 19, 1999",
          "May 25, 1983",
          "May 21, 1980",
          "May 25, 1977"
        ]},
    {
      "Title":
        [
          "Star Wars: The Rise of Skywalker",
          "Solo: A Star Wars Story",
          "Star Wars Ep. VIII: The Last Jedi",
          "Rogue One: A Star Wars Story",
          "Star Wars Ep. VII: The Force Awakens",
          "Star Wars: The Clone Wars",
          "Star Wars Ep. III: Revenge of the Sith",
          "Star Wars Ep. II: Attack of the Clones",
          "Star Wars Ep. I: The Phantom Menace",
          "Star Wars Ep. VI: Return of the Jedi",
          "Star Wars Ep. V: The Empire Strikes Back",
          "Star Wars Ep. IV: A New Hope"
        ]},
    {
      "Production Budget":
        [
          275,
          275,
          262,
          200,
          306,
          8.5,
          115,
          115,
          115,
          32.5,
          23,
          11
        ]},
    {
      "Domestic Box Office":
        [
          515202542,
          213767512,
          620181382,
          533539991,
          936662225,
          35161554,
          380270577,
          310676740,
          474544677,
          316465003,
          291738960,
          460998007
        ]},
    {
      "Opening Weekend":
        [
          177383864,
          84420489,
          220009584,
          155081681,
          247966675,
          14611273,
          108435841,
          80027814,
          64810970,
          23019618,
          4910483,
          1554475
        ]},
    {
      "Worldwide Box Office":
        [
          1074,
          393,
          1332,
          1055,
          2065,
          69,
          849,
          657,
          1027,
          482,
          549,
          775
        ]}
    ]
  }
const grad=[
  "#fe1212",
  "#f1002c",
  "#e0003d",
  "#cc0049",
  "#b50052",
  "#9b0058",
  "#81005a",
  "#650059",
  "#4a0154",
  "#30094b",
  "#160a40",
  "#000032"
]
const grad2=[
  "#fe1212",
  "#f84000",
  "#f05a00",
  "#e66f00",
  "#da8200",
  "#cb9200",
  "#bca100",
  "#aaaf00",
  "#96bb00",
  "#7fc600",
  "#62d107",
  "#35db3d"
]
const profit_after_production = allData.data[5]["Worldwide Box Office"].map((element, index) => element - allData.data[2]["Production Budget"][index]);
function toggleSections() {
  try {
      let alphaSection = document.getElementById("alphaSection");
      let betaSection = document.getElementById("betaSection");
  
      if (isAlphaVisible) {
      alphaSection.style.display = "none";
      betaSection.style.display = "block";
      isAlphaVisible = false;
      chart_creation("bar","bar-chart",[movie_list, num_theaters],"# Opening Theaters",'# of Theaters showing Star Wars on opening day', grad);
      chart_creation("bar","star-chart",[movie_list,opening_profit],"Opening Profit",'Profit of theaters on Opening Day', grad2);
      donut_chart_creation("doughnut","donut-chart",[allData.data[1].Title,allData.data[5]["Worldwide Box Office"]],"WorldWide Box Office","WorldWide Box Office (mlns)", grad);
      donut_chart_creation("doughnut","donut2-profit-chart",[allData.data[1].Title,profit_after_production],"Profit after Production Budget","Profit after Production Budget (mlns)" , grad2);

     } else {
      alphaSection.style.display = "block";
      betaSection.style.display = "none";
      isAlphaVisible = true;
      }
  } catch(e){
      console.log(e);
  }
}
function donut_chart_creation(t, x, y, z1, z2, gradient){
  let data = {
    labels: y[0],
    datasets: [{
      label: z1,
      data: y[1],
      backgroundColor: gradient,
      hoverOffset: 4
    }]
  };
  option = {
    legend: {
      display: false
   },
    title: {
      display: true,
      text: z2,
      color: '#0f4ee0'
    }
  };
  new Chart(document.getElementById(x), {
    type: t,
    data: data,
    options: option
    }
  );
}
function chart_creation(t, x, y, z1, z2, gradient){
  new Chart(document.getElementById(x), {
    type: t,
    data: {
      labels: y[0],
      datasets: [
          {
            label: z1,
            data: y[1],
            backgroundColor: gradient
          }
        ]
      },
    options: {
      legend: {
        position: 'top',
        },
      title: {
          display: true,
          text: z2
        }
      }
    }
  );
}
