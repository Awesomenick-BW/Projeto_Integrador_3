$ (function() {

    // Comunicação com o backend
    $.ajax({
        url: 'http://localhost:5000/listar_rascunhos',
        method: 'GET',
        dataType: 'json',
        success: listar, // Função chamada ao receber resultado positivo
        
        error: function() { // Função chamada ao receber resultado negativo
            alert("Erro ao listar as redações")
        }
    });

    function listar (rascunhos) {
        var email = sessionStorage.getItem('email');

        for (var i in rascunhos) {
            if (rascunhos[i].emailAluno == email){
                lin = '<div class="post">' + 
                '<h1>' + rascunhos[i].titulo + '</h1>' +
                '<p class="content">' + rascunhos[i].texto + '</p>' +
                '<p class="content">Criado por: ' + rascunhos[i].emailAluno + '</p>' +
                '<button onclick="readMore(this)">Read More</button>' +
                '<a href="#target1"><button>Reply</button></a>' +
                '</div>';
                
                $('#rascunhosAluno').append(lin);
            }
        }
    }
});