// JavaScript Document
		$(function(){
			var i, pages1,pages2;
			$(function(){
				$('.box1_1 li a').hover(function(){
					i = $(this).parent().index();
					$('.box1_1 li').eq(i).find('p').css({display:""});
				},function(){
					$('.box1_1 li').eq(i).find('p').css({display:"none"});
				})
			})

			$(function(){
				$('.box2_2 li a').click(function(){
					pages2 = pages1;
					pages1 = $(this).parent().index();
					$('.box2_2 li').eq(pages1).find('a').addClass("active");
				})
				$('.box2_2 li a').blur(function(){
					if(pages2 != pages1)
						{
							$('.box2_2 li').eq(pages2).find('a').removeClass("active");
						}
					if(pages1 != 1)
						{
							$('.box2_2 li').eq(1).find('a').removeClass("active");
						}
				})
			})
			$('.vtemp').each(function(){
			    if($(this).html() > 37.3){
			        $(this).css('color','red');
			    }
			});
		})
