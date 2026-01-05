/* =========================================
   AEO Proposal Integration Logic
   Adapts original script.js for the landing page
   ========================================= */

document.addEventListener('DOMContentLoaded', () => {
    // Wait for the content to be fully loaded/injected
    setTimeout(() => {
        initAeoTechTabs();
        initAeoCounterAnimations();
        initAeoCollisionAnimation();
        initAeoScrollAnimations();
    }, 500); // Slight delay to ensure DOM update if dynamically injected
});

/* ===== Tech Tabs Logic ===== */
function initAeoTechTabs() {
    const tabs = document.querySelectorAll('.aeo-proposal-wrapper .tech-tab');
    
    if (tabs.length === 0) return;

    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            // Remove active from all tabs
            tabs.forEach(t => t.classList.remove('active'));
            
            // Add active to clicked tab
            tab.classList.add('active');

            // Hide all contents
            const wrapper = tab.closest('.aeo-proposal-wrapper');
            const contents = wrapper.querySelectorAll('.tech-content');
            contents.forEach(c => c.classList.remove('active'));

            // Show target content
            const targetId = `tab-${tab.dataset.tab}`;
            const targetContent = document.getElementById(targetId);
            if (targetContent) {
                targetContent.classList.add('active');
            }
        });
    });
}

/* ===== Counter Animations ===== */
function initAeoCounterAnimations() {
    const counters = document.querySelectorAll('.aeo-proposal-wrapper .stat-number');
    
    if (counters.length === 0) return;

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const counter = entry.target;
                const target = parseFloat(counter.dataset.count);
                animateAeoCounter(counter, target);
                observer.unobserve(counter);
            }
        });
    }, { threshold: 0.5 });

    counters.forEach(counter => observer.observe(counter));
}

function animateAeoCounter(element, target) {
    const duration = 2000;
    const start = 0;
    const startTime = performance.now();
    const isDecimal = target % 1 !== 0;
    const suffix = element.dataset.suffix || '';

    function update(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        const easeOutExpo = progress === 1 ? 1 : 1 - Math.pow(2, -10 * progress);
        const current = start + (target - start) * easeOutExpo;

        if (isDecimal) {
            element.textContent = current.toFixed(1) + suffix;
        } else {
            element.textContent = Math.floor(current).toLocaleString() + suffix;
        }

        if (progress < 1) {
            requestAnimationFrame(update);
        }
    }

    requestAnimationFrame(update);
}

/* ===== Collision Animation ===== */
function initAeoCollisionAnimation() {
    const container = document.querySelector('.aeo-proposal-wrapper .collision-container');
    
    if (!container) return;

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                container.classList.add('animate');
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.3 });

    observer.observe(container);
}

/* ===== Scroll Animations (Fade-Up) ===== */
function initAeoScrollAnimations() {
    const elements = document.querySelectorAll('.aeo-proposal-wrapper .fade-up');
    
    if (elements.length === 0) return;

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                
                // Stagger children like cards
                const children = entry.target.querySelectorAll('.glass-card, .stat-card, .roi-card, .comparison-card');
                children.forEach((child, i) => {
                    child.style.transitionDelay = `${i * 0.1}s`;
                    child.classList.add('visible'); // Reuse visible class for opacity 1
                });
                
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    elements.forEach(el => observer.observe(el));
}
