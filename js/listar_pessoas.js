$ (function() {

    $.ajax({
        url: 'http://localhost:5000/listar_usuarios',
        method: 'GET',
        dataType: 'json',
        success: listar,
        
        error: function() {
            alert("Erro ao listar as pessoas")
        }
    })

    function listar (pessoas) {
        for (var i in pessoas) {
            lin = '<tr>' +
            '<td>' + pessoas[i].id + '</td>' +
            '<td>' + pessoas[i].nome + '</td>' +
            '<td>' + pessoas[i].email + '</td>' +
            '<td>' + pessoas[i].cpf + '</td>' + 
            '<td>' + pessoas[i].idade + '</td>' +
            '<td>' + pessoas[i].role + '</td>' +
            '</tr>';

            $('#corpoTabelaPessoas').append(lin);
        }
    }
});