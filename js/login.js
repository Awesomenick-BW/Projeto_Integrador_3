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
                datatype: 'json',
                contentType: 'application/json',
                data: dados,
                success: pessoaEncontrada,
                error: erroAoEncontrar
            });

            function pessoaEncontrada(retorno){
                if (retorno.resultado == "aluno") {
                    alert("Logado");
                    sessionStorage.setItem("role", "aluno");
                }
                else if (retorno.resultado == "professor"){
                    alert("Logado");
                    sessionStorage.setItem("role", "professor");
                }
                else if (retorno.resultado == "nada"){
                    alert("Não foi enconctrado tal pessoa");
                }
            }

            function erroAoEncontrar(retorno){
                alert("Erro!" + ":" + retorno.resultado);
            }
        }
    });
});