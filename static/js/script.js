/*
Fonctions pour le responsive
*/


/*
Au chargement du document
*/
function submitForm(e) {
    e.preventDefault()
}
$(function () {
    bsCustomFileInput.init()
    $('.navbar-toggler').on('click',function (e) {
        e.preventDefault();
        if ($('#nav-menu').hasClass('collapsed')) {
            document.getElementById("nav-menu").style.width = "0px";
            $('#nav-menu').removeClass('collapsed');
            $('#u-info').collapse('hide')
            $('.modal-backdrop').remove();
        }
        else{
            var vw = document.documentElement.offsetWidth
            marginY = vw*0.05
            document.getElementById("nav-menu").style.width = "80vw";
            $("#nav-menu").addClass('collapsed')
            $('#u-info').collapse('show')
            $('header').append("<div class='modal-backdrop fade show'></div>")
        }
    });
});