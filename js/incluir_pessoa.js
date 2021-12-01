$(function(){

    // Função executada ao clicar
    $ (document).on("click", "#btIncluirPessoa", function() {
        var heranca = 0

        // Pegando os valores dos campos 
        nome = $("#campoNome").val();
        senha = $("#campoSenha").val();
        con_senha = $("#campoCon_Senha").val();
        email = $("#campoEmail").val();
        cpf = $("#campoCpf").val();
        idade = $("#campoIdade").val();

        profi = $("input[name='user']:checked").val();

        // Validação da role do usuário
        if (profi == "aluno") {
            heranca = 2;
            role = "aluno";
        }
        if (profi == "prof"){
            heranca = 1;
            role = "professor";
        }

        // Verificação da existência de uma role
        if (heranca != 0) {

            // Verificação das senhas
            if (senha != con_senha) {
                alert("ERRO: Erro ao confirmar a senha");
            } else {

                var dados = JSON.stringify({nome: nome, cpf: cpf, email: email, idade: idade, senha: senha, role: role});

                // Comunicação com o backend
                $.ajax({
                    url: 'http://localhost:5000/incluir_pessoa/'+heranca,
                    type: 'POST',
                    dataType: 'json',
                    contentType: 'application/json',
                    data: dados,
                    success: pessoaIncluida, // Função chamada ao receber resultados positivos
                    error: erroAoIncluir  // Função chamada ao receber resultados negativos
                });

                function pessoaIncluida (retorno) {
                    // Limpando campos do frontend
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
        } else {
            alert("Confirme se é aluno ou professor!")
        }
    });
});