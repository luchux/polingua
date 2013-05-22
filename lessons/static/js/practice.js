	function update_exercise() {

		function roundImages(){
			$('#images img').each(function() {
				console.log(1)
				var imgClass = $(this).attr('class');
				$(this).wrap('<span class="image-wrap ' + imgClass + '" style="width: auto; height: auto;"/>');
				$(this).removeAttr('class');
			});

		};
		//TODO: ver la api porque aca devuelve adentro del objeto tmbn
		//las stats. deberia traer solo datos del ejercicio.
		$.get('/api/words/exercise/?format=json',function(response){

			if (response) {
				exercises = response['objects'];

				//Ojo, esto es feo.
				update_list_exercises(exercises)

				console.log(exercises)
				exercise = exercises[0]['translation'];
				native_sent = exercise['en'];
				foreing_sent = exercise['es'];

				$('#exercise h2').text(native_sent)

				$('#help h2').text(foreing_sent);


				images = ""
				urls = exercise['img_urls'].split("URLURL")
				$.each(urls, function(key,value) {
					images = images + "<img class='rounded-img' src='" + value + "'/>";
				});
				$('#images').html(images);

				roundImages();

			}
			else{
				console.log('Error: no response $.get(polingua/exercise)')
			}
		});

	};

	function update_list_exercises(exercises) {
		exercises = typeof exercises !== 'undefined' ? exercises : [];
		var table = $("#table_exercises tbody");
		var html = ""
	    $.each(exercises, function(idx, exercise){
			html += "<tr><td>" + exercise['translation']['es'] + "</td><td>" + exercise['translation']['en'] + "</td><td style='width=80%'><div class='ratio-bars'><div class='progress progress-success progress-striped active'><div class='bar bar-corrects'>" + exercise['corrects'] + "</div></div><div class='progress progress-danger progress-striped active'><div class='bar bar-tries'>" + exercise['tries'] + "</div></div></div></td><td class = 'td-score'><div class='progress progress-success progress-striped score-bars'><div class='bar'r>"  + exercise['corrects'] / exercise['tries'] + "</div></div></td><td>" + exercise['last_correct'] + "</td></tr>"

	    });
		table.html(html)
	}

	function adjust_scores(){

			$('.progress').attr('style','margin-bottom:3px');
			$('.td-score').attr('style','vertical-align:center')

			$('.score-bars .bar').each(function(){
				$(this).attr('style','width:' + $(this).text()*100 +'%')
			});

			$('.ratio-bars').each(function(k,elem){
				total = 0
				$(elem).find('.bar-tries').each(function(){
					$(this).attr('style','width:100%');
					total = $(this).text();
				});

				$(elem).find('.bar-corrects').each(function(){
					percentage = ( parseInt($(this).text()) / total ) * 100;
					$(this).attr('style','width:'+percentage+'%');
				});
			});

	};

    function load_help_buttons(){

        $("#play_sound").click(function(){

  		 	$('body').append("<embed src='" + $('#play_sound').attr('src') + $('#help h2').text() + "'"+ "autostart='true' hidden='true' loop='false'>");
  		 });


		$("#help_me").click(function(){

			$('#help').show().delay(4000).fadeOut();
		    // Animation complete.
		  });
	};

//DOCUMENT READY
$(document).ready(function() {

 $('#submit_solution').submit(function(e) { // catch the form's submit event
        // Assign handlers immediately after making the request,
        // and remember the jqxhr object for this request

        var jqxhr = $.post("/trains/validate/",{'solution':$('#solution').val()})
        .done(function(response) {
            $('#submit_solution #solution').attr('value', '');
            if (response['result']){

                msg = "Right! Congratulations ";
                msg = msg + response['user'] + "!";
                $('#exercise-result').text(msg)
                $('#exercise-result').show().delay(2000).fadeOut();
            }
            else{
                msg = "Wrong! Keep training ";
                msg = msg + response['user'] + "!";
                $('#exercise-result').text(msg)
                $('#exercise-result').show().delay(2000).fadeOut();
            }
            console.log('success validate')
            update_exercise();
               update_list_exercises();
               adjust_scores();
               console.log('success update')
        })
        .error(function() { console.log("error"); })
        .complete(function() { console.log("complete"); });
          e.preventDefault();
        // perform other work here ...
       });
});