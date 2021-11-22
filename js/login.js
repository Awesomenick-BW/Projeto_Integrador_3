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
                success: pessoaEncontrada2,
                error: erroAoEncontrar
            });

            function pessoaEncontrada2(retorno){
                if (retorno.resultado == "aluno") {
                    if (sessionStorage.getItem("role") != "aluno") {
                        sessionStorage.setItem("role", "aluno");
                        alert("Logado aluno");
                    }
                }
                else if (retorno.resultado == "professor"){
                    if (sessionStorage.getItem("role") != "professor")
                    sessionStorage.setItem("role", "professor");
                    alert("Logado professor");
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
});