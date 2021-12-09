$(function() {
    $ (document).on("click", "#btAdicionarComentario", function() {
        titulo = $("#campoTitulo").val();
        comentario = $("#campoComentario").val();
        emailAluno = $("#campoEmailAluno").val();

        var dados = JSON.stringify({titulo: titulo, comentario: comentario, emailAluno: emailAluno})

        $.ajax({
            url: 'http://localhost:5000/update_rascunho',
            type: 'POST',
            dataType: 'json',
            contentType: 'application/json',
            data: dados,
            success: comentarioIncluido,
            error: erroAoIncluir
        });

        function comentarioIncluido (retorno) {
            if (retorno.resultado == "ok") {
                alert("Comentário incluido com sucesso!");
                $("#campoTitulo").val("");
                $("#campoComentario").val("");
                $("#campoEmailAluno").val("");
            } else {
                alert(retorno.resultado + ":" + retorno.detalhes);
            }
        }

        function erroAoIncluir (retorno) {
            alert("ERRO: " + retorno.resultado + ":" + retorno.detalhes);
        }

    });
});