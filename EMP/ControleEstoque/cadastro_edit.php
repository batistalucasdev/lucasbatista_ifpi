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

    <?php

        $preco_unitario = filter_input(INPUT_POST, 'preco_unitario', FILTER_VALIDATE_FLOAT);

        if ($preco_unitario === false) {
            die("Erro: O valor de preço unitário não é válido.");
        }

        $preco_unitario = number_format($preco_unitario, 2, '.', '');

        include "conexao.php";
        $id = $_GET['id'] ?? '';
        $sql = "SELECT * FROM ControleEstoque WHERE cod_produto = $id";

        $dados = mysqli_query($conn, $sql);
        $linha = mysqli_fetch_assoc($dados);

    ?>

    <div class="container">
        <div class="row">
            <div class="col">
                <h1>Cadastro</h1>
                <form action="edit_script.php" method="post">
                    <div class="form-group">
                        <label for="nome_produto">Nome Produto</label>
                        <input type="text" class="form-control" name="nome_produto" required value="<?php echo $linha['nome_produto']; ?>">
                    </div>
                    <div class="form-group">
                        <label for="descricao">Descrição</label>
                        <input type="text" class="form-control" name="descricao" required value="<?php echo $linha['descricao']; ?>">
                    </div>
                    <div class="form-group">
                        <label for="preco_unitario">Preço Unitário</label>
                        <input type="number" step="0.01" class="form-control" name="preco_unitario" required value="<?php echo number_format($linha['preco_unitario'], 2, '.', ''); ?>">
                    </div>

                    <div class="form-group">
                        <label for="qtd_estoque">Qtd em Estoque</label>
                        <div class="input-group">
                            <div class="input-group-prepend">
                                <button type="button" class="btn btn-danger" onclick="alterarQuantidade(-1)">-</button>
                            </div>
                            <input type="number" class="form-control" name="qtd_estoque" required value="<?php echo $linha['qtd_estoque']; ?>" onchange="calcularValorEstoque()" min="0">
                            <div class="input-group-append">
                                <button type="button" class="btn btn-success" onclick="alterarQuantidade(1)">+</button>
                            </div>
                        </div>
                    </div>

                    <div class="form-group">
                        <label for="valor_estoque">Valor Estoque</label>
                        <input type="number" class="form-control" name="valor_estoque" readonly value="<?php echo $linha['valor_estoque']; ?>">
                    </div>
                    <div class="form-group">
                        <input type="submit" class="btn btn-success" value="Salvar Alterações">
                        <input type="hidden" name="id" value="<?php echo $linha['cod_produto']?>">
                    </div>
                </form>

                <a href="welcome.php" class='btn btn-primary'>Voltar para início</a>

                </div>
            </div>
        </div>

    <script>
        
        function calcularValorEstoque() {
            var precoUnitario = parseFloat(document.getElementsByName('preco_unitario')[0].value);
            var qtdEstoque = parseFloat(document.getElementsByName('qtd_estoque')[0].value);
            if (!isNaN(precoUnitario) && !isNaN(qtdEstoque)) {
                document.getElementById('valor_estoque').value = (precoUnitario * qtdEstoque).toFixed(2);
            }
        }

        function alterarQuantidade(valor) {
            var inputQtd = document.getElementsByName('qtd_estoque')[0];
            var novaQuantidade = parseInt(inputQtd.value) + valor;
            if (novaQuantidade >= 0) { // Impede valores negativos
                inputQtd.value = novaQuantidade;
                calcularValorEstoque();
            }
        } 

        document.getElementsByName('preco_unitario')[0].addEventListener('input', calcularValorEstoque);
        document.getElementsByName('qtd_estoque')[0].addEventListener('input', calcularValorEstoque);
    </script>

    <!-- JavaScript (Opcional) -->
    <!-- jQuery primeiro, depois Popper.js, depois Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
  </body>
</html>