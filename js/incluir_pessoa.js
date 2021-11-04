$(function(){

    $ (document).on("click", "#btIncluirPessoa", function() {
        nome = $("#campoNome").val();
        email = $("#campoEmail").val();
        cpf = $("campoCpf").val();
        idade = $("campoIdade").val();

        var dados = JSON.stringify({nome: nome, email: email, cpf: cpf, idade: idade});

        $.ajax({
            url: 'https://localhost:5000/incluir_pessoa',
            type: 'POST',
            dataType: 'json',
            contentType: 'application/json',
            data: dados,
            success: pessoaInluida,
            error: erroAoIncluir
        });

        function pessoaInluida (retorno) {
            if (retorno.resultado == "ok") {
                alert("Pessoa incluída com sucesso!");      
                $("campoNome").val("");
                $("campoEmail").val("");
                $("campoCpf").val("");
                $("campoIdade").val("");
            } else {
                alert(retorno.resultado + ":" + retorno.detalhes)
            }
        }

        function erroAoIncluir (retorno) {
            alert("ERRO: "+retorno.resultado + ":" + retorno.detalhes);
        }
    });
});