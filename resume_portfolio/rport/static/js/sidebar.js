// Toggle the side navigation
function toggleSidebar() {
    document.body.classList.toggle("sidebar-toggled");
    const sidebar = document.querySelector(".sidebar");
    sidebar.classList.toggle("toggled");
    if (sidebar.classList.contains("toggled")) {
      const collapseElements = document.querySelectorAll('.sidebar .collapse');
      collapseElements.forEach((element) => {
        element.classList.remove('show');
      });
    }
  }
  
  document.getElementById("sidebarToggle").addEventListener("click", toggleSidebar);
  document.getElementById("sidebarToggleTop").addEventListener("click", toggleSidebar);
  
  // Close any open menu accordions when window is resized below 768px
  window.addEventListener("resize", function() {
    if (window.innerWidth < 768) {
      const collapseElements = document.querySelectorAll('.sidebar .collapse');
      collapseElements.forEach((element) => {
        element.classList.remove('show');
      });
    }
    
    // Toggle the side navigation when window is resized below 480px
    if (window.innerWidth < 480 && !document.querySelector(".sidebar").classList.contains("toggled")) {
      document.body.classList.add("sidebar-toggled");
      document.querySelector(".sidebar").classList.add("toggled");
      const collapseElements = document.querySelectorAll('.sidebar .collapse');
      collapseElements.forEach((element) => {
        element.classList.remove('show');
      });
    }
  });
  
  // Prevent the content wrapper from scrolling when the fixed side navigation hovered over
  const sidebar = document.querySelector('body.fixed-nav .sidebar');
  sidebar.addEventListener('mousewheel', function(e) {
    if (window.innerWidth > 768) {
      this.scrollTop += e.deltaY;
      e.preventDefault();
    }
  });
  
  