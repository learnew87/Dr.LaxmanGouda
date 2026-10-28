document.addEventListener('DOMContentLoaded', () => {
    // -------------------------------------------------------------
    // Theme Switcher with LocalStorage persistence
    // -------------------------------------------------------------
    const themeToggle = document.getElementById('themeToggle');
    const htmlElement = document.documentElement;

    const savedTheme = localStorage.getItem('theme') || 'dark';
    htmlElement.setAttribute('data-theme', savedTheme);

    if (themeToggle) {
        themeToggle.addEventListener('click', () => {
            const currentTheme = htmlElement.getAttribute('data-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            htmlElement.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
        });
    }

    // -------------------------------------------------------------
    // Interactive Deep-Tech Image Slider
    // -------------------------------------------------------------
    const slider = document.getElementById('imageSlider');
    const slides = document.querySelectorAll('.slide-item');
    const dots = document.querySelectorAll('.slider-dot');
    const prevBtn = document.getElementById('prevSlide');
    const nextBtn = document.getElementById('nextSlide');

    if (slider && slides.length > 0) {
        let currentSlide = 0;
        let slideInterval = null;
        const totalSlides = slides.length;

        const showSlide = (index) => {
            // Normalize index
            if (index < 0) {
                currentSlide = totalSlides - 1;
            } else if (index >= totalSlides) {
                currentSlide = 0;
            } else {
                currentSlide = index;
            }

            // Update slide items
            slides.forEach((slide, i) => {
                if (i === currentSlide) {
                    slide.classList.add('active');
                } else {
                    slide.classList.remove('active');
                }
            });

            // Update indicator dots
            dots.forEach((dot, i) => {
                if (i === currentSlide) {
                    dot.classList.add('active');
                } else {
                    dot.classList.remove('active');
                }
            });
        };

        const nextSlide = () => showSlide(currentSlide + 1);
        const prevSlide = () => showSlide(currentSlide - 1);

        if (nextBtn) nextBtn.addEventListener('click', nextSlide);
        if (prevBtn) prevBtn.addEventListener('click', prevSlide);

        dots.forEach((dot) => {
            dot.addEventListener('click', (e) => {
                const targetIndex = parseInt(e.target.dataset.slide, 10);
                showSlide(targetIndex);
            });
        });

        // Auto-play timer
        const startAutoplay = () => {
            if (!slideInterval) {
                slideInterval = setInterval(nextSlide, 5000);
            }
        };

        const stopAutoplay = () => {
            if (slideInterval) {
                clearInterval(slideInterval);
                slideInterval = null;
            }
        };

        // Pause on mouse hover
        slider.addEventListener('mouseenter', stopAutoplay);
        slider.addEventListener('mouseleave', startAutoplay);

        // Touch swipe support for mobile
        let touchStartX = 0;
        let touchEndX = 0;

        slider.addEventListener('touchstart', (e) => {
            touchStartX = e.changedTouches[0].screenX;
            stopAutoplay();
        }, { passive: true });

        slider.addEventListener('touchend', (e) => {
            touchEndX = e.changedTouches[0].screenX;
            if (touchStartX - touchEndX > 50) {
                nextSlide();
            } else if (touchEndX - touchStartX > 50) {
                prevSlide();
            }
            startAutoplay();
        }, { passive: true });

        // Start autoplay on load
        startAutoplay();
    }

    // -------------------------------------------------------------
    // Auto-dismiss alert messages after 5 seconds
    // -------------------------------------------------------------
    const alerts = document.querySelectorAll('.flash-alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.transition = 'opacity 0.6s ease';
            alert.style.opacity = '0';
            setTimeout(() => alert.remove(), 600);
        }, 5000);
    });

    // -------------------------------------------------------------
    // Animate skill progress bars on scroll
    // -------------------------------------------------------------
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const fill = entry.target.querySelector('.progress-bar-fill');
                if (fill && !fill.dataset.animated) {
                    const width = fill.style.width;
                    fill.style.width = '0%';
                    setTimeout(() => {
                        fill.style.width = width;
                        fill.dataset.animated = 'true';
                    }, 100);
                }
            }
        });
    }, { threshold: 0.2 });

    document.querySelectorAll('.skill-card').forEach(card => observer.observe(card));
});
