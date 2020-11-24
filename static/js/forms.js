var user;
class User{
    constructor(response){
        this.instance = response['user']
        this.token = response['token']
        console.log(this)
    }
    isOnSelfProfile() {
        var a = window.location.pathname.split('/')
        return a[a.length-1]==this.instance.username ? true : false
    }
}
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$(document).ready(function () {
    $('#signinForm form').on('submit',(e) => {
        e.preventDefault();
        $("#signinForm .modal-body .alert").remove()
        var formData = {
            'csrfmiddlewaretoken' : $("#signinForm input[name='csrfmiddlewaretoken']").val(),
            'username'    : $("#signinForm input[name='username']").val(),
            'password'    : $("#signinForm input[name='password']").val(),
        }
        csrf_token = getCookie('csrf_token')
        $.ajax({
            type: "POST",
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            url: "/login/",
            headers: {
                'X-CSRFToken':getCookie('csrftoken')
            },
            data: JSON.stringify(formData),
            success: function (response) {
                user = new User(response)
                $("#signinForm input[name='password']").val('')
                $("#signinForm input[name='username']").val('')
                title = $('.modal-title').html()
                $('.modal-title').html('Connexion réussie')
                $('.modal-title').css('color', 'green');
                var htmlin = $('#signinForm form').html()
                $('#signinForm form').html(`<i class="far fa-check-circle fa-9x offset-4" style='color:green;'></i>`)
                setTimeout(() => {
                    $('.modal').modal('hide')
                    $('#navbar').load("/ #navbar-content")
                    if (user.isOnSelfProfile()) {
                        $('#main-content').load(window.location.pathname+" #main-content>*")
                        
                    }
                    else{
                        $('#user-card').load(window.location.pathname+" #user-card>*")
                    }
                    $('#signinForm form').html(htmlin)
                }, 1500);
            },
            error: (xhr, status) => {
                if (status<500) {
                    var errors = xhr.responseJSON;
                    alertElement = `<div class='alert alert-danger'>${errors["non_field_errors"]}</div>`;
                    $('#signinForm .modal-body').append(alertElement);
                }
                alertElement = `<div class='alert alert-danger'>Une erreur innatendue s'est produite...</div>`;
                $('#signinForm .modal-body').append(alertElement);
            }
        });

    })

    $('#signupForm form').on('submit', (e)=>{
        e.preventDefault()
        $('.alert').remove()
        alertElement = `<div class='alert alert-info'>Traitement...</div>`;
        $('#signupForm .modal-body').append(alertElement);
        var formData = {
            'csrfmiddlewaretoken' : $("#signinForm input[name='csrfmiddlewaretoken']").val(),
            'first_name': $("#signupForm input[name='username']").val(),
            'last_name': $("#signupForm input[name='last_name']").val(),
            'username': $("#signupForm input[name='username']").val(),
            'email':  $("#signupForm input[name='email']").val(),
            'password': $("#signupForm input[name='password']").val(),
        }

        $.ajax({
            type: "POST",
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            url: "/users/",
            headers: {
                'X-CSRFToken':getCookie('csrftoken')
            },
            data: JSON.stringify(formData),
            success: () =>{
                $('.alert').remove()
                alertElement = `<div class='alert alert-success mt-2'>Demande traitée avec succés<br>Tentez de vous connecter !</div>`;
                $("#signupForm .form-group input").val('')
                $('#signupForm .modal-body').append(alertElement);
                setTimeout(() => {
                    $('.alert').remove()
                }, 1500);
            },
            error: (xhr) =>{
                $('.alert').remove()
                if (status<500) {
                    var errors = xhr.responseJSON;
                    alertElement = `<div class='alert alert-danger'>${errors["non_field_errors"]}</div>`;
                    $('#signupForm .modal-body').append(alertElement);
                }
                alertElement = `<div class='alert alert-danger'>Une erreur innatendue s'est produite...</div>`;
                $('#signupForm .modal-body').append(alertElement);
            }
        });
    })

    $('form#ad-form').on('submit', (e) => {
        e.preventDefault()
        
        $('.alert').remove()
        alertElement = `<div class='alert alert-info'>Traitement...</div>`;
        $('form#ad-form').append(alertElement);
        auhorId = $('b.username').attr('id')
        var formData = new FormData()
        formData.append('csrfmiddlewaretoken' , $("form#ad-form input[name='csrfmiddlewaretoken']").val())
        formData.append('title', $("form#ad-form input[name='title']").val())
        formData.append('description', $("form#ad-form textarea[name='description']").val())
        formData.append('image', $("form#ad-form input[name='image']")[0].files[0])
        formData.append('category',  $("form#ad-form select[name='category']").val())
        formData.append('author', $("form#ad-form select[name='author']").val())
        
        console.log(formData)

        $.ajax({
            type: "POST",
            contentType: false,
            processData: false,
            url: "/annonces/",
            headers: {
                'X-CSRFToken':getCookie('csrftoken'),
                //'Accept': 'text/plain;charset=UTF-8;'
            },
            data: formData,
            success: () =>{
                $('.alert').remove()
                alertElement = `<div class='alert alert-success mt-2'>Annonce publiée avec succés !</div>`;
                $("form#ad-form .form-group input").val('')
                $('form#ad-form').append(alertElement);
                setTimeout(() => {
                    $('.alert').remove()
                }, 1500);
                $('div#ad-list').load(window.location.pathname+' div#my-adverts')
            },
            error: (xhr) =>{
                console.log(xhr.responseJSON)
                $('.alert').remove()
                if (status<500) {
                    var errors = xhr.responseJSON;
                    alertElement = `<div class='alert alert-danger'>${errors["non_field_errors"]}</div>`;
                    $('form#ad-form').append(alertElement);
                }
                else{
                    alertElement = `<div class='alert alert-danger'>Une erreur innatendue s'est produite...</div>`;
                    $('form#ad-form').append(alertElement);
                }
                
            }
        })
    })
});