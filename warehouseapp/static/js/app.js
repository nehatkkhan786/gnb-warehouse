$(document).on('submit', '#form_add', function(e){
	e.preventDefault();
	$.ajax({
		type:'POST',
		url : '/save_book', 
		data : {
			quantity:$('#quantity').val(),
			csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
			action:'post',

		},
		success: function(data){
			console.log(data)
		} 

	});
});














// window.onload = initall()

// var SaveBookBtn;
// function initall(){
// 	SaveBookBtn = document.getElementById('savebook');
// 	SaveBookBtn.onclick = SaveBook;
// }

// function SaveBook(){

// 	var name = document.getElementById('book_name').value;
// 	var price = document.getElementById('book_price').value;
// 	var pages = document.getElementById('book_pages').value;
// 	var url = '/save_book?name='+name+'&price='+price+'&pages='+pages;

// 	var request = new XMLHttpRequest();
// 	request.onreadystatechange = function (){
// 		if(this.readyState == 4 && this.status == 200){
// 			alert(request.responseText)
// 		}
// 	};
// 	request.open('POST', url, true);
// 	request.send();
// }























