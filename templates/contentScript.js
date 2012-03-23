/*var link = document.createElement('link');
link.href =  chrome.extension.getURL('contentScript.css');
  //chrome-extension://<extension id>/main.css
link.rel = 'stylesheet';
document.documentElement.insertBefore(link);
*/

//popup for each keyword click
$('<div class="popup"><div class="popup_keyword1"></div><div class="popup_keyword2">popup of keyword2</div><div class="popup_keyword3">popup of keyword3</div><div class="popup_keyword4">popup of keyword4</div><div class="popup_keyword5">popup of keyword4</div></div>').appendTo('body');


//layout of bottom extension
$('<div class="layout"><img class="close-image" src="http://residentialsearch.savills.co.uk/Content/Images/icon_close.png" /><img class="gmap" src="http://cdn1.iconfinder.com/data/icons/Mobile-Icons/128/04_maps.png" /><img class="spinner" src="ajax-loader.gif" /><div class="mextension"><div class="keyword1"><p id="keyword1">My extension</p></div><div class="keyword2"><p id="keyword2">video</p></div><div class="keyword3"><p id="keyword3">position</p></div><div class="keyword4"><p id="keyword4">person</p></div><div class="keyword5"><p id="keyword5">Tweets</p><img class="tweet" src="data:image/png;base64,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"/></div><button type="button" id="rifuprevkeyword" style="position: absolute; left: 840px;top: 5px; background-color: white; width: 43px;height: 26px;">Prev</button><button type="button" id="rifunextkeyword" style="position: absolute;left: 840px;top: 43px;background-color: white;width: 43px;height: 26px;">Next</button></div></div>').appendTo('body');

$('.layout').hide();
$('.popup_keyword1').hide();
$('.popup_keyword2').hide();
$('.popup_keyword3').hide();
$('.popup_keyword4').hide();
$('.popup_keyword5').hide();

$(':button').click(function(){
	//alert("button click");
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
});

$('.keyword2').click(function(){
	//alert("in onclick function of keyword2");
	//$('.popup_keyword2').slideToggle();
	if($('.popup_keyword2').is(':visible')){
        	$('.popup_keyword2').slideUp('slow');
        }else{
		$('.popup_keyword2').slideDown('slow');	
	}
	
	$('.popup_keyword1').slideUp('slow');
	$('.popup_keyword3').slideUp('slow');
	$('.popup_keyword4').slideUp('slow');
	$('.popup_keyword5').slideUp('slow');
	
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
});



$('.keyword5').click(function(){
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
});
/*$('.keyword3').click(function(){
	//alert("in onclick function of keyword3");
	$('.popup_keyword3').toggle();
});
$('.keyword4').click(function(){
	//alert("in onclick function of keyword4");
	$('.popup_keyword4').toggle();
});

$('.keyword5').click(function(){
	//alert("in onclick function of keyword4");
	$('.popup_keyword5').toggle();
});*/

/*$(".close-image").click(function(){
   	$(this).parent().hide();
	$(".popup_keyword1").hide();
   	$(".popup_keyword2").hide();
   	$(".popup_keyword3").hide();
   	$(".popup_keyword4").hide();
});
*/

//1)button click 2)call fuction from background.html  sendrequest/onrequest


/*			//w
$('#rifuprevkeyword').click(function(){
	alert("prev button click");
	chrome.extension.sendRequest({"button": "prev"});
});
$('#rifunextkeyword').click(function(){
	alert("next button click");
	chrome.extension.sendRequest({"button": "next"});
});
*/
/*                   //W
$(':button').click(function(){
	alert("button click");
});*/


/* for adding video: need to check
//popup for each keyword click
$('<div class="popup_keyword1">

<object height="240" id="grelated-id-yt-player" type="application/x-shockwave-flash" width="396">
	<param name="movie" value="http://www.youtube.com/v/MsuXnUiwG-Q?enablejsapi=1&amp;version=3&amp;hl=en_US&amp;rel=0"><param name="allowFullScreen" value="true">
	<param name="allowscriptaccess" value="always">
	<embed src="http://www.youtube.com/v/MsuXnUiwG-Q?enablejsapi=1&amp;version=3&amp;hl=en_US&amp;rel=0" type="application/x-shockwave-flash" allowscriptaccess="always" allowfullscreen="true" height="240" width="396">
</object>
</div><div class="popup_keyword2">popup of keyword2</div><div class="popup_keyword3">popup of keyword3</div><div class="popup_keyword4">popup of keyword4</div>').appendTo('body');
*/

