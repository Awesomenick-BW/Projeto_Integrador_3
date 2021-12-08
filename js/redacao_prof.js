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

    function encontrar_aluno(idAluno) {
        $.ajax({
            url: 'http://localhost:5000/encontrar_aluno/'+idAluno,
            type: 'GET',
            dataType: 'json',
            success: alunoEncontrado, // Função chamada ao receber resultados positivos
            error: function() {
                alert("Aluno não encontrado")
            }  // Função chamada ao receber resultados negativos
        });

        function alunoEncontrado (emailAluno) {
            return emailAluno;
        }
    }

    function listar (rascunhos) {
        for (var i in rascunhos) {
            lin = '<div class="post">' + 
            '<h1>' + rascunhos[i].titulo + '</h1>' +
            '<p class="content">' + rascunhos[i].texto + '</p>' +
            '<p class="content">' + encontrar_aluno(rascunhos[i].idAluno) + '</p>' +
            '<button onclick="readMore(this)">Read More</button>' +
            '<a href="#target1"><button>Reply</button></a>' +
            '</div>';
            
            $('#rascunhosAluno').append(lin);
        }
    }
});