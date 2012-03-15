/*var link = document.createElement('link');
link.href =  chrome.extension.getURL('contentScript.css');
  //chrome-extension://<extension id>/main.css
link.rel = 'stylesheet';
document.documentElement.insertBefore(link);
*/

//popup for each keyword click
$('<div class="popup"><div class="popup_keyword1"></div><div class="popup_keyword2">popup of keyword2</div><div class="popup_keyword3">popup of keyword3</div><div class="popup_keyword4">popup of keyword4</div></div>').appendTo('body');


//layout of bottom extension
$('<div class="layout"><img class="close-image" src="http://residentialsearch.savills.co.uk/Content/Images/icon_close.png" /><div class="mextension"><button type="button" id="prevkeyword">Prev</button><div class="keyword1"><p id="keyword1">My extension</p></div><div class="keyword2"><p id="keyword2">video</p></div><div class="keyword3"><p id="keyword3">position</p></div><div class="keyword4"><p id="keyword4">person</p></div><div class="keyword5"><p  id="keyword5">keyword5</p></div><button type="button" id="nextkeyword">Next</button><button type="button" id="tweets">tweets</button></div></div>').appendTo('body');

$('.layout').hide();
$('.popup_keyword1').hide();
$('.popup_keyword2').hide();
$('.popup_keyword3').hide();
$('.popup_keyword4').hide();


$('.keyword1').click(function(){
	//alert("in onclick function of keyword1");
	$('.popup_keyword1').toggle();
});
$('.keyword2').click(function(){
	//alert("in onclick function of keyword2");
	$('.popup_keyword2').toggle();
});
$('.keyword3').click(function(){
	//alert("in onclick function of keyword3");
	$('.popup_keyword3').toggle();
});
$('.keyword4').click(function(){
	//alert("in onclick function of keyword4");
	$('.popup_keyword4').toggle();
});
$('#prevkeyword').click(function(){
	//alert("button click");
	chrome.extension.sendRequest({"button": "prev"});
});
$('#nextkeyword').click(function(){
	//alert("button click");
	chrome.extension.sendRequest({"button": "next"});
});
$('#tweets').click(function(){
	//alert("button click");
	chrome.extension.sendRequest({"button": "tweets"});
});
$(".close-image").click(function(){
   	$(this).parent().hide();
	$(".popup_keyword1").hide();
   	$(".popup_keyword2").hide();
   	$(".popup_keyword3").hide();
   	$(".popup_keyword4").hide();
});

//1)button click 2)call fuction from background.html  sendrequest/onrequest

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

