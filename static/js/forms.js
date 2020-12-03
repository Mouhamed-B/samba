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
showModalDialog = (title,message, button, btn) => {
    $('#confirmModal .modal-body').html(message)
    $('#confirmModal .modal-footer>button:last-child')
        .html(button)
        .addClass(btn)
    $('#confirmModal .modal-title').html(title)
    $('.modal#confirmModal').modal('show')
}
showModalForm = (id,form,modal) => {
    let data;
    a=$.ajax({
        type: 'get',
        contentType: "application/json; charset=utf-8",
        url: `/annonces/${id}/?format=json`,
        dataType: "json",
        success: function (response) {
            data = response
            console.log('a',data)
        }
    });
    console.log(a)
    /* fetch(`/annonces/${id}/`)
        .then(response =>{
            data=response
            console.log(data)
        })
        .catch(err => {
            form.append(`<a class='alert mt-2 alert-danger'>Une erreur est survenue</a>`)
            console.log('error')
        }) */
    form.find("input[name='title']").val(data.title)
    form.find("textarea[name='description']").val(data.description)
    form.find("select[name='category']").val(data.category)
    form.find("select[name='author']").val(data.auhor)
    modal.modal('show')
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

$(function () {
    //connexion
    $('#signinForm form').on('submit',(e) => {
        e.preventDefault();
        $("#signinForm .alert").remove()
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
                $('#signinForm .modal-title').html('Connexion réussie')
                $('#signinForm .modal-title').css('color', 'green');
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
                else{
                    alertElement = `<div class='alert alert-danger'>Identifiants incorrects</div>`;
                    $('#signinForm .modal-body').append(alertElement);
                }
                
            }
        });

    })
    //inscription
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


    /*Annonces*/
    //post
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
    //delete,put,patch
    $('#ad-card button.dropdown-item').on('click', (e) => {
        e.preventDefault()
        target = e.target
        $('.alert').remove()
        parent=$(target).parent().parent().parent().parent()
        //delete
        if ($(target).attr('data-method')=='delete') {
            showModalDialog('','Voulez-vous vraiment supprimmer cet annonce ?', 'Oui, supprimer','btn-danger')
            $('#confirmModal .modal-footer>button:last-child').on('click',()=>{
                parent.css('opacity',.65)
                var id = parent.attr('data-index')
                $.ajax({
                    type: "delete",
                    url: `/annonces/${id}/`,
                    dataType: "json",
                    success: function () {
                        
                        $('.modal').modal('hide')
                        parent.remove()
                        $('#my-adverts').load(window.location.pathname+' #my-adverts>*')
                    },
                    error: () => {
                        $('.alert').remove()
                        parent.css('opacity',1)
                        alertElement = `<a class='alert mt-2 alert-danger'>Une erreur est survenue</a>`;
                        $('.modal-body#confirmModal').append(alertElement)
                    }
                });
            })  
        }
        //put
        if ($(target).attr('data-method')=='put') {
            id = parent.attr('data-index')
            modal = $('#formModal')
            form = $('#ad-form')
            showModalForm(id,form,modal)
            var data = new FormData()
            formData.append('csrfmiddlewaretoken' , form.find("input[name='csrfmiddlewaretoken']").val())
            formData.append('title', form.find("input[name='title']").val())
            formData.append('description', form.find("textarea[name='description']").val())
            formData.append('image', form.find("input[name='image']")[0].files[0])
            formData.append('category',  form.find("select[name='category']").val())
            formData.append('author', form.find("select[name='author']").val())
            $.ajax({
                type: 'get',
                url:`/annonces/${id}/`,
                contentType: false,
                processData: false,
                data: data,
                headers: {
                    'X-CSRFToken':getCookie('csrftoken'),
                    //'Accept': 'text/plain;charset=UTF-8;'
                },
                success: () => {
                    form.append(`<a class='alert mt-2 alert-success'>Modifications Enregisrées</a>`)
                    setTimeout(() => {
                        modal.load(window.location.pathname+' #formModal>*')
                        $('.modal').modal('hide')
                    }, 1800);
                },
                error: ()=>{
                    form.append(`<a class='alert mt-2 alert-danger'>Une erreur est survenue</a>`)
                }
            })
            
        }      
    })
    
    
    /*Categories*/
    //delete,
    $('div#c-card button').on('click', (e) => {
        $('.alert').remove()
        alertElement = `<a class='alert alert-info'>Traitement...</a>`;
        $('#alert').append(alertElement)
        parent = $(e.target).parent().parent().parent()
        if ($(e.target).attr('data-method')=='delete') {
            parent.css('opacity',.65)
            var id = parent.attr('data-index')
            $.ajax({
                type: "delete",
                url: `/categories/${id}/`,
                dataType: "json",
                success: function (response) {
                    $('.alert').remove()
                    parent.remove()
                    alertElement = `<a class='alert alert-success'>Suppression Effectuée</a>`;
                    $('#alert').append(alertElement)
                    setTimeout(() => {
                        $('.alert').remove()
                    }, 1500);
                },
                error: () => {
                    $('.alert').remove()
                    parent.css('opacity',1)
                    alertElement = `<a class='alert alert-danger'>Une erreur est survenue</a>`;
                    $('#alert').append(alertElement)
                }
            });
        }
    })
    //post
    $('form#c-form').on('submit', function (e) {
        e.preventDefault()        
        $('.alert').remove()
        alertElement = `<div class='alert alert-info mt-2'>Traitement...</div>`;
        $(e.target).append(alertElement);
        var formData = {
            'csrf_token' : $(e.target).find("input[name='csrfmiddlewaretoken']").val(),
            'title' : $(e.target).find("input[name='title']").val(),
        }
        $.ajax({
            type: "POST",
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            url: "/categories/",
            data: JSON.stringify(formData),
            success: function (response) {
                $('.alert').remove()
                alertElement = `<div class='alert alert-success mt-2'>Catégorie ajoutée avec succés !</div>`;
                $(e.target).find("input[name='title']").val('')
                $(e.target).append(alertElement);
                setTimeout(() => {
                    $('.alert').remove()
                    $('.modal').modal('hide')
                    $('#c-cards').load(window.location.pathname+' #c-cards>*')
                }, 1500);
            },
            error: ()=>{
                console.log(xhr.responseJSON)
                $('.alert').remove()
                if (status<500) {
                    var errors = xhr.responseJSON;
                    alertElement = `<div class='alert alert-danger'>${errors["non_field_errors"]}</div>`;
                    $(e.target).append(alertElement);
                }
                else{
                    alertElement = `<div class='alert alert-danger'>Une erreur innatendue s'est produite...</div>`;
                    $(e.target).append(alertElement);
                }
            }
        });
    });

});