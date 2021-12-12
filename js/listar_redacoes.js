$ (function() {
    email = sessionStorage.getItem('email');

    var dados = JSON.stringify({email: email});

    // Comunicação com o backend
    $.ajax({
        url: 'http://localhost:5000/rascunho_aluno',
        method: 'post',
        dataType: 'json',
        contentType: 'application/json',
        dados: dados,
        success: listar, // Função chamada ao receber resultado positivo
        
        error: function() { // Função chamada ao receber resultado negativo
            alert("Erro ao listar as redações");
        }
    });

    function listar (rascunhos) {
        for (var i in rascunhos) {
            lin = '<div class="post">' + 
            '<h1>' + rascunhos[i].titulo + '</h1>' +
            '<p class="content">' + rascunhos[i].comentario + '</p>' +
            '<button onclick="readMore(this)">Read More</button>' +
            '</div>';
            
            $('#rascunhosAluno').append(lin);
        }
    }
});