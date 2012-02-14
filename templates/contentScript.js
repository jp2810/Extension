alert("I'm your content script on every page.");

$('<div id="mextension_popup_video">Click anywhere in the document to auto-close me</div><div class="layout"><div class="mextension"><div class="mextension_images">My extension</div><div class="mextension_video" id="video">video</div><div class="mextension_position">position</div><div class="mextension_person">person</div></div>').appendTo('body');

$('<input type="hidden" id="url_send"/> ').appendTo('body');
$('#mextension_popup_video').hide();

$('#video').click(function(){    //its working
		alert("Handler for .click called");
//$("#mextension_popup_video").show();
		chrome.extension.sendRequest({},function(response){});
	});

$(window).load(function() {
	alert("window load occurred!");
	chrome.tabs.getSelected(null, function(tab) {
		       		current_url=tab.url;
		  		$('#url_send').val(tab.url);
	  		});    	
		$.getJSON('http://127.0.0.1:5000/tokenize',{
			   		url:$('#url_send').val()
		  			}, function(data) {
				     		global_data = data;
				   		var markup = "<ul>";
				   		$.each(global_data.final_results, function(index, value){              
		  	    				markup += "<li class='keyword'>" + value.keyword + "<span class='showLinks'>show links<ul class='linkList'>";
			  				$.each(global_data.final_results[index].search_res,function(i,val){
			  					markup += "<li><a href="+val.Url+"id="+i+"target="+"_blank"+">"+val.Url+"</a></li>";
			  					return(i!=3); 
			    				});
			  				markup += "</ul></span></li>";
		      					return(index!=3);
		      				});
			      			markup += "</ul>";
			      			$(".search_result_id").append(markup);
			      		}
			  	);		
});

			




/*$(document).ready(function() {
      alert("document ready occurred!");
		chrome.extension.sendRequest({}, function(response) {});      
});

$(window).load(function() {
	alert("window load occurred!");
    //$("mextension_video").addEventListener("click",chrome.extension.sendRequest({}, function(response) {}), false);
	chrome.extension.sendRequest({}, function(response) {});			
});*/
//$('<iframe class="notranslate" src="http://127.0.0.1:5000/iframe_div" frameborder="0"  scrolling="no" style="height:100px;"></iframe>').appendTo('body');

