// $(document).ready(function (){
//
//     $('#registration').click(function (e){
//         alert('Регистрация')
//     })
// });


// $(document).ready(function (){
//
//     $('#id1').click(function (e){
//         x = $('#input1').val()
//         if (x.length <=2) {
//             alert('3 and more symbols required')
//             e.preventDefault()
//         }
//     })
//
//
// });

// $(document).ready(function (){
//
//     $('#id2').click(function (e){
//         x = $('#input2').val()
//         if (x.length <=2) {
//             alert('3 and more symbols required')
//             e.preventDefault()
//         }
//     })
//
//
// });


//
// $(document).ready(function () {
//
//     $('#iduseless').click(function (e) {
//
//         $('#tabl').html('dgtgt<strobt');
//         $('#tabl').show()
//     })
// });
//
// $(document).ready(function (){
//     var login = $("#input1").val();
//     $('#input1').blur(function (){
//
//         $.post(
//             'ajax',
//             {
//                 'a':' '
//             },
//             function (response) {
//                 alert(response.message)
//             }
//         );
//         })
// });

// var $page = $('html, body');
// $('a[href*="#"]').click(function() {
//     $page.animate({
//         scrollTop: $($.attr(this, 'href')).offset().top
//     }, 400);
//     return false;
// });

    const anchors = document.querySelectorAll('a[href*="#"]')

    for (let anchor of anchors) {
        anchor.addEventListener('click', function (e) {
            e.preventDefault()

            const blockID = anchor.getAttribute('href').substr(1)

            document.getElementById(blockID).scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            })
        })
    }
var $page = $('html, body');
$('a[href*="#"]').click(function() {
    $page.animate({
        scrollTop: $($.attr(this, 'href')).offset().top
    }, 400);
    return false;
});

$(document).ready(function(){
   $("#menu").on("click","a", function (event) {
   event.preventDefault();
   var id  = $(this).attr('href'),
         top = $(id).offset().top;
    $('body,html').animate({scrollTop: top}, 1500);
  });
	});


$('a').click(function(){
    $('html, body').animate({
        scrollTop: $( $(this).attr('href') ).offset().top
    }, 500);
    return false;
});

$('a[href*=#]').click(function(event){
    $('html, body').animate({
        scrollTop: $( $.attr(this, 'href') ).offset().top
    }, 500);
    event.preventDefault();
});




