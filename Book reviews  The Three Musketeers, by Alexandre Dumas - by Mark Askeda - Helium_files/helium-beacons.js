var hebMD5={};hebMD5.hex_chr="0123456789ABCDEF";hebMD5.rhex=function(e){str="";for(j=0;j<=3;j++){str+=hebMD5.hex_chr.charAt((e>>(j*8+4))&15)+hebMD5.hex_chr.charAt((e>>(j*8))&15)}return str};hebMD5.str2blks_MD5=function(e){nblk=((e.length+8)>>6)+1;blks=new Array(nblk*16);for(i=0;i<nblk*16;i++){blks[i]=0}for(i=0;i<e.length;i++){blks[i>>2]|=e.charCodeAt(i)<<((i%4)*8)}blks[i>>2]|=128<<((i%4)*8);blks[nblk*16-2]=e.length*8;return blks};hebMD5.add=function(e,h){var g=(e&65535)+(h&65535);var f=(e>>16)+(h>>16)+(g>>16);return(f<<16)|(g&65535)};hebMD5.rol=function(e,f){return(e<<f)|(e>>>(32-f))};hebMD5.cmn=function(l,g,f,e,k,h){return hebMD5.add(hebMD5.rol(hebMD5.add(hebMD5.add(g,l),hebMD5.add(e,h)),k),f)};hebMD5.ff=function(g,f,m,l,e,k,h){return hebMD5.cmn((f&m)|((~f)&l),g,f,e,k,h)};hebMD5.gg=function(g,f,m,l,e,k,h){return hebMD5.cmn((f&l)|(m&(~l)),g,f,e,k,h)};hebMD5.hh=function(g,f,m,l,e,k,h){return hebMD5.cmn(f^m^l,g,f,e,k,h)};hebMD5.ii=function(g,f,m,l,e,k,h){return hebMD5.cmn(m^(f|(~l)),g,f,e,k,h)};hebMD5.calcMD5=function(e){x=hebMD5.str2blks_MD5(e);a=1732584193;b=-271733879;c=-1732584194;d=271733878;for(i=0;i<x.length;i+=16){olda=a;oldb=b;oldc=c;oldd=d;a=hebMD5.ff(a,b,c,d,x[i+0],7,-680876936);d=hebMD5.ff(d,a,b,c,x[i+1],12,-389564586);c=hebMD5.ff(c,d,a,b,x[i+2],17,606105819);b=hebMD5.ff(b,c,d,a,x[i+3],22,-1044525330);a=hebMD5.ff(a,b,c,d,x[i+4],7,-176418897);d=hebMD5.ff(d,a,b,c,x[i+5],12,1200080426);c=hebMD5.ff(c,d,a,b,x[i+6],17,-1473231341);b=hebMD5.ff(b,c,d,a,x[i+7],22,-45705983);a=hebMD5.ff(a,b,c,d,x[i+8],7,1770035416);d=hebMD5.ff(d,a,b,c,x[i+9],12,-1958414417);c=hebMD5.ff(c,d,a,b,x[i+10],17,-42063);b=hebMD5.ff(b,c,d,a,x[i+11],22,-1990404162);a=hebMD5.ff(a,b,c,d,x[i+12],7,1804603682);d=hebMD5.ff(d,a,b,c,x[i+13],12,-40341101);c=hebMD5.ff(c,d,a,b,x[i+14],17,-1502002290);b=hebMD5.ff(b,c,d,a,x[i+15],22,1236535329);a=hebMD5.gg(a,b,c,d,x[i+1],5,-165796510);d=hebMD5.gg(d,a,b,c,x[i+6],9,-1069501632);c=hebMD5.gg(c,d,a,b,x[i+11],14,643717713);b=hebMD5.gg(b,c,d,a,x[i+0],20,-373897302);a=hebMD5.gg(a,b,c,d,x[i+5],5,-701558691);d=hebMD5.gg(d,a,b,c,x[i+10],9,38016083);c=hebMD5.gg(c,d,a,b,x[i+15],14,-660478335);b=hebMD5.gg(b,c,d,a,x[i+4],20,-405537848);a=hebMD5.gg(a,b,c,d,x[i+9],5,568446438);d=hebMD5.gg(d,a,b,c,x[i+14],9,-1019803690);c=hebMD5.gg(c,d,a,b,x[i+3],14,-187363961);b=hebMD5.gg(b,c,d,a,x[i+8],20,1163531501);a=hebMD5.gg(a,b,c,d,x[i+13],5,-1444681467);d=hebMD5.gg(d,a,b,c,x[i+2],9,-51403784);c=hebMD5.gg(c,d,a,b,x[i+7],14,1735328473);b=hebMD5.gg(b,c,d,a,x[i+12],20,-1926607734);a=hebMD5.hh(a,b,c,d,x[i+5],4,-378558);d=hebMD5.hh(d,a,b,c,x[i+8],11,-2022574463);c=hebMD5.hh(c,d,a,b,x[i+11],16,1839030562);b=hebMD5.hh(b,c,d,a,x[i+14],23,-35309556);a=hebMD5.hh(a,b,c,d,x[i+1],4,-1530992060);d=hebMD5.hh(d,a,b,c,x[i+4],11,1272893353);c=hebMD5.hh(c,d,a,b,x[i+7],16,-155497632);b=hebMD5.hh(b,c,d,a,x[i+10],23,-1094730640);a=hebMD5.hh(a,b,c,d,x[i+13],4,681279174);d=hebMD5.hh(d,a,b,c,x[i+0],11,-358537222);c=hebMD5.hh(c,d,a,b,x[i+3],16,-722521979);b=hebMD5.hh(b,c,d,a,x[i+6],23,76029189);a=hebMD5.hh(a,b,c,d,x[i+9],4,-640364487);d=hebMD5.hh(d,a,b,c,x[i+12],11,-421815835);c=hebMD5.hh(c,d,a,b,x[i+15],16,530742520);b=hebMD5.hh(b,c,d,a,x[i+2],23,-995338651);a=hebMD5.ii(a,b,c,d,x[i+0],6,-198630844);d=hebMD5.ii(d,a,b,c,x[i+7],10,1126891415);c=hebMD5.ii(c,d,a,b,x[i+14],15,-1416354905);b=hebMD5.ii(b,c,d,a,x[i+5],21,-57434055);a=hebMD5.ii(a,b,c,d,x[i+12],6,1700485571);d=hebMD5.ii(d,a,b,c,x[i+3],10,-1894986606);c=hebMD5.ii(c,d,a,b,x[i+10],15,-1051523);b=hebMD5.ii(b,c,d,a,x[i+1],21,-2054922799);a=hebMD5.ii(a,b,c,d,x[i+8],6,1873313359);d=hebMD5.ii(d,a,b,c,x[i+15],10,-30611744);c=hebMD5.ii(c,d,a,b,x[i+6],15,-1560198380);b=hebMD5.ii(b,c,d,a,x[i+13],21,1309151649);a=hebMD5.ii(a,b,c,d,x[i+4],6,-145523070);d=hebMD5.ii(d,a,b,c,x[i+11],10,-1120210379);c=hebMD5.ii(c,d,a,b,x[i+2],15,718787259);b=hebMD5.ii(b,c,d,a,x[i+9],21,-343485551);a=hebMD5.add(a,olda);b=hebMD5.add(b,oldb);c=hebMD5.add(c,oldc);d=hebMD5.add(d,oldd)}return hebMD5.rhex(a)+hebMD5.rhex(b)+hebMD5.rhex(c)+hebMD5.rhex(d)};var hebConfiguration={version:"1.1.1",logging:{debug:false},beacons:{beaconID:1,loadTimeoutSeconds:30,loaded:false,baseBeaconURL:"http://beacons.test.local/beaconlet.js",han2LifetimeSeconds:4*60*60,han3LifetimeSeconds:4*60*60,defaultMillisDelayForDelayedBeacon:500,linkBeacons:false,han6Enable:true,han7Enable:true,han8Enable:true,han8LifetimeSeconds:60*60*24*365*2,enableOnLaodTracking:false,enableOnUnloadTracking:false,beaconServerAvailable:true,siteContext:"unknown",pageOwner:null,pageType:null,pageTitle:null,fullSiteContext:"unknown",siteOwnerID:null,siteOwnerName:null,pageContext1:null,pageContext2:null,pageContext1ID:null,pageContext2ID:null,pageID:null}};var hebLogger={loggerDebug:hebConfiguration.logging.debug,getDebugSetting:function(){if(window.location.search.indexOf("hebLoggingDebug=true")>-1){hebLogger.loggerDebug=true}if(window.location.search.indexOf("hebLoggingDebug=false")>-1){hebLogger.loggerDebug=false}return hebLogger.loggerDebug},debug:function(g){try{if(window.console!="undefined"){if(hebLogger.getDebugSetting()==true){console.log(g)}}}catch(f){}}};var hebUtilities={hebNormalizeProtocol:function(e){var f=document.location.protocol;if(f.indexOf("https:")>-1){if(e.indexOf("http:")>-1){e=e.replace(/http:/,"https:")}}else{if(e.indexOf("https:")>-1){e=e.replace(/https:/,"http:")}}return e},addLoadEventHandler:function(e){var f=window.onload;if(typeof window.onload!="function"){window.onload=e}else{window.onload=function(){if(f){f()}e()}}},addUnloadEventHandler:function(e){var f=window.onunload;if(typeof window.onunload!="function"){window.onunload=e}else{window.onunload=function(){if(f){f()}e()}}},cookie:function(f,o,r){if(typeof o!="undefined"){r=r||{};if(o===null){o="";r.expires=null;k="; expires=Thu, 01-Jan-70 00:00:01 GMT";hebLogger.debug("hebUtilities.cookie: Trying to force expiry with explicit date "+k)}var k="";if(r.expires&&(typeof r.expires=="number"||r.expires.toUTCString)){var l;if(typeof r.expires=="number"){l=new Date();l.setTime(l.getTime()+(r.expires*1000))}else{l=r.expires}k="; expires="+l.toUTCString();hebLogger.debug("hebUtilities.cookie : Setting traditional expiry to "+k)}var q=r.path?"; path="+(r.path):"";var m=r.domain?"; domain="+(r.domain):"";var e=r.secure?"; secure":"";document.cookie=[f,"=",encodeURIComponent(o),k,q,m,e].join("")}else{var h=null;if(document.cookie&&document.cookie!=""){var p=document.cookie.split(";");for(var n=0;n<p.length;n++){var g=p[n].replace(/^\s+|\s+$/g,"");if(g.substring(0,f.length+1)==(f+"=")){h=decodeURIComponent(g.substring(f.length+1));break}}}return h}}};var hebBeaconUtilities={getBaseDomain:function(){var e=window.location.hostname;var h=e.split(/\./);var g=h.length;var f=h[g-1];var l=h[g-2];var k=l+"."+f;hebLogger.debug('hebBeaconUtilities.getBaseDomain "'+k+'"');return k==null?"":k},getHeliumUniqueMemberIdentifier:function(){var g=hebUtilities.cookie("remember_me");var f=hebUtilities.cookie("_hupn");if((g!=null)&&(g!="")&&(f!=null)&&(f!="")){var e=f.split("|");var h=e[1];hebLogger.debug("hebBeaconUtilities.getHeliumUniqueMemberIdentifier both Helium login cookies set. Currently using userID "+h);return h}else{hebLogger.debug("hebBeaconUtilities.getHeliumUniqueMemberIdentifier one or other of login cookies not set");return null}},setSiteContext:function(e){hebConfiguration.beacons.siteContext=e},getSiteContext:function(){return hebConfiguration.beacons.siteContext},setFullSiteContext:function(e){hebConfiguration.beacons.fullSiteContext=e},getFullSiteContext:function(){return hebConfiguration.beacons.fullSiteContext},setPageOwner:function(e){hebConfiguration.beacons.pageOwner=e},getPageOwner:function(){return hebConfiguration.beacons.pageOwner},setPageTitle:function(e){hebConfiguration.beacons.pageTitle=e},getPageTitle:function(){return hebConfiguration.beacons.pageTitle},setPageType:function(e){hebConfiguration.beacons.pageType=e},getPageType:function(){return hebConfiguration.beacons.pageType},setSiteOwnerID:function(e){hebConfiguration.beacons.siteOwnerID=e},getSiteOwnerID:function(){return hebConfiguration.beacons.siteOwnerID},setSiteOwnerName:function(e){hebConfiguration.beacons.siteOwnerName=e},getSiteOwnerName:function(){return hebConfiguration.beacons.siteOwnerName},setPageContext1:function(e){hebConfiguration.beacons.pageContext1=e},getPageContext1:function(){return hebConfiguration.beacons.pageContext1},setPageContext2:function(e){hebConfiguration.beacons.pageContext2=e},getPageContext2:function(){return hebConfiguration.beacons.pageContext2},setPageContext1ID:function(e){hebConfiguration.beacons.pageContext1ID=e},getPageContext1ID:function(){return hebConfiguration.beacons.pageContext1ID},setPageContext2ID:function(e){hebConfiguration.beacons.pageContext2ID=e},getPageContext2ID:function(){return hebConfiguration.beacons.pageContext2ID},setPageID:function(e){hebConfiguration.beacons.pageID=e},getPageID:function(){return hebConfiguration.beacons.pageID},getUniqueIdentifier:function(){var e=new Date();e=(e.getTime()+"")+(Math.floor(Math.random()*100000)+"");return e},setSessionData:function(){var n=hebBeaconUtilities.getBaseDomain();var h=false;var k=hebBeaconUtilities.getHeliumUniqueMemberIdentifier();if(k==null){hebUtilities.cookie("_han3",null,{path:"/",domain:n});hebUtilities.cookie("_han4",null,{path:"/",domain:n})}else{if(hebUtilities.cookie("_han3")==null||hebUtilities.cookie("_han3")==""){h=true;var g=hebBeaconUtilities.getUniqueIdentifier();hebUtilities.cookie("_han3",g,{expires:hebConfiguration.beacons.han3LifetimeSeconds,path:"/",domain:n});hebUtilities.cookie("_han4",k,{expires:hebConfiguration.beacons.han3LifetimeSeconds,path:"/",domain:n})}}var o=hebUtilities.cookie("_han2");if(o==null||o==""){var l=hebConfiguration.beacons.han2LifetimeSeconds;if(h){l=hebConfiguration.beacons.han3LifetimeSeconds>l?hebConfiguration.beacons.han3LifetimeSeconds:l}var m=hebBeaconUtilities.getUniqueIdentifier();hebUtilities.cookie("_han2",m,{expires:l,path:"/",domain:n})}else{if(h){var m=o;var l=hebConfiguration.beacons.han2LifetimeSeconds;l=hebConfiguration.beacons.han3LifetimeSeconds>l?hebConfiguration.beacons.han3LifetimeSeconds:l;hebUtilities.cookie("_han2",m,{expires:l,path:"/",domain:n})}}if(hebConfiguration.beacons.han8Enable){var f=hebUtilities.cookie("_han8");if(f==null||f==""){var e=hebBeaconUtilities.getUniqueIdentifier();hebUtilities.cookie("_han8",e,{expires:hebConfiguration.beacons.han8LifetimeSeconds,path:"/",domain:n})}}},normalizeProtocol:function(e){var f=document.location.protocol;if(f.indexOf("https:")>-1){if(e.indexOf("http:")>-1){e=e.replace(/http:/,"https:")}}else{if(e.indexOf("https:")>-1){e=e.replace(/https:/,"http:")}}return e},writeBeaconTag:function(g){hebLogger.debug("hebBeaconUtilities.writeBeaconTag");if(typeof g=="undefined"){g={}}var h=hebBeaconUtilities.getUniqueIdentifier();hebConfiguration.beacons.tagId="heb"+h;g._han0=h;g._han1=hebConfiguration.beacons.beaconID;g._han5=hebBeaconUtilities.getSiteContext();var f=(document.referrer=="undefined"||document.referrer==null)?"noreferer":document.referrer;g._han10=f;if(hebConfiguration.beacons.han6Enable){g._han6=hebMD5.calcMD5(document.location.href)}if(hebConfiguration.beacons.han7Enable){g._han7=hebMD5.calcMD5(f)}g._han11=hebConfiguration.beacons.fullSiteContext?hebConfiguration.beacons.fullSiteContext:"";g._han12=hebConfiguration.beacons.pageOwner?hebConfiguration.beacons.pageOwner:"";g._han13=hebConfiguration.beacons.pageType?hebConfiguration.beacons.pageType:"";g._han14=hebConfiguration.beacons.siteOwnerID?hebConfiguration.beacons.siteOwnerID:"";g._han15=hebConfiguration.beacons.siteOwnerName?hebConfiguration.beacons.siteOwnerName:"";g._han16=hebConfiguration.beacons.pageTitle?hebConfiguration.beacons.pageTitle:"";g._han17=hebConfiguration.beacons.pageContext1?hebConfiguration.beacons.pageContext1:"";g._han18=hebConfiguration.beacons.pageContext2?hebConfiguration.beacons.pageContext2:"";g._han19=hebConfiguration.beacons.pageContext1ID?hebConfiguration.beacons.pageContext1ID:"";g._han20=hebConfiguration.beacons.pageContext2ID?hebConfiguration.beacons.pageContext2ID:"";g._han21=hebConfiguration.beacons.pageID?hebConfiguration.beacons.pageID:"";var l=hebUtilities.hebNormalizeProtocol(hebConfiguration.beacons.baseBeaconURL);var e="?";for(option in g){l+=e+option+"="+encodeURIComponent(g[option]);if(e=="?"){e="&"}}setTimeout(function(){hebLogger.debug("hebBeaconUtilities.writeBeaconTag timeout check");if(hebConfiguration.beacons.loaded==false){var n=document.getElementById(hebConfiguration.beacons.tagId);if(n!=null){var m=n.parentNode;m.removeChild(n);hebConfiguration.beacons.beaconServerAvailable=false;hebLogger.debug("hebBeaconUtilities.writeBeaconTag.timeoutCheck beacon not yet loaded. So remove it.")}}else{hebLogger.debug("hebBeaconUtilities.writeBeaconTag.timeoutCheck beacon loaded. All is well.")}},hebConfiguration.beacons.loadTimeoutSeconds*1000);var k=document.createElement("script");k.setAttribute("src",hebBeaconUtilities.normalizeProtocol(l));k.setAttribute("type","text/javascript");k.setAttribute("id",hebConfiguration.beacons.tagId);document.body.appendChild(k);hebConfiguration.beacons.loaded=true;hebLogger.debug("hebBeaconUtilities.writeBeaconTag: just wrote beacon tag")},beaconLoadHandler:function(){hebBeaconUtilities.fireBeacon();if(hebConfiguration.beacons.enableOnLoadTracking){hebBeaconUtilities.fireOnLoadBeacon()}hebBeaconUtilities.beaconifyLinks()},beaconUnloadHandler:function(){hebBeaconUtilities.fileOnUnloadBeacon()},fireBeacon:function(e){if(hebConfiguration.beacons.beaconServerAvailable){hebLogger.debug("hebBeaconUtilities.fireBeacon: setting up beacon");hebBeaconUtilities.setSessionData();hebBeaconUtilities.writeBeaconTag(e);hebLogger.debug("hebBeaconUtilities.fireBeacon: just fired beacon")}else{hebLogger.debug("hebBeaconUtilities.fireBeacon: beacon server not available. Beacon not fired")}},fireCustomBeaconTypeOnly:function(f){var e={_han9:f};hebBeaconUtilities.fireBeacon(e)},fireCustomBeaconTypeSingleValue:function(g,f){var e={_han9:g,_han10:f};hebBeaconUtilities.fireBeacon(e)},fireDelayedCustomBeaconTypeOnly:function(f,e){if(typeof e=="undefined"){e=hebConfiguration.beacons.defaultMillisDelayForDelayedBeacon}setTimeout(function(){var g={_han9:f};hebBeaconUtilities.fireBeacon(g)},e)},fireDelayedCustomBeaconTypeSingleValue:function(g,f,e){if(typeof e=="undefined"){e=hebConfiguration.beacons.defaultMillisDelayForDelayedBeacon}setTimeout(function(){var h={_han9:g,_han10:customValue};hebBeaconUtilities.fireBeacon(h)},e)},fireOnLoadBeacon:function(){hebBeaconUtilities.fireCustomBeaconTypeSingleValue("pageLoad",document.location.href)},fireOnUnloadBeacon:function(){hebBeaconUtilities.fireCustomBeaconTypeSingleValue("pageUnload",document.location.href)},setBeaconLoadHandler:function(){hebUtilities.addLoadEventHandler(hebBeaconUtilities.beaconLoadHandler);if(hebConfiguration.beacons.enableOnUnloadTracking){hebUtilities.addUnloadEventHandler(hebBeaconUtilities.beaconUnloadHandler)}},beaconifyLink:function(g){var e=document.getElementById(g);if(e!=null){var f=e.onclick;if(typeof f!="function"){e.onclick=function(){hebLogger.debug("hebBeaconUtilities.beaconifyLink.directClickHandler firing beacon on "+this.href);hebBeaconUtilities.fireCustomBeaconTypeSingleValue("linkClick",this.href);return true}}else{e.onclick=function(){hebLogger.debug("hebBeaconUtilities.beaconifyLink.chainedClickHandler invoked on "+this.href);var h=true;if(f){hebLogger.debug("hebBeaconUtilities.beaconifyLink.chainedClickHandler chaining to previous handler");h=f(this)}if(h){hebLogger.debug("hebBeaconUtilities.beaconifyLink.chainedClickHandler about to fire beacon on "+this.href);hebBeaconUtilities.fireCustomBeaconTypeSingleValue("linkClick",this.href)}return true}}}},beaconifyLinks:function(){if(hebConfiguration.beacons.linkBeacons){hebLogger.debug("hebBeaconUtilities.beaconifyLinks enabled. About to processing all the links on the page");for(i=0;i<document.links.length;i++){var e=document.links[i];hebLogger.debug("hebBeaconUtilities.beaconifyLinks enabled. Processing "+e);var f=e.onclick;if(typeof f!="function"){e.onclick=function(){hebLogger.debug("hebBeaconUtilities.beaconifyLinks.directClickHandler firing beacon on "+this.href);hebBeaconUtilities.fireCustomBeaconTypeSingleValue("linkClick",this.href);return true}}else{e.onclick=function(){hebLogger.debug("hebBeaconUtilities.beaconifyLinks.chainedClickHandler invoked on "+this.href);var g=true;if(f){hebLogger.debug("hebBeaconUtilities.beaconifyLinks.chainedClickHandler chaining to previous handler");g=f(this)}if(g){hebLogger.debug("hebBeaconUtilities.beaconifyLinks.chainedClickHandler about to fire beacon on "+this.href);hebBeaconUtilities.fireCustomBeaconTypeSingleValue("linkClick",this.href)}return true}}}}else{hebLogger.debug("hebBeaconUtilities.beaconifyLinks disabled. Nothing doing ...")}}};hebBeaconUtilities.setBeaconLoadHandler();