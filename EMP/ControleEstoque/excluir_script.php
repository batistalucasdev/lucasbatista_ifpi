<!DOCTYPE html>
<html lang="pt-br">
  <head>
    <!-- Meta tags Obrigatórias -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="ControleEstoque/css/bootstrap.min.css">

    <title>Exclusão de Produto</title>
  </head>
  <body>
    
    <div class="container">
        <div class="row">
           <?php
           include "conexao.php";

           $id = $_POST['id'];
           $nome_produto = $_POST['nome_produto'];

           $sql = "DELETE from ControleEstoque WHERE cod_produto = $id";

          if (mysqli_query($conn,$sql)){
            mensagem("$nome_produto EXCLUÍDO COM SUCESSO!", 'success');
          }
          else
            mensagem("$nome_produto NÃO EXCLUÍDO.", 'danger');
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