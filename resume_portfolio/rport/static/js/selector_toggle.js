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

function toggleSections() {
  try {
      let alphaSection = document.getElementById("alphaSection");
      let betaSection = document.getElementById("betaSection");
  
      if (isAlphaVisible) {
      alphaSection.style.display = "none";
      betaSection.style.display = "block";
      isAlphaVisible = false;
      chart_creation("bar","bar-chart",[movie_list, num_theaters],"# Opening Theaters",'# of Theaters showing Star Wars on opening day');
      chart_creation("bar","star-chart",[movie_list,opening_profit],"Opening Profit",'Profit of theaters on Opening Day');
     } else {
      alphaSection.style.display = "block";
      betaSection.style.display = "none";
      isAlphaVisible = true;
      }
  } catch(e){
      console.log(e);
  }
}
function chart_creation(t, x, y, z1, z2){
  new Chart(document.getElementById(x), {
    type: t,
    data: {
      labels: y[0],
      datasets: [
          {
            label: z1,
            data: y[1],
            backgroundColor: 'blue'
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
