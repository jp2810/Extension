/*var link = document.createElement('link');
link.href =  chrome.extension.getURL('contentScript.css');
  //chrome-extension://<extension id>/main.css
link.rel = 'stylesheet';
document.documentElement.insertBefore(link);
*/

//variable declaration
var count=-1,total_count=0,response,flag=0,loaded=0;
//popup for each keyword click
$('<div class="popup"><div class="popup_map"></div><div class="popup_keyword1"></div><div class="popup_keyword2">popup of keyword2</div><div class="popup_keyword3">popup of keyword3</div><div class="popup_keyword4">popup of keyword4</div><div class="popup_keyword5">popup of keyword4</div></div>').appendTo('body');

//layout of bottom extension
$('<div class="layout"><img class="close-image" src="http://residentialsearch.savills.co.uk/Content/Images/icon_close.png" /><p class="closetext"style="position:aboslute;top:58px;left:35px;">Close</p><span><img class="gmap" src="http://cdn1.iconfinder.com/data/icons/Mobile-Icons/128/04_maps.png" /><p class="googlemap" style="position:absolute;top:58px;left:35px;">Google Map</p></span><div class="ball1"></div><div class="mextension"><div class="keyword1"><p id="keyword1"></p></div><div class="keyword2"><p id="keyword2"></p></div><div class="keyword3"><p id="keyword3"></p></div><div class="keyword4"><p id="keyword4"></p></div><div class="keyword5"><p id="keyword5"></p><img class="twitter" src="http://cdn1.iconfinder.com/data/icons/colorstroked/Twitter.png" /></div><button type="button" id="rifuprevkeyword" style="position: absolute; left: 863px;top: -8px; background-color: white; width: 43px;height: 26px;">Prev</button><button type="button" id="rifunextkeyword" style="position: absolute;left: 863px;top: 30px;background-color: white;width: 43px;height: 26px;">Next</button></div></div>').appendTo('body');

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
	//alert("button click");
	var s=this.id;
	if(s=="rifuprevkeyword")
	{
		//alert("prev button click");
		//chrome.extension.sendRequest({"button": "prev"});
		display_next_keyword("prev");
	}
	else if(s=="rifunextkeyword")
	{
		//alert("next button click");
		//chrome.extension.sendRequest({"button": "next"});
		display_next_keyword("next");
	}
});
$('.keyword1').click(function(){
	//alert("in onclick function of keyword1");
	//$('.popup_keyword1').toggle();
	if($('.popup_keyword1').is(':visible'))
	{
       	$('.popup_keyword1').slideUp('slow');
    }
    else
    {
		$('.popup_keyword1').slideDown('slow');	
	}
	$('.popup_keyword2').slideUp('slow');
	$('.popup_keyword3').slideUp('slow');
	$('.popup_keyword4').slideUp('slow');
	$('.popup_keyword5').slideUp('slow');	
});
$('.keyword2').click(function(){
	//alert("in onclick function of keyword2");
	//$('.popup_keyword2').toggle();
	if($('.popup_keyword2').is(':visible'))
	{
       	$('.popup_keyword2').slideUp('slow');
    }
    else
    {
		$('.popup_keyword2').slideDown('slow');	
	}
	$('.popup_keyword1').slideUp('slow');
	$('.popup_keyword3').slideUp('slow');
	$('.popup_keyword4').slideUp('slow');
	$('.popup_keyword5').slideUp('slow');	
});
$('.keyword3').click(function(){
	//alert("in onclick function of keyword3");
	//$('.popup_keyword3').toggle();
	if($('.popup_keyword3').is(':visible'))
	{
       	$('.popup_keyword3').slideUp('slow');
    }
    else
    {
		$('.popup_keyword3').slideDown('slow');	
	}
	$('.popup_keyword1').slideUp('slow');
	$('.popup_keyword2').slideUp('slow');
	$('.popup_keyword4').slideUp('slow');
	$('.popup_keyword5').slideUp('slow');	
});
$('.keyword4').click(function(){
	//alert("in onclick function of keyword4");
	//$('.popup_keyword4').toggle();
	if($('.popup_keyword4').is(':visible'))
	{
       	$('.popup_keyword4').slideUp('slow');
    }
    else
    {
		$('.popup_keyword4').slideDown('slow');	
	}
	$('.popup_keyword2').slideUp('slow');
	$('.popup_keyword3').slideUp('slow');
	$('.popup_keyword1').slideUp('slow');
	$('.popup_keyword5').slideUp('slow');	
});

$('.keyword5').click(function(){
	//alert("in onclick function of keyword4");
	//$('.popup_keyword5').toggle();
	if($('.popup_keyword5').is(':visible'))
	{
       	$('.popup_keyword5').slideUp('slow');
    }
    else
    {
		$('.popup_keyword5').slideDown('slow');	
	}
	$('.popup_keyword2').slideUp('slow');
	$('.popup_keyword3').slideUp('slow');
	$('.popup_keyword4').slideUp('slow');
	$('.popup_keyword1').slideUp('slow');	
});
$(".close-image").click(function(){
   	$(this).parent().hide();
	$(".popup_keyword1").hide();
   	$(".popup_keyword2").hide();
   	$(".popup_keyword3").hide();
   	$(".popup_keyword4").hide();
});
/*chrome.extension.onRequest.addListener(request_handler);
function request_handler(request, sender, sendResponse)
{
	alert("jayesh");
	sendResponse({farewell: "goodbye"});
}*/
chrome.extension.onRequest.addListener(request_handler);
function request_handler(request, sender, sendResponse)
{
	if(request.method=="tokenize")
	{
		display_first_four_keyword(request);
	}
	else if(request.method=="get_remaining")
	{
		remaining_keyword(request);
	}
	else if(request.method=="isloaded")
	{
		if(loaded==1)
		{
			sendResponse({farewell: "goodbye"});
		}
		else
		{
			 sendResponse({}); // snub them.
		}
	}
    loaded=1;
	sendResponse({}); // snub them.
}
  function display_first_four_keyword(request) {
	//sender is object which contain id of extension and tab which is null
    response = request.response;
    total_count=response.final_results.length;
	total_count-=1;
	if(total_count>=4)
	{
			show_keyword(0,3);
			count=3;
	}
	else
	{
			show_keyword(0,total_count-1);
			count = total_count-1;
	}
	flag=0;
  }
  function display_next_keyword(button)
		{	
			//keyword are displayed from count to total_count-1
			alert("count=" + count);
			if(button=="next")
			{
				if(flag==1)
				{
					//keyword are exhausted
					alert("no more keyword...");
				}
				else
				{
					//keywords are yet to be displayed
					if(total_count-count<6)
					{
						//less than four keyword are remaines...make flag=1
						if(total_count-count==1)	
						{
							flag=1;
							alert("no more keyword...");
						}
						else
						{
							show_keyword(count+1,total_count-1);
							count = total_count-1;
						}
					}
					else
					{
						//more than four keyword are remain
						show_keyword(count+1,count+4)
						count+=4;
					}
				}
			}
			else if(button=="prev")
			{
				//for prev button
				if(count>3)
				{
					//more than 4 keyword are available
					flag=0;
					count-=count%4+1
					show_keyword(count-3,count);
				}
				else
				{
					//total keyword are less than four
					//show_keyword(0,count);
				}			
			}
			else if(button=="tweets")
			{
				alert("showing tweets");
			}
	 	}
function remaining_keyword(request)
{
	response=request.response;
	total_count=response.final_results.length;
	total_count-=1;
}

function show_keyword(start,end){	
			for(var i=start;i<=end && i<total_count;i++)
			{
				alert(i);
				$('p#keyword'+(i%4+1)).text(response.final_results[i].keyword);		//W
				print_res_of_kwd(i);
				//show_tweets(response.final_results[i].keyword);
				chrome.extension.sendRequest({"keyword": response.final_results[i].keyword});
			}	
			//if less than four keyword are displayed then fill other with blank	
			if(end-start<3)
			{
				for(var i=end-start+1;i<=3;i++)
				{
					$('p#keyword'+(i+1)).empty();
					$('div.popup_keyword'+(i+1)).empty();	
				}
			}
		}	 
function print_res_of_kwd(index)
	 	{
			var markup = "<ul>",clss;
			for(i = 0; i<3 ; i++)
			{	
				str=response.final_results[index].search_res[i].Url;
				str = str.replace(/'/g,"");       //to replace quotes in string with blank string..working properly
				markup += "<li><a href="+str+">"+response.final_results[index].search_res[i].Title+"</a><br />"+response.final_results[index].search_res[i].Description+"</li><hr />";
			}
			markup += "</ul>"
			//alert(markup);            
			clss = "div.popup_keyword"+(index%4+1)
			//chrome.tabs.executeScript(tab_id,{code:"$('"+clss+"').text('');"});		
			$(clss).empty();
			$(clss).append(markup);
			/*			
			if (response.final_results[index].film != "empty")
			{
				var video_url = response.final_results[index].film[0];
				var pos = video_url.search("v=");
				var video_substring = video_url.substring(pos+2,pos+2+11);
		        alert(video_substring);					
		    	var markup_video = '<object height="200" id="grelated-id-yt-player" type="application/x-shockwave-flash" width="200"><param name="movie"           value="http://www.youtube.com/v/'+video_substring+'?enablejsapi=1&amp;version=3&amp;hl=en_US&amp;rel=0"><param name="allowFullScreen" value="true"><param name="allowscriptaccess" value="always"><embed src="http://www.youtube.com/v/'+video_substring+'?enablejsapi=1&amp;version=3&amp;hl=en_US&amp;rel=0" type="application/x-shockwave-flash" allowscriptaccess="always" allowfullscreen="true" height="200" width="200"></object>'
			
				chrome.tabs.executeScript(tab_id,{code:"$('"+clss+"').append('"+markup_video+"');"});		
			}*/
		}
		
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

