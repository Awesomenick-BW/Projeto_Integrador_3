$(function(){
    $ (document).on("click", "#btAdicionarRedacao", function() {
        titulo = $("#campoTitulo").val();
        texto = $("#campoTexto").val();

        emailAluno = sessionStorage.getItem("email");

        var dados = JSON.stringify({titulo: titulo, texto: texto, emailAluno: emailAluno})

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
                $("#campoTexto").val("");
            } else {
                alert(retorno.resultado + ":" + retorno.detalhes);
            }
        }

        function erroAoIncluir (retorno) {
            alert("ERRO: " + retorno.resultado + ":" + retorno.detalhes);
        }

    });

});