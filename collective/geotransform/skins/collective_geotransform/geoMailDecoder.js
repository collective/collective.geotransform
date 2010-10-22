        jq(document).ready( function() {
        	// Decode the href attribute to extract de mail 
        	jq("a[href^=contact]").each(function(i){
        		jq(this).attr('class', 'link-mailto');
        		encodedMail = jq(this).attr('href').replace(/contact\//,"");
        		decodedMail = jq.base64.decode(encodedMail);
        		jq(this).attr('href', 'mailto:'+decodedMail);
        		jq(this).text(decodedMail);
        	});
        });