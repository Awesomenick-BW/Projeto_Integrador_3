$(function(){

    url = window.location.href;
    url = url.split("src/").pop();

    if (url == 'portal_aluno.html') {
        if (sessionStorage.role != 'aluno') {
            window.location.href = "index.html";
        }
    }
    else if (url == "portal_professor.html") {
        if (sessionStorage.role != 'professor') {
            window.location.href = "index.html";
        }
    }

})