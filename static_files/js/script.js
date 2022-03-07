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
$("span").on("click", function() {
    modal.style.display = "none";
})

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
    navText: ["<img src='{% static '/images/arrow-left.png' %}>", "<img src='{% static '/images/arrow-right.png' %}'>"],
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

$('.owl-carousel').on('mousewheel', '.owl-stage', function(e) {
    if (e.deltaY > 0) {
        owl.trigger('next.owl');
    } else {
        owl.trigger('prev.owl');
    }
    e.preventDefault();
});

// $(window).scroll(function () {
//     if ($(window).scrollTop() >= 20) {
//         $('nav').addClass('f-nav');
//         $('.topbar').addClass('f-top');
//     }
//     else {
//         $('nav').removeClass('f-nav');
//         $('.topbar').removeClass('f-top');
//     }
// });

// $(function () {
//     $('#bab').click(function () {
//         $('html, body').animate({
//             scrollTop: 0
//         }, 1000);
//     });
// });

// $(function () {
//     $('nav a').click(function (e) {
//         var linkHref = $(this).attr("href");
//         var idElement = linkHref.substr(linkHref.indexOf("#"));
//         $('html, body').animate({
//             scrollTop: $(idElement).offset().top
//         }, 1000);
//         return false;
//     });
// });

$(function() {
    $('#bab').click(function() {
        $('html, body').animate({
            scrollTop: 0
        }, 1000);
    });
    $('.nav li a').click(function() {
        if ($('.navbar-collapse').hasClass('in')) {
            $('.navbar-collapse').removeClass('in');
            $('.navbar-collapse').css('height', '0');
        }
    });
});
// $(window).scroll(function () {
//     if ($(this).scrollTop() > 125) {
//         $('.bottom_arrow_btn').css('opacity', '1');
//     } else {
//         $('.bottom_arrow_btn').css('opacity', '0');
//     }
// });

$(function() {
    $('nav a').click(function(e) {
        var linkHref = $(this).attr("href");
        var idElement = linkHref.substr(linkHref.indexOf("#"));
        $('html, body').animate({
            scrollTop: $(idElement).offset().top
        }, 1000);
        return false;
    });
});

function shuffle(array) {
    var currentIndex = array.length,
        randomIndex;

    // While there remain elements to shuffle...
    while (0 !== currentIndex) {
        // Pick a remaining element...
        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex--;

        // And swap it with the current element.
        [array[currentIndex], array[randomIndex]] = [
            array[randomIndex],
            array[currentIndex],
        ];
    }

    return array;
}

function spin() {
    // Play the sound
    wheel.play();
    // Initialize variable
    const box = document.getElementById("box");
    const element = document.getElementById("mainbox");
    let SelectedItem = "";

    // Shuffle 450 because class box1 has been increased by 90 degrees in the beginning.
    // minus 40 per item so that the arrow position fits in the middle.
    // Each item has a 12.5% ​​win except the bike item which only has about a 4% chance of winning.
    // Items ipad and samsung tab will never win.
    // let Bike = shuffle([2210]); //Probability : 33% or 1/3
    let MagicRoaster = shuffle([1890, 2250, 2610]);
    let Sepeda = shuffle([1850, 2210, 2570]); //Probability : 100%
    let RiceCooker = shuffle([1810, 2170, 2530]);
    let LunchBox = shuffle([1770, 2130, 2490]);
    let Sanken = shuffle([1750, 2110, 2470]);
    let Electrolux = shuffle([1630, 1990, 2350]);
    let JblSpeaker = shuffle([1570, 1930, 2290]);

    // Random shape
    let Hasil = shuffle([
        MagicRoaster[0],
        Sepeda[0],
        RiceCooker[0],
        LunchBox[0],
        Sanken[0],
        Electrolux[0],
        JblSpeaker[0],
    ]);
    // console.log(Hasil[0]);

    // Get the value of the selected item
    if (MagicRoaster.includes(Hasil[0])) SelectedItem = "User Name 3";
    if (Sepeda.includes(Hasil[0])) SelectedItem = "User Name 4";
    if (RiceCooker.includes(Hasil[0])) SelectedItem = "User Name 5";
    if (LunchBox.includes(Hasil[0])) SelectedItem = "User Name 6";
    if (Sanken.includes(Hasil[0])) SelectedItem = "User Name 7";
    if (Electrolux.includes(Hasil[0])) SelectedItem = "User Name 8";
    if (JblSpeaker.includes(Hasil[0])) SelectedItem = "User Name 2";

    // Process
    box.style.setProperty("transition", "all ease 5s");
    box.style.transform = "rotate(" + Hasil[0] + "deg)";
    element.classList.remove("animate");
    setTimeout(function() {
        element.classList.add("animate");
    }, 5000);

    // Show Alert
    setTimeout(function() {
        applause.play();
        swal(
            "Congratulations",
            //"You Won The " + SelectedItem + ".",
            SelectedItem,
            "success"
        );
    }, 5500);

    // Delay and set to normal state
    setTimeout(function() {
        box.style.setProperty("transition", "initial");
        box.style.transform = "rotate(90deg)";
    }, 6000);
}