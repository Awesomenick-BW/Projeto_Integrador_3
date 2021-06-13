var slides = document.querySelectorAll('.slide');
var butns = document.querySelectorAll('.butn');
let currentSlide = 1;

// Javascript for image slider manual navigation
var manualNav = function(manual){
slides.forEach((slide) => {
    slide.classList.remove('active');

    butns.forEach((butn) => {
    butn.classList.remove('active');
    });
});

slides[manual].classList.add('active');
butns[manual].classList.add('active');
}

butns.forEach((butn, i) => {
butn.addEventListener("click", () => {
    manualNav(i);
    currentSlide = i;
});
});

// Javascript for image slider autoplay navigation
var repeat = function(activeClass){
let active = document.getElementsByClassName('active');
let i = 1;

var repeater = () => {
    setTimeout(function(){
    [...active].forEach((activeSlide) => {
        activeSlide.classList.remove('active');
    });

    slides[i].classList.add('active');
    butns[i].classList.add('active');
    i++;

    if(slides.length == i){
    i = 0;
    }
    if(i >= slides.length){
    return;
    }
    repeater();
}, 7000);
}
repeater();
}
repeat();