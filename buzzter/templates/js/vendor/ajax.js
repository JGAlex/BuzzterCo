/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/*
 * author: Joger
 * date: 14/11/2013
 * branch: JGBranch
 *
 */

 $('#buscar').onclick(){
 		$.ajax({
 			type="POST"
 			url: '/Posts/Search/',
 			data:{
 				'textToSeach' : $('#Search').val()
 				'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()

 			},

 			dataType: 'html'
 		}):
 }):

 function seachSuccess (data, textStatus, jqXHR) {
 	// body...
 	$('#Seach-results').html(data):
 }