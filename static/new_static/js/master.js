$('.home-carusal').owlCarousel({
	
loop:true,
items:1,
center:true,
margin:50,
nav:true,
autoplay:true,
autoplayTimeout:2000,
navText: ['<span class="fw-bold mx-2 far fa-circle"></span>', '<span class="far fa-circle"></span>'],
URLhashListener:true,
autoplayHoverPause:true,

});

$('.carousel-1').owlCarousel({
loop:true,
margin:10,
nav:true,
navText: ['<span class="fw-bold mx-2 bi bi-arrow-left"></span>', '<span class="bi bi-arrow-right"></span>'],
responsive:{
0:{
items:1
},
600:{
items:3
},
1000:{
items:4
}
}
})

$(".product-page-carusal").owlCarousel({
    loop: true,
    margin: 10,
    nav:true,
    navText: ['<span class="fw-bold mx-2 bi bi-arrow-left"></span>', '<span class="bi bi-arrow-right"></span>'],
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: true,
        },
        600: {
            items: 2,
            nav: true,
        },
        1000: {
            items: 4,
            nav: true,
        },

    },
});

$('.discover-carousel').owlCarousel({
loop:true,
margin:10,
nav:false,
responsive:{
0:{
items:1
},
600:{
items:3
},
1000:{
items:3
}
}
})

$('.drammers-carousel').owlCarousel({
loop:true,
margin:10,
stagePadding: 50,
nav:true,
autoplay:true,
autoplayTimeout:2000,
autoplayHoverPause:true,
navText: ['<span class="fw-bold mx-2 bi bi-arrow-left"></span>', '<span class="bi bi-arrow-right"></span>'],
responsive:{
0:{
items:1
},
600:{
items:2
},
1000:{
items:2
}
}
});


$('.how-we-get').owlCarousel({
	loop:true,
	margin:10,
	nav:true,
	autoplay:true,
	autoplayTimeout:2000,
	autoplayHoverPause:true,
	navText: ['<span class="fw-bold mx-2 bi bi-arrow-left"></span>', '<span class="bi bi-arrow-right"></span>'],
	responsive:{
	0:{
	 items:1
	},
	600:{
	 items:2
	},
	1000:{
	 items:2
	 }
	}
	});
	$('.Rewards-haul').owlCarousel({
	loop:true,
	stagePadding: 90,
	margin:30,
	nav:true,
	autoplay:false,
	navText: ['<span class="fw-bold mx-2 bi bi-arrow-left"></span>', '<span class="bi bi-arrow-right"></span>'],
	responsive:{
	0:{
	 items:1,
	 margin:20,
	 stagePadding: false
	},
	768:{
	 items:2,
	  stagePadding: false
	},
	1000:{
	 items:2
	 }
	}
	});
	
	$('.team-carusal').owlCarousel({
	loop:true,
	margin:10,
	nav:false,
	autoplay:true,
	autoplayTimeout:2000,
	autoplayHoverPause:true,
	responsive:{
	0:{
	 items:1
	},
	600:{
	 items:2
	},
	1000:{
	 items:5
	 }
	}
	});
	
	$('.count').each(function () {
		$(this).prop('Counter',0).animate({
			Counter: $(this).text()
		}, {
			duration: 9500,
			easing: 'swing',
			step: function (now) {
				$(this).text(Math.ceil(now));
			}
		});
	});