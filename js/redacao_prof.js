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
        for (var i in rascunhos) {
            lin = '<div class="post">' + 
            '<h1>' + rascunhos[i].titulo + '</h1>' +
            '<p class="readP" id="p">' + rascunhos[i].texto + '</p>' +
            '<p class="read"><strong>Criado por: ' + rascunhos[i].emailAluno + '</strong></p>' +
            '<a href="#target1"><button>Reply</button></a>' +
            '</div>';
            
            $('#rascunhosAluno').append(lin);
        }
    }
});