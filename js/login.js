$(function(){

    $ (document).on("click", "btIncluirPessoa", function(){
        email = $("loginEmail").val();
        senha = $("loginSenha").val();

        var dados = JSON.stringify({email: email, senha: senha})

        if ((email == null) || (senha == null)){
            alert("Faltou preencher os campos!")
        } else {

            $.ajax({
                url: 'http://localhost:5000/encontrar_pessoa',
                type: 'POST',
                datatype: 'json',
                contentType: 'application/json',
                data: dados,
                success: pessoaEncontrada,
                error: erroAoEncontrar
            })

            function pessoaEncontrada(retorno){
                if (retorno == "aluno") {
                    sessionStorage.setItem("role", "aluno")
                }
                if (retorno == "professor"){
                    sessionStorage.setItem("role", "professor")
                }
            }
        }
    })
})