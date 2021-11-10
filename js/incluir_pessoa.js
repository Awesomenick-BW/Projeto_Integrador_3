$(function(){

    $ (document).on("click", "#btIncluirPessoa", function() {
        var heranca = 0

        nome = $("#campoNome").val();
        senha = $("#campoSenha").val();
        con_senha = $("#campoCon_Senha").val();
        email = $("#campoEmail").val();
        cpf = $("#campoCpf").val();
        idade = $("#campoIdade").val();

        profi = $("input[name='user']:checked").val();

        if (profi == "aluno") {
            heranca = 2
        }
        if (profi == "prof"){
            heranca = 1
        }

        if (senha != con_senha) {
            alert("ERRO: Erro ao confirmar a senha");
        } else {

            var dados = JSON.stringify({nome: nome, cpf: cpf, email: email, idade: idade});

            $.ajax({
                url: 'http://localhost:5000/incluir_pessoa/'+heranca,
                type: 'POST',
                dataType: 'json',
                contentType: 'application/json',
                data: dados,
                success: pessoaIncluida,
                error: erroAoIncluir
            });

            function pessoaIncluida (retorno) {
                if (retorno.resultado == "ok") {
                    alert("Pessoa incluída com sucesso!");      
                    $("campoNome").val("");
                    $("campoEmail").val("");
                    $("campoSenha").val("");
                    $("campoCon_Senha").val("");
                    $("campoCpf").val("");
                    $("campoIdade").val("");
                } else {
                    alert(retorno.resultado + ":" + retorno.detalhes)
                }
            }

            function erroAoIncluir (retorno) {
                alert("ERRO: "+retorno.resultado + ":" + retorno.detalhes);
            }
        }
    });
});