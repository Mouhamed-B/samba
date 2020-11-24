setDropdownPosition = () => {
    document.getElementById('u-info').style.right = ($(window).width() - document.getElementById('connect-btn').offsetLeft - $('#connect-btn').width()*1.3)+'px'
}
unsetDropdownPosition = () => {
    document.getElementById('u-info').style.right = 'initial'
}
/* enableResponsiveMenu = () => {
    unsetDropdownPosition()
    menu = document.getElementById('category-list')
    nav = document.getElementById('nav-menu')
    if (!$('#nav-menu ul#Categories')[0]) {
        nav.innerHTML += menu.innerHTML
        menu.style.display = "none"
    }
}
disableResponsiveMenu = () => {
    $('#nav-menu ul#Categories').remove()
    if ($('#nav-menu').hasClass('collapsed')) {
        $('.navbar-toggler').trigger('click')
    }
    menu = document.getElementById('category-list')
    if (menu) {
        menu.style.display = "initial"
    }
    
    setDropdownPosition()
} */

/* $(() => {
    if ($(window).width()<769) {
        enableResponsiveMenu()
    }
    $(window).on('resize', () => {
        if ($(window).width()<769) {
            enableResponsiveMenu()
        }
        else{
            disableResponsiveMenu()
        }
    })
}) */