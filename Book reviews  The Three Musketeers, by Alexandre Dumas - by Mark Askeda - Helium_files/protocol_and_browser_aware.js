function heNormalizeProtocol(a){var b=document.location.protocol;if(b.indexOf("https:")>-1){if(a.indexOf("http:")>-1){a=a.replace(/http:/,"https:")}}else{if(a.indexOf("https:")>-1){a=a.replace(/https:/,"http:")}}return a}function heMakeURLAbsolute(c){var b=/^http.*:\/\//i;var g=c.indexOf("http")>-1?true:false;var f=c.replace(b,"");if(f.indexOf("%d")>-1){var d=Math.floor((Math.random()*4)+1)-1;f=f.replace(/%d/,d.toString())}var e=document.location.protocol;var a=null;if(g){a=e+"//"+f}else{a=e+"//"+document.location.host+f}return a}HELIUM_BROWSER=null;function heSetBrowserType(){if(!!(window.attachEvent&&!window.opera)){if(window.XDomainRequest){if(document.documentMode=="5"){HELIUM_BROWSER="ie5"}else{if(document.documentMode=="7"){HELIUM_BROWSER="ie8"}else{HELIUM_BROWSER="ie8"}}}else{if(window.XMLHttpRequest){HELIUM_BROWSER="ie8"}else{HELIUM_BROWSER="ie8"}}}else{if(navigator.userAgent.indexOf("AppleWebKit/")>-1||!!navigator.userAgent.match(/Apple.*Mobile.*Safari/)){HELIUM_BROWSER="safari"}else{HELIUM_BROWSER="standard"}}}heSetBrowserType();function heGenerateAbsoluteBrowserAwareStyleSheetHref(a,c){var b="";if(c!=null){b+=c}b+="/css/"+a;if(HELIUM_BROWSER){b+="-"+HELIUM_BROWSER}b=b+".css";return heMakeURLAbsolute(b)}function heWriteAbsoluteBrowserAwareStyleSheetLink(c,f,a){if(a==null){a=new Object()}if(a.rel==undefined){a.rel="Stylesheet"}if(a.type==undefined){a.type="text/css"}if(a.media==undefined){a.media="screen"}var e=heGenerateAbsoluteBrowserAwareStyleSheetHref(c,f);var d="";for(var b in a){d+=" "+b+'="'+a[b]+'" '}document.write("<link "+d+" href='"+heMakeURLAbsolute(e)+"'></link>")}function heWriteAbsoluteBrowserAwareStyleSheetImport(c,f,a){if(a==null){a=new Object()}if(a.type==undefined){a.type="text/css"}var e=heGenerateAbsoluteBrowserAwareStyleSheetHref(c,f);var d="";for(var b in a){d+=" "+b+'="'+a[b]+'" '}document.write("<style "+d+" > @import url('"+heMakeURLAbsolute(e)+"')</style>")}function heWriteAbsoluteJavaScriptTag(d,f,a){if(a==null){a=new Object()}if(a.type==undefined){a.type="text/javascript"}var c="";if(f!=null){c+=f}c+="/javascripts/"+d;var e="";for(var b in a){e+=" "+b+'="'+a[b]+'" '}document.write("<script "+e+" src='"+heMakeURLAbsolute(c)+"'><\/script>")}function heGenerateAbsoluteJavaScriptSrc(b,c){var a="";if(c!=null){a+=c}a+="/javascripts/"+b;return heMakeURLAbsolute(a)}function heWriteAbsoluteImageTag(c,f,a){if(a==null){a=new Object()}var e="";if(f!=null){e+=f}e+="/images/"+c;var d="";for(var b in a){d+=" "+b+'="'+a[b]+'" '}document.write("<img "+d+" src='"+heMakeURLAbsolute(e)+"'></img>")}function heGenerateAbsoluteImageSrc(a,c){var b="";if(c!=null){b+=c}b+="/images/"+a;return heMakeURLAbsolute(b)};