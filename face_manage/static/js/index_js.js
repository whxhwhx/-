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
		})
