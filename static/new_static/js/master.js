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


// quantity button

var QtyInput = (function () {
	var $qtyInputs = $(".qty-input");

	if (!$qtyInputs.length) {
		return;
	}

	var $inputs = $qtyInputs.find(".product-qty");
	//var $countBtn = $qtyInputs.find(".qty-count");
	var $countBtn = "";
	var qtyMin = parseInt($inputs.attr("min"));
	var qtyMax = parseInt($inputs.attr("max"));

	$inputs.change(function () {
		var $this = $(this);
		var $minusBtn = $this.siblings(".qty-count--minus");
		var $addBtn = $this.siblings(".qty-count--add");
		var qty = parseInt($this.val());

		if (isNaN(qty) || qty <= qtyMin) {
			$this.val(qtyMin);
			$minusBtn.attr("disabled", true);
		} else {
			$minusBtn.attr("disabled", false);
			
			if(qty >= qtyMax){
				$this.val(qtyMax);
				$addBtn.attr('disabled', true);
			} else {
				$this.val(qty);
				$addBtn.attr('disabled', false);
			}
		}
	});

	$countBtn.click(function () {
		var operator = this.dataset.action;
		var $this = $(this);
		var $input = $this.siblings(".product-qty");
		var qty = parseInt($input.val());

		if (operator == "add") {
			qty += 1;
			if (qty >= qtyMin + 1) {
				$this.siblings(".qty-count--minus").attr("disabled", false);
			}

			if (qty >= qtyMax) {
				$this.attr("disabled", true);
			}
		} else {
			qty = qty <= qtyMin ? qtyMin : (qty -= 1);
			
			if (qty == qtyMin) {
				$this.attr("disabled", true);
			}

			if (qty < qtyMax) {
				$this.siblings(".qty-count--add").attr("disabled", false);
			}
		}

		$input.val(qty);
	});
})();
