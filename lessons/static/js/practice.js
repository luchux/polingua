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

	function update_list_exercises() {
				//Todo:
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
