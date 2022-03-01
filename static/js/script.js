// Get the modal
var modal = document.getElementById("myModal");
        
// Get the button that opens the modal
//var btn = document.getElementById("myBtn");
var btn2 = document.getElementById("myBtn2");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal 
//btn.onclick = function() {
//  modal.style.display = "block";
//}
btn2.onclick = function() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

$('.owl-carousel').owlCarousel({
    loop: true,
    margin: 22,
    responsiveClass: true,
    smartSpeed: 1500,
    autoplay: true,
    autoplayTimeout: 4000,
    autoplayHoverPause: true,
    nav: true,
    dots: false,
    navText: ["<i class='fas fa-angle-left nav-btn'></i>", "<i class='fas fa-angle-right nav-btn'></i>"],
    responsive: {
        0: {
            items: 1,
        },
        600: {
            items: 2,
        },
        1200: {
            items: 4,
        }
    }
});

$('.owl-carousel').on('mousewheel', '.owl-stage', function (e) {
    if (e.deltaY > 0) {
        owl.trigger('next.owl');
    } else {
        owl.trigger('prev.owl');
    }
    e.preventDefault();
});

$(window).scroll(function () {
    if ($(window).scrollTop() >= 20) {
        $('nav').addClass('f-nav');
        $('.topbar').addClass('f-top');
    }
    else {
        $('nav').removeClass('f-nav');
        $('.topbar').removeClass('f-top');
    }
});

$(function () {
    $('#bab').click(function () {
        $('html, body').animate({
            scrollTop: 0
        }, 1000);
    });
    $('.nav li a').click(function () {
        if ($('.navbar-collapse').hasClass('in')) {
            $('.navbar-collapse').removeClass('in');
            $('.navbar-collapse').css('height', '0');
        }
    });
});
$(window).scroll(function () {
    if ($(this).scrollTop() > 125) {
        $('.bottom_arrow_btn').css('opacity', '1');
    } else {
        $('.bottom_arrow_btn').css('opacity', '0');
    }
});

$(function () {
    $('nav a').click(function (e) {
        var linkHref = $(this).attr("href");
        var idElement = linkHref.substr(linkHref.indexOf("#"));
        $('html, body').animate({
            scrollTop: $(idElement).offset().top
        }, 1000);
        return false;
    });
});

$(function () {
    $('#bab').click(function () {
        $('html, body').animate({
            scrollTop: 0
        }, 1000);
    });
    $('.nav li a').click(function () {
        if ($('.navbar-collapse').hasClass('in')) {
            $('.navbar-collapse').removeClass('in');
            $('.navbar-collapse').css('height', '0');
        }
    });
});
$(window).scroll(function () {
    if ($(this).scrollTop() > 125) {
        $('.bottom_arrow_btn').css('opacity', '1');
    } else {
        $('.bottom_arrow_btn').css('opacity', '0');
    }
});

$(function () {
            $('nav a').click(function (e) {
                var linkHref = $(this).attr("href");
                var idElement = linkHref.substr(linkHref.indexOf("#"));
                $('html, body').animate({
                    scrollTop: $(idElement).offset().top
                }, 1000);
                return false;
            });
        });