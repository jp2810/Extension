//alert("in content script");
//$('<div class="layout"><input type="text" value="Jayesh" id="url_send"/><div class="keywords">keywords</div></div>').appendTo('body');

//popup for each keyword click
$('<div class="popup_keyword1">popup of keyword1</div><div class="popup_keyword2">popup of keyword2</div><div class="popup_keyword3">popup of keyword3</div><div class="popup_keyword4">popup of keyword4</div>').appendTo('body');

//layout of bottom extension
$('<div class="layout"><div class="mextension"><button type="button" id="prevkeyword">Prev</button><div class="keyword1"><p id="keyword1">My extension</p></div><div class="keyword2"><p id="keyword2">video</p></div><div class="keyword3"><p id="keyword3">position</p></div><div class="keyword4"><p id="keyword4">person</p></div><div class="keyword5"><p  id="keyword5">keyword5</p></div><button type="button" id="nextkeyword">Next</button></div></div>').appendTo('body');

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
	alert("button click");
	chrome.extension.sendRequest({"button": "prev"});
});
$('#nextkeyword').click(function(){
	alert("button click");
	chrome.extension.sendRequest({"button": "next"});
});


//1)button click 2)call fuction from background.html  sendrequest/onrequest

/*                   //W
$(':button').click(function(){
	alert("button click");
});*/
