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
                    if (sessionStorage.getItem("role") != "aluno") {
                        sessionStorage.setItem("role", "aluno");
                    }
                    if (sessionStorage.getItem("id") != retorno.identificador) {
                        sessionStorage.setItem("id", retorno.identificador)
                        alert("Aluno Logado")
                    }
                }
                else if (retorno.resultado == "professor"){
                    if (sessionStorage.getItem("role") != "professor") {
                    sessionStorage.setItem("role", "professor");
                    }
                    if (sessionStorage.getItem("id") != retorno.identificador) {
                        sessionStorage.setItem("id", retorno.identificador)
                        alert("Professor Logado")
                    }
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