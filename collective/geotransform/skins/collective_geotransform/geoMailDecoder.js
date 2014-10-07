        $(document).ready( function() {
        	// Decode the href attribute to extract de mail 
        	$("a[href^=geomailto]").each(function(i){
        		$(this).attr('class', 'link-mailto');
        		encodedMail = $(this).attr('href').replace("geomailto:","");
                decodedMail = $.base64.decode(encodedMail);
        		$(this).attr('href', 'mailto:'+decodedMail);
                if (decodedMail) $(this).text(decodedMail);
        	});
        });