document.onreadystatechange = function() {
    if (document.readyState !== "complete") {
        document.querySelector(
        "body").style.visibility = "hidden";
        document.querySelector(
        "#loader").style.visibility = "visible";
    } else {
        document.querySelector(
        "#loader").style.display = "none";
        document.querySelector(
        "body").style.visibility = "visible";
    }
};

$(document).ready(function() {
    var sec2 = $(`
    <section id="section_2" class="shortcuts">
            <div class="row">
                <div class="column">
                  <div class="card" style="background-color:#172642">
                    <h3> <a href="https://datasadvocate.dev/resume" style="color:white;">RESUME</a> </h3>
                  </div>
                </div>
                <div class="column">
                  <div class="card" style="background-color:#172642">
                    <h3> 
                      <a href="https://meetings.aps.org/Meeting/FWS18/Event/338683"
                        target="_blank" 
                        rel="noopener noreferrer nofollow"
                        style="color:white;">
                        MASTER'S THESIS
                      </a>
                    </h3>
                  </div>
                </div>
                <div class="column">
                  <div class="card" style="background-color:#172642">
                    <h3>    
                      <a href="https://www.linkedin.com/in/dominicmt/"
                      target="_blank" 
                      rel="noopener noreferrer nofollow" style="color:white;">
                      LINKEDIN
                    </a>
                  </h3>
                  </div>
                </div>
                <div class="column">
                  <div class="card" style="background-color:#172642">
                    <h3>    
                      <a href="https://aip.scitation.org/doi/abs/10.1063/1.4954278"
                      target="_blank" 
                      rel="noopener noreferrer nofollow" style="color:white;">
                      UNDERGRADUATE THESIS
                    </a>
                  </h3>
                  </div>
                </div>
                <div class="column">
                  <div class="card" style="background-color:#172642">
                    <h3>    
                      <a href="/api"
                      target="_blank" 
                      rel="noopener noreferrer nofollow" style="color:white;">
                      API
                    </a>
                  </h3>
                  </div>
                </div>
                <div class="column">
                  <div class="card" style="background-color:#172642">
                    <h3>    
                      <a href="/examples"
                      target="_blank" 
                      rel="noopener noreferrer nofollow" style="color:white;">
                      EXAMPLES/PRACTICE (In development)
                    </a>
                  </h3>
                  </div>
                </div>                
            </div>               
        </section>
    `).hide();
    
    $("a").click("slow", function () {
       $("section").replaceWith( (sec2) );
       $("section").fadeIn(3000);
    });
 });