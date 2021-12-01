$(function(){

    // Pegando o nome do arquivo
    url = window.location.href;
    url = url.split("src/").pop();

    // Iniciando validação para verificar se a pessoa logada possui a role 
    // necessária para poder usufruir da página
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