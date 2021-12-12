$(function(){
    $ (document).on("click", "#btAdicionarRedacao", function() {
        titulo = $("#campoTitulo").val();
        // texto = $("#campoTexto").val();
        var texto = document.getElementById('campoTexto');
        var text = texto.textContent;
        comentario = "nenhum"

        emailAluno = sessionStorage.getItem("email");

        var dados = JSON.stringify({titulo: titulo, texto: text, comentario: comentario, emailAluno: emailAluno})

        $.ajax({
            url: 'http://localhost:5000/incluir_rascunho',
            type: 'POST',
            dataType: 'json',
            contentType: 'application/json',
            data: dados,
            success: rascunhoIncluido,
            error: erroAoIncluir
        });

        function rascunhoIncluido (retorno) {
            if (retorno.resultado == "ok") {
                alert("Redação incluido com sucesso!");
                $("#campoTitulo").val("");
                document.getElementById('campoTexto').innerHTML = "";
            } else {
                alert(retorno.resultado + ":" + retorno.detalhes);
            }
        }

        function erroAoIncluir (retorno) {
            alert("ERRO: " + retorno.resultado + ":" + retorno.detalhes);
        }

    });

});