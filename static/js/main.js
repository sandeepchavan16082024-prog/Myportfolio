(function () {
    "use strict";

    // ---------- Preloader ----------
    const preloader = document.getElementById("preloader");
    const hidePreloader = () => preloader.classList.add("done");
    window.addEventListener("load", hidePreloader);
    setTimeout(hidePreloader, 2200);

    // ---------- Scroll progress bar ----------
    const progressBar = document.getElementById("scroll-progress");
    const updateProgress = () => {
        const max = document.documentElement.scrollHeight - window.innerHeight;
        progressBar.style.width = (max > 0 ? (window.scrollY / max) * 100 : 0) + "%";
    };
    window.addEventListener("scroll", updateProgress, { passive: true });
    updateProgress();

    // ---------- Cursor glow ----------
    const glow = document.getElementById("cursor-glow");
    let glowX = -500, glowY = -500, targetX = -500, targetY = -500;
    window.addEventListener("mousemove", (e) => {
        targetX = e.clientX;
        targetY = e.clientY;
        document.body.classList.add("has-cursor");
    }, { passive: true });
    (function glowLoop() {
        glowX += (targetX - glowX) * 0.12;
        glowY += (targetY - glowY) * 0.12;
        glow.style.transform = `translate(${glowX}px, ${glowY}px)`;
        requestAnimationFrame(glowLoop);
    })();

    // ---------- Theme toggle ----------
    const themeBtn = document.getElementById("theme-toggle");
    const savedTheme = localStorage.getItem("theme");
    if (savedTheme) document.documentElement.setAttribute("data-theme", savedTheme);
    themeBtn.addEventListener("click", () => {
        const current = document.documentElement.getAttribute("data-theme");
        const next = current === "light" ? "dark" : "light";
        document.documentElement.setAttribute("data-theme", next);
        localStorage.setItem("theme", next);
    });

    // ---------- Navbar scroll state ----------
    const navbar = document.getElementById("navbar");
    const onScroll = () => {
        navbar.classList.toggle("scrolled", window.scrollY > 30);
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();

    // ---------- Mobile menu ----------
    const hamburger = document.getElementById("hamburger");
    const navLinks = document.getElementById("nav-links");
    hamburger.addEventListener("click", () => {
        hamburger.classList.toggle("open");
        navLinks.classList.toggle("open");
    });
    navLinks.querySelectorAll("a").forEach((link) =>
        link.addEventListener("click", () => {
            hamburger.classList.remove("open");
            navLinks.classList.remove("open");
        })
    );

    // ---------- Typewriter effect ----------
    const el = document.getElementById("typewriter");
    const phrases = [
        "Data Analyst & SCADA Specialist",
        "ETL Pipeline Developer",
        "Power BI & Tableau Storyteller",
        "Python · SQL · VBA Automation",
        "AI-Assisted Development",
    ];
    let phraseIdx = 0, charIdx = 0, deleting = false;

    function type() {
        const current = phrases[phraseIdx];
        if (!deleting) {
            charIdx++;
            el.textContent = current.slice(0, charIdx);
            if (charIdx === current.length) {
                deleting = true;
                setTimeout(type, 1800);
                return;
            }
            setTimeout(type, 55);
        } else {
            charIdx--;
            el.textContent = current.slice(0, charIdx);
            if (charIdx === 0) {
                deleting = false;
                phraseIdx = (phraseIdx + 1) % phrases.length;
                setTimeout(type, 350);
                return;
            }
            setTimeout(type, 28);
        }
    }
    if (el) type();

    // ---------- Reveal on scroll ----------
    const revealEls = document.querySelectorAll(".reveal");
    const revealObserver = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add("visible");
                    revealObserver.unobserve(entry.target);
                }
            });
        },
        { threshold: 0.12 }
    );
    revealEls.forEach((el, i) => {
        el.style.transitionDelay = (i % 4) * 0.08 + "s";
        revealObserver.observe(el);
    });

    // ---------- Animated counters ----------
    const stats = document.querySelectorAll(".stat-value");
    const countObserver = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (!entry.isIntersecting) return;
                const el = entry.target;
                countObserver.unobserve(el);
                const target = parseInt(el.dataset.target, 10);
                const suffix = el.dataset.suffix || "";
                const duration = 1400;
                const start = performance.now();
                function tick(now) {
                    const p = Math.min((now - start) / duration, 1);
                    const eased = 1 - Math.pow(1 - p, 3);
                    el.textContent = Math.floor(eased * target) + suffix;
                    if (p < 1) requestAnimationFrame(tick);
                }
                requestAnimationFrame(tick);
            });
        },
        { threshold: 0.4 }
    );
    stats.forEach((s) => countObserver.observe(s));

    // ---------- Active nav link highlighting ----------
    const sections = document.querySelectorAll("section[id]");
    const linkMap = {};
    navLinks.querySelectorAll("a[href^='#']").forEach((a) => {
        const id = a.getAttribute("href").slice(1);
        if (id && id !== "hero") linkMap[id] = a;
    });
    const activeObserver = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting && linkMap[entry.target.id]) {
                    Object.values(linkMap).forEach((a) => (a.style.color = ""));
                    linkMap[entry.target.id].style.color = "#38bdf8";
                }
            });
        },
        { rootMargin: "-40% 0px -55% 0px" }
    );
    sections.forEach((s) => activeObserver.observe(s));

    // ---------- 3D tilt + spotlight ----------
    const tiltEls = document.querySelectorAll("[data-tilt]");
    const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    const isTouch = window.matchMedia("(hover: none)").matches;
    if (reduceMotion || isTouch) {
        tiltEls.forEach((el) => el.classList.remove("tilt"));
    } else {
        tiltEls.forEach((el) => {
            el.classList.add("tilt");
            let rafId = null;
            el.addEventListener("mousemove", (e) => {
                const rect = el.getBoundingClientRect();
                const px = (e.clientX - rect.left) / rect.width;
                const py = (e.clientY - rect.top) / rect.height;
                const mx = e.clientX - rect.left;
                const my = e.clientY - rect.top;
                if (rafId) cancelAnimationFrame(rafId);
                rafId = requestAnimationFrame(() => {
                    el.style.setProperty("--ry", ((px - 0.5) * 10).toFixed(2) + "deg");
                    el.style.setProperty("--rx", ((0.5 - py) * 10).toFixed(2) + "deg");
                    el.style.setProperty("--ty", "-4px");
                    el.style.setProperty("--mx", mx + "px");
                    el.style.setProperty("--my", my + "px");
                });
            });
            el.addEventListener("mouseleave", () => {
                if (rafId) cancelAnimationFrame(rafId);
                el.classList.add("tilt-static");
                el.style.setProperty("--rx", "0deg");
                el.style.setProperty("--ry", "0deg");
                el.style.setProperty("--ty", "0px");
                setTimeout(() => el.classList.remove("tilt-static"), 500);
            });
        });
    }

    // ---------- Spotlight follow (non-tilt cards) ----------
    document.querySelectorAll(".spotlight:not([data-tilt])").forEach((el) => {
        el.addEventListener("mousemove", (e) => {
            const rect = el.getBoundingClientRect();
            el.style.setProperty("--mx", e.clientX - rect.left + "px");
            el.style.setProperty("--my", e.clientY - rect.top + "px");
        });
    });

    // ---------- Magnetic buttons ----------
    if (!reduceMotion && !isTouch) {
        document.querySelectorAll(".btn").forEach((btn) => {
            btn.addEventListener("mousemove", (e) => {
                const rect = btn.getBoundingClientRect();
                const x = (e.clientX - rect.left - rect.width / 2) * 0.22;
                const y = (e.clientY - rect.top - rect.height / 2) * 0.35;
                btn.style.transform = `translate(${x.toFixed(1)}px, ${y.toFixed(1)}px)`;
            });
            btn.addEventListener("mouseleave", () => {
                btn.style.transform = "";
            });
        });
    }

    // ---------- Parallax orbs on scroll ----------
    const orbs = document.querySelectorAll(".orb");
    const onScrollParallax = () => {
        const y = window.scrollY;
        orbs.forEach((orb, i) => {
            orb.style.transform = `translateY(${y * (i % 2 === 0 ? -0.06 : 0.05)}px)`;
        });
    };
    window.addEventListener("scroll", onScrollParallax, { passive: true });

    // ---------- Back to top ----------
    const backToTop = document.getElementById("back-to-top");
    window.addEventListener(
        "scroll",
        () => {
            backToTop.classList.toggle("show", window.scrollY > 600);
        },
        { passive: true }
    );
    backToTop.addEventListener("click", () => window.scrollTo({ top: 0, behavior: "smooth" }));
})();