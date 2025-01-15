// Simple router example using location.hash
const navigateTo = (page) => {
    window.location.hash = page;
  };
  
  const handleNavigation = () => {
    const currentPage = window.location.hash.substring(1);
    // Add logic to dynamically load content based on currentPage
  };
  
  window.addEventListener('hashchange', handleNavigation);
  handleNavigation(); // Call on initial load
  