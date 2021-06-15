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



$(document).ready(function () {

    $('#iduseless').click(function (e) {

        $('#tabl').html('dgtgt<strobt');
        $('#tabl').show()
    })
});

$(document).ready(function (){
    var login = $("#input1").val();
    $('#input1').blur(function (){

        $.post(
            'ajax',
            {
                'a':' '
            },
            function (response) {
                alert(response.message)
            }
        );
        })
});



