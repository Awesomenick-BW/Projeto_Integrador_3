$(function(){

    $("#btLogin").click(function(){
        email = $("#loginEmail").val();
        senha = $("#loginSenha").val();

        var dados = JSON.stringify({email: email, senha: senha});

        if ((email == null) || (senha == null)){
            alert("Faltou preencher os campos!");
        } else {

            $.ajax({
                url: 'http://localhost:5000/encontrar_pessoa',
                type: 'POST',
                dataType: 'json',
                contentType: 'application/json',
                data: dados,
                success: pessoaEncontrada,
                error: erroAoEncontrar
            });

            function pessoaEncontrada(retorno){
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

    $("#btLogout").click(function(){
        sessionStorage.removeItem("role");
        sessionStorage.removeItem("id");
        window.location.reload();
    });
});