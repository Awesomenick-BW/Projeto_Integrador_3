$(function(){

    // Função executada ao apertar o botão
    $("#btLogin").click(function(){
        email = $("#loginEmail").val();
        senha = $("#loginSenha").val();

        var dados = JSON.stringify({email: email, senha: senha});

        // Verificação de dados
        if ((email == null) || (senha == null)){
            alert("Faltou preencher os campos!");
        } else {

            // Comunicação com o backend
            $.ajax({
                url: 'http://localhost:5000/encontrar_pessoa',
                type: 'POST',
                dataType: 'json',
                contentType: 'application/json',
                data: dados,
                success: pessoaEncontrada, // função chamada ao receber resultado positivo
                error: erroAoEncontrar // função chamada ao receber resultado negativo
            });

            function pessoaEncontrada(retorno){
                // Criação de uma chave para futuras validações
                if (retorno.resultado == "aluno") {
                    sessionStorage.setItem("role", "aluno");
                    sessionStorage.setItem("id", retorno.identificador);
                    alert("Aluno Logado");
                }
                else if (retorno.resultado == "professor"){
                    sessionStorage.setItem("role", "professor");
                    sessionStorage.setItem("id", retorno.identificador);
                    alert("Professor Logado");
                }  
                else if (retorno.resultado == "nada"){
                    alert("Não foi encontrado tal pessoa");
                }
            }

            function erroAoEncontrar(retorno){
                alert("Erro!" + ":" + retorno.resultado);
            }
        }
    });

    // Função executada ao clicar 
    $("#btLogout").click(function(){
        // Remoção de chaves e relocação 
        sessionStorage.removeItem("role");
        sessionStorage.removeItem("id");
        window.location.reload();
    });
});