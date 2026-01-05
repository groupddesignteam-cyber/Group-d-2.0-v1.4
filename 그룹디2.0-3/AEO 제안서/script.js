/* =========================================
   그룹디 AEO 제안서 v2.0 - Enhanced Interactions
   Premium Healthcare Marketing Proposal
   ========================================= */

document.addEventListener('DOMContentLoaded', () => {
  // Initialize modules (simplified - no 3D tilt or parallax)
  initScrollAnimations();
  initCounterAnimations();
  initTechTabs();
  initSmoothScroll();
  initCollisionAnimation();
  // initCardTiltEffect(); // Disabled for cleaner look
  // initParallaxHero();   // Disabled for cleaner look
  // initButtonRipple();   // Disabled for cleaner look

  // Fix ROI icons if broken (encoding issue fallback)
  setTimeout(() => {
    const roiLabels = document.querySelectorAll('.roi-label');
    roiLabels.forEach(label => {
      const card = label.closest('.roi-card');
      if (card) {
        const icon = card.querySelector('.roi-icon');
        if (icon) {
          if (label.textContent.includes('진성 환자')) icon.innerHTML = '📈';
          if (label.textContent.includes('디지털 자산')) icon.innerHTML = '💎';
        }
      }
    });
  }, 100);

  console.log('🚀 그룹디 AEO 제안서 v3.0 로드 완료');
});

/* ===== Collision Animation (ChatGPT/Gemini vs Naver) ===== */
function initCollisionAnimation() {
  const collisionContainer = document.querySelector('.collision-container');

  if (!collisionContainer) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        // Add animate class to trigger the collision animation
        setTimeout(() => {
          collisionContainer.classList.add('animate');
        }, 300);

        // Only trigger once
        observer.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.3,
    rootMargin: '0px'
  });

  observer.observe(collisionContainer);
}

/* ===== Scroll Animations with Stagger ===== */
function initScrollAnimations() {
  const observerOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.05
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');

        // Stagger animation for direct children cards
        const children = entry.target.querySelectorAll('.glass-card, .stat-card, .timeline-item, .roi-card, .comparison-card');
        children.forEach((child, i) => {
          child.style.transitionDelay = `${i * 0.15}s`;
          child.classList.add('card-visible');
        });

        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  // Observe all fade-up elements
  document.querySelectorAll('.fade-up').forEach(el => {
    observer.observe(el);
  });

  // Also directly observe stat cards for immediate visibility
  document.querySelectorAll('.stat-card').forEach(card => {
    const cardObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('card-visible');
          cardObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1 });
    cardObserver.observe(card);
  });
}

/* ===== Enhanced Counter Animations ===== */
function initCounterAnimations() {
  const counters = document.querySelectorAll('.stat-number');

  const counterObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const counter = entry.target;
        const target = parseFloat(counter.dataset.count);
        animateCounter(counter, target);
        counterObserver.unobserve(counter);
      }
    });
  }, { threshold: 0.5 });

  counters.forEach(counter => counterObserver.observe(counter));
}

function animateCounter(element, target) {
  const duration = 2500;
  const start = 0;
  const startTime = performance.now();
  const isDecimal = target % 1 !== 0;
  const suffix = element.dataset.suffix || '%';

  function update(currentTime) {
    const elapsed = currentTime - startTime;
    const progress = Math.min(elapsed / duration, 1);

    // Enhanced easing function (ease-out-expo with bounce)
    const easeOutExpo = progress === 1 ? 1 : 1 - Math.pow(2, -10 * progress);
    const current = start + (target - start) * easeOutExpo;

    if (isDecimal) {
      element.textContent = current.toFixed(1) + suffix;
    } else {
      element.textContent = Math.floor(current) + suffix;
    }

    // Add pulse effect when counter finishes
    if (progress >= 1) {
      element.style.animation = 'counter-complete 0.5s ease';
      return;
    }

    requestAnimationFrame(update);
  }

  requestAnimationFrame(update);
}

// Add keyframe for counter complete animation
const style = document.createElement('style');
style.textContent = `
  @keyframes counter-complete {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.1); }
  }
`;
document.head.appendChild(style);

/* ===== Tech Tabs with Smooth Transition ===== */
function initTechTabs() {
  const tabs = document.querySelectorAll('.tech-tab');
  const contents = document.querySelectorAll('.tech-content');

  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      // Remove active from all tabs with transition
      tabs.forEach(t => {
        t.classList.remove('active');
        t.style.transform = 'scale(1)';
      });

      // Add active to clicked tab with animation
      tab.classList.add('active');
      tab.style.transform = 'scale(1.05)';
      setTimeout(() => {
        tab.style.transform = 'scale(1)';
      }, 200);

      // Fade out current content
      const currentActive = document.querySelector('.tech-content.active');
      if (currentActive) {
        currentActive.style.opacity = '0';
        currentActive.style.transform = 'translateY(20px)';

        setTimeout(() => {
          currentActive.classList.remove('active');

          // Show new content
          const targetId = `tab-${tab.dataset.tab}`;
          const newContent = document.getElementById(targetId);
          newContent.classList.add('active');

          // Fade in new content
          setTimeout(() => {
            newContent.style.opacity = '1';
            newContent.style.transform = 'translateY(0)';
          }, 50);
        }, 300);
      }
    });
  });

  // Initialize content transitions
  contents.forEach(content => {
    content.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
    if (content.classList.contains('active')) {
      content.style.opacity = '1';
      content.style.transform = 'translateY(0)';
    }
  });
}

/* ===== Smooth Scroll with Offset ===== */
function initSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        const offsetTop = target.offsetTop - 50;
        window.scrollTo({
          top: offsetTop,
          behavior: 'smooth'
        });
      }
    });
  });
}

/* ===== 3D Card Tilt Effect ===== */
function initCardTiltEffect() {
  const cards = document.querySelectorAll('.glass-card, .comparison-card');

  cards.forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;

      const centerX = rect.width / 2;
      const centerY = rect.height / 2;

      const rotateX = (y - centerY) / 20;
      const rotateY = (centerX - x) / 20;

      card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-8px)`;
    });

    card.addEventListener('mouseleave', () => {
      card.style.transform = 'perspective(1000px) rotateX(0) rotateY(0) translateY(0)';
    });
  });
}

/* ===== Parallax Hero Effect ===== */
function initParallaxHero() {
  const hero = document.querySelector('.hero');
  const orbs = document.querySelectorAll('.hero-orb');

  window.addEventListener('scroll', () => {
    const scrolled = window.pageYOffset;

    if (hero && scrolled < window.innerHeight) {
      // Parallax for hero content
      const heroContent = hero.querySelector('.hero-content');
      if (heroContent) {
        heroContent.style.transform = `translateY(${scrolled * 0.3}px)`;
        heroContent.style.opacity = 1 - (scrolled / window.innerHeight);
      }

      // Parallax for orbs
      orbs.forEach((orb, index) => {
        const speed = (index + 1) * 0.1;
        orb.style.transform = `translateY(${scrolled * speed}px)`;
      });
    }
  });

  // Mouse move effect for orbs
  hero.addEventListener('mousemove', (e) => {
    const mouseX = e.clientX / window.innerWidth - 0.5;
    const mouseY = e.clientY / window.innerHeight - 0.5;

    orbs.forEach((orb, index) => {
      const speed = (index + 1) * 30;
      orb.style.transform = `translate(${mouseX * speed}px, ${mouseY * speed}px)`;
    });
  });
}

/* ===== Button Ripple Effect ===== */
function initButtonRipple() {
  document.querySelectorAll('.btn').forEach(btn => {
    btn.addEventListener('click', function (e) {
      const rect = this.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;

      const ripple = document.createElement('span');
      ripple.style.cssText = `
        position: absolute;
        width: 4px;
        height: 4px;
        background: rgba(255, 255, 255, 0.5);
        border-radius: 50%;
        transform: scale(0);
        animation: ripple 0.6s linear;
        left: ${x}px;
        top: ${y}px;
        pointer-events: none;
      `;

      this.appendChild(ripple);

      setTimeout(() => ripple.remove(), 600);
    });

    // Add hover glow effect
    btn.addEventListener('mouseenter', function () {
      this.style.boxShadow = '0 20px 60px rgba(59, 130, 246, 0.6)';
    });

    btn.addEventListener('mouseleave', function () {
      this.style.boxShadow = '';
    });
  });
}

// Add ripple keyframe
const rippleStyle = document.createElement('style');
rippleStyle.textContent = `
  @keyframes ripple {
    to {
      transform: scale(100);
      opacity: 0;
    }
  }
`;
document.head.appendChild(rippleStyle);

/* ===== Comparison Card Animation ===== */
window.addEventListener('load', () => {
  // Animate comparison arrow
  const arrow = document.querySelector('.comparison-arrow');
  if (arrow) {
    setInterval(() => {
      arrow.style.transform = 'translateX(10px) scale(1.1)';
      setTimeout(() => {
        arrow.style.transform = 'translateX(0) scale(1)';
      }, 300);
    }, 2000);
  }
});

/* ===== Highlight Text Animation on Scroll ===== */
function initHighlightAnimation() {
  const highlights = document.querySelectorAll('.highlight-marker');

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.backgroundSize = '100% 40%';
      }
    });
  }, { threshold: 0.5 });

  highlights.forEach(el => {
    el.style.backgroundSize = '0% 40%';
    el.style.transition = 'background-size 0.8s ease';
    observer.observe(el);
  });
}

// Initialize highlight animation after DOM loaded
setTimeout(initHighlightAnimation, 500);

/* ===== Print Optimization ===== */
window.addEventListener('beforeprint', () => {
  // Expand all sections for print
  document.querySelectorAll('.fade-up').forEach(el => {
    el.classList.add('visible');
    el.style.opacity = '1';
    el.style.transform = 'none';
  });

  document.querySelectorAll('.glass-card, .comparison-card').forEach(el => {
    el.style.opacity = '1';
    el.style.transform = 'none';
  });

  document.querySelectorAll('.tech-content').forEach(content => {
    content.style.display = 'block';
    content.style.opacity = '1';
  });
});

/* ===== Number with Decimal Support ===== */
function formatNumber(num) {
  if (num % 1 !== 0) {
    return num.toFixed(1);
  }
  return Math.floor(num);
}
