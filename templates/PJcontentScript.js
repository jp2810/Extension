//popup for each keyword click
$('<div class="popup"><div class="popup_map"></div><div class="popup_keyword1"></div><div class="popup_keyword2">popup of keyword2</div><div class="popup_keyword3">popup of keyword3</div><div class="popup_keyword4">popup of keyword4</div><div class="popup_keyword5">popup of keyword4</div></div>').appendTo('body');

//layout of bottom extension
$('<div class="layout"><img class="close-image" src="http://residentialsearch.savills.co.uk/Content/Images/icon_close.png" /><p class="closetext"style="position:aboslute;top:58px;left:35px;">Close</p><span><img class="gmap" src="http://cdn1.iconfinder.com/data/icons/Mobile-Icons/128/04_maps.png" /><p class="googlemap" style="position:absolute;top:58px;left:35px;">Google Map</p></span><div class="ball1"></div><div class="mextension"><div class="keyword1"><p id="keyword1"></p></div><div class="keyword2"><p id="keyword2">video</p></div><div class="keyword3"><p id="keyword3"></p></div><div class="keyword4"><p id="keyword4"></p></div><div class="keyword5"><p id="keyword5"></p><img class="twitter" src="http://cdn1.iconfinder.com/data/icons/colorstroked/Twitter.png" /></div><button type="button" id="rifuprevkeyword" style="position: absolute; left: 863px;top: -17px; background-color: white; width: 43px;height: 26px;">Prev</button><button type="button" id="rifunextkeyword" style="position: absolute;left: 863px;top: 25px;background-color: white;width: 43px;height: 26px;">Next</button></div></div>').appendTo('body');

$('.mextension').hide();
$('.layout').hide();
$('.popup_keyword1').hide();
$('.popup_keyword2').hide();
$('.popup_keyword3').hide();
$('.popup_keyword4').hide();
$('.popup_keyword5').hide();
$('.popup_map').hide();
$('p.googlemap').hide();
$('p.closetext').hide();

$(':button').click(function(){
	var s=this.id;
	if(s=="rifuprevkeyword")
	{
		//alert("prev button click");
		chrome.extension.sendRequest({"button": "prev"});
	}
	else if(s=="rifunextkeyword")
	{
		//alert("next button click");
		chrome.extension.sendRequest({"button": "next"});
	}
});
$('.keyword4').click(function(){
	//alert("in onclick function of keyword4");
	if($('.popup_keyword4').is(':visible')){
        	$('.popup_keyword4').slideUp('slow');
        }else{
		$('.popup_keyword4').slideDown('slow');	
	}
	
	$('.popup_keyword1').slideUp('slow');
	$('.popup_keyword2').slideUp('slow');
	$('.popup_keyword3').slideUp('slow');
	$('.popup_keyword5').slideUp('slow');
	$('.popup_map').slideUp('slow');
});

$('.keyword1').click(function(){
	//alert("in onclick function of keyword1");
	//check if any popup is currently open,close that by removing the class
	if($('.popup_keyword1').is(':visible')){
        	$('.popup_keyword1').slideUp('slow');
        }else{
		$('.popup_keyword1').slideDown('slow');	
	}
	$('.popup_keyword2').slideUp('slow');
	$('.popup_keyword3').slideUp('slow');
	$('.popup_keyword4').slideUp('slow');
	$('.popup_keyword5').slideUp('slow');	
	$('.popup_map').slideUp('slow');
});

$('.keyword2').click(function(){
	//alert("in onclick function of keyword2");
	if($('.popup_keyword2').is(':visible')){
        	$('.popup_keyword2').slideUp('slow');
        }else{
		$('.popup_keyword2').slideDown('slow');	
	}
	
	$('.popup_keyword1').slideUp('slow');
	$('.popup_keyword3').slideUp('slow');
	$('.popup_keyword4').slideUp('slow');
	$('.popup_keyword5').slideUp('slow');
	$('.popup_map').slideUp('slow');
});

$('.keyword3').click(function(){
	if($('.popup_keyword3').is(':visible')){
        	$('.popup_keyword3').slideUp('slow');
        }else{
		$('.popup_keyword3').slideDown('slow');	
	}
	$('.popup_keyword1').slideUp('slow');
	$('.popup_keyword2').slideUp('slow');
	$('.popup_keyword4').slideUp('slow');
	$('.popup_keyword5').slideUp('slow');
	$('.popup_map').slideUp('slow');
});

$('.gmap').click(function(){
	//alert("in onclick function of keyword4");
	if($('.popup_map').is(':visible')){
        	$('.popup_map').slideUp('slow');
        }else{
		$('.popup_map').slideDown('slow');	
	}
	
	$('.popup_keyword1').slideUp('slow');
	$('.popup_keyword2').slideUp('slow');
	$('.popup_keyword3').slideUp('slow');
	$('.popup_keyword5').slideUp('slow');
	$('.popup_keyword4').slideUp('slow');
});


$('.twitter').click(function(){
	//alert("in onclick function of keyword4");
	if($('.popup_keyword5').is(':visible')){
        	$('.popup_keyword5').slideUp('slow');
        }else{
		$('.popup_keyword5').slideDown('slow');	
	}
	$('.popup_keyword1').slideUp('slow');
	$('.popup_keyword2').slideUp('slow');
	$('.popup_keyword3').slideUp('slow');
	$('.popup_keyword4').slideUp('slow');
});

$(".close-image").click(function(){
   	 $(this).parent().slideUp('slow');
   	 $(".popup_keyword1").slideUp('slow');
   	 $(".popup_keyword2").slideUp('slow');
   	 $(".popup_keyword3").slideUp('slow');
   	 $(".popup_keyword4").slideUp('slow');
         $(".popup_keyword5").slideUp('slow');
         $(".keyword1").hide('slow');
         $(".keyword2").hide('slow');
         $(".keyword3").hide('slow');
	 $(".keyword4").hide('slow');
});


$('.gmap').mouseenter(function(){
		$('p.googlemap').fadeIn();	
	});
$('.gmap').mouseleave(function(){
		$('p.googlemap').fadeOut();	
	});

$('.close-image').mousehover(function(){
		$('p.closetext').fadeIn();	
	});



