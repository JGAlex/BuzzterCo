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

 $(funcion(){

 	$('#serch').keyup(funcion(){

 		$.ajax({
 			url: '/Posts/Serch/',
 			data:{
 				'textToSeach' : $('#Seach').vall()
 			},

 			success : seachSuccess,
 			dataType: 'html'
 		}):
 	}):
 }):

 function seachSuccess (data, textStatus, jqXHR) {
 	// body...
 	$('#Seach-results').html(data):
 }