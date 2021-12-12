$ (function() {

    // Comunicação com o backend
    $.ajax({
        url: 'http://localhost:5000/listar_rascunhos',
        method: 'GET',
        dataType: 'json',
        success: listar, // Função chamada ao receber resultado positivo
    });

    function listar (rascunhos) {
        var email = sessionStorage.getItem('email');

        for (var i in rascunhos) {
            if (rascunhos[i].emailAluno == email){
                lin = '<div class="post">' + 
                '<h1>' + rascunhos[i].titulo + '</h1>' +
                '<p>' + rascunhos[i].comentario + '</p>' +
                '</div>';
                
                $('#rascunhosAluno').append(lin);
            }
        }
    }
});