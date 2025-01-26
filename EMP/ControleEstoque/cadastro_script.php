<!DOCTYPE html>
<html lang="pt-br">
  <head>
    <!-- Meta tags Obrigatórias -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="ControleEstoque/css/bootstrap.min.css">

    <title>Cadastro</title>
  </head>
  <body>
    
    <div class="container">
        <div class="row">
           <?php
           include "conexao.php";

           $nome_produto = $_POST['nome_produto'];
           $descricao = $_POST['descricao'];
           $preco_unitario = $_POST['preco_unitario'];
           $qtd_estoque = $_POST['qtd_estoque'];
           $valor_estoque = $preco_unitario * $qtd_estoque;

           $sql = "INSERT INTO ControleEstoque (nome_produto, descricao, preco_unitario, qtd_estoque, valor_estoque) VALUES ('$nome_produto','$descricao','$preco_unitario','$qtd_estoque', '$valor_estoque')";

          if (mysqli_query($conn,$sql)){
            mensagem("$nome_produto CADASTRADO COM SUCESSO!", 'success');
          }
          else
            mensagem("$nome_produto NÃO CADASTRADO.", 'danger');

          $sql = "SELECT nome_produto, descricao, preco_unitario, qtd_estoque, (preco_unitario * qtd_estoque) AS valor_estoque FROM ControleEstoque";
          
          $result = mysqli_query($conn, $sql);

           ?>
          <br>
          <a href="index.php"><button type="button" class="btn btn-primary">Voltar</button></a>

        </div>
    </div>

    <!-- JavaScript (Opcional) -->
    <!-- jQuery primeiro, depois Popper.js, depois Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
  </body>
</html>