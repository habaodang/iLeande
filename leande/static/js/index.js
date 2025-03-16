// Simple script for smooth scrolling between sections when clicking nav links
const links = document.querySelectorAll('nav ul li a');
links.forEach(link => {
    link.addEventListener('click', function(e) {
        e.preventDefault();
        const targetId = this.getAttribute('href').substring(1);
        const targetSection = document.getElementById(targetId);

        window.scrollTo({
            top: targetSection.offsetTop - 60,  // Adjust for the fixed header
            behavior: 'smooth'
        });
    });
});
