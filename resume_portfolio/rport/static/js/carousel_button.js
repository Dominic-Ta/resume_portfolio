// I needed something to highlight the bars to our buttons regarding our carousel. It appears that
// when we removed it from the container, it would no longer work. So I had to remake it.
let previousClass = null;
new MutationObserver((mutationsList) => {
  mutationsList.forEach((mutation) => {
    if (mutation.type === 'attributes' && mutation.attributeName === 'class') {
      let currentClass = mutation.target.className;
      if (currentClass.includes('active') && currentClass !== previousClass) {
        let el_car_val = mutation.target.getAttribute('data-car-count');
        if (document.querySelector(`[data-button-var="${el_car_val}"]`)) {
          let button_el = document.querySelector(`[data-button-var="${el_car_val}"]`);
          let all_buttons_el = document.querySelectorAll('[data-button-var]');
          all_buttons_el.forEach(function(ele) {
              if (!button_el.classList.contains('active')){
                button_el.classList.add('active');
              } 
              if (ele.classList.contains('active') && ele.getAttribute('data-button-var') != el_car_val){
                ele.classList.remove('active')
              }
            }
          );
        }
      }
      previousClass = currentClass;
    }
  });
}).observe(document.body, { subtree: true, attributes: true });  