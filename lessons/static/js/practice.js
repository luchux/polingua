
	function update_exercise() {

		function roundImages(){
			
			$('#images img').each(function() {
				var imgClass = $(this).attr('class');
				$(this).wrap('<span class="image-wrap ' + imgClass + '" style="width: auto; height: auto;"/>');
				$(this).removeAttr('class');
			});
			 /*
			    $(this).css("opacity","0");
			  });
			*/
			
		};

		$.get('/polingua/exercise',function(response){

			if (response) {
			
				exercise = response['exercise'];
				native_sent = exercise['trans_en'];
				foreing_sent = exercise['trans_es'];

				$('#exercise h2').text(native_sent)

				$('#help h2').text(foreing_sent);


				images = ""
				$(exercise['urls']).each(function(key,value) {
					images = images + "<img class='rounded-img' src='" + value + "'/>";
				});
				$('#images').html(images);
				roundImages();


			}
			else{
				console.log('Error: no response $.get(polingua/exercise)')
			}
		});
		
	}

	function update_list_exercises() {
				//Todo:
		$('#exercises').load('/polingua/exercises/');
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

    function play_sound(){

        $("#play_sound").click(function(){

  		 	$('body').append("<embed src='" + $('#play_sound').attr('src') + $('#help').text() + "'"+ "autostart='true' hidden='true' loop='false'>");
  		 });
    };

    function show_help(){	
		$("#help_me").click(function(){

			$('#help').show().delay(4000).fadeOut();
		    // Animation complete.
		  });
	};
	

