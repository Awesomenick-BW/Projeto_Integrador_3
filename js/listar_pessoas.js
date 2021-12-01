$ (function() {

    // Comunicação com o backend
    $.ajax({
        url: 'http://localhost:5000/listar_usuarios',
        method: 'GET',
        dataType: 'json',
        success: listar, // Função chamada ao receber resultado positivo
        
        error: function() { // Função chamada ao receber resultado negativo
            alert("Erro ao listar as pessoas")
        }
    })

    function listar (pessoas) { 
        // Laço de repetição para a criação de linhas
        for (var i in pessoas) {
            lin = '<tr>' +
            '<td>' + pessoas[i].id + '</td>' +
            '<td>' + pessoas[i].nome + '</td>' +
            '<td>' + pessoas[i].email + '</td>' +
            '<td>' + pessoas[i].cpf + '</td>' + 
            '<td>' + pessoas[i].idade + '</td>' +
            '<td>' + pessoas[i].role + '</td>' +
            '</tr>';

            // Comunicação com o frontend
            $('#corpoTabelaPessoas').append(lin);
        }
    }
});