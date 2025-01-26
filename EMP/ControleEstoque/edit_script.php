<!DOCTYPE html>
<html lang="pt-br">
  <head>
    <!-- Meta tags Obrigatórias -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="css/bootstrap.min.css">

    <title>Alteração de Cadastro</title>
  </head>
  <body>
    
    <div class="container">
        <div class="row">
           <?php

            $preco_unitario = filter_input(INPUT_POST, 'preco_unitario', FILTER_VALIDATE_FLOAT);

            if ($preco_unitario === false) {
                die("Erro: O valor de preço unitário não é válido.");
            }

            $preco_unitario = number_format($preco_unitario, 2, '.', '');

           include "conexao.php";

           $id = $_POST['id'];
           $nome_produto = $_POST['nome_produto'];
           $descricao = $_POST['descricao'];
           $preco_unitario = $_POST['preco_unitario'];
           $qtd_estoque = $_POST['qtd_estoque'];
           $valor_estoque = $preco_unitario * $qtd_estoque;

           $sql = "UPDATE ControleEstoque SET nome_produto = '$nome_produto', descricao = '$descricao', preco_unitario = '$preco_unitario', qtd_estoque = '$qtd_estoque', valor_estoque = '$valor_estoque' WHERE cod_produto = $id";

          if (mysqli_query($conn,$sql)){
            mensagem("$nome_produto ALTERADO COM SUCESSO!", 'success');
          }
          else
            mensagem("$nome_produto NÃO ALTERADO.", 'danger');
           ?>
          <br>
          <a href="pesquisa.php"><button type="button" class="btn btn-primary">Voltar</button></a>

        </div>
    </div>

    <!-- JavaScript (Opcional) -->
    <!-- jQuery primeiro, depois Popper.js, depois Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
  </body>
</html>