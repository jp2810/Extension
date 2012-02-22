//alert("in content script");
//$('<div class="layout"><input type="text" value="Jayesh" id="url_send"/><div class="keywords">keywords</div></div>').appendTo('body');

$('<div class="layout"><input type="text" id="url_send"/><div class="mextension"><div class="keyword1"><p id="mext_image">My extension</p></div><div class="keyword2"><p onclick="show();">video</p></div><div class="keyword3"><p>position</p></div><div class="keyword4"><p>person</p></div></div></div>').appendTo('body');

$('.layout').hide();
$('.keyword1').click(function(){
	alert("in onclick function of keyword1");
});

//date-22/2/2012 time:9:00AM => do event handling
