<!DOCTYPE html>
<html lang="pt-br">
  <head>
    <!-- Meta tags Obrigatórias -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="ControleEstoque/css/bootstrap.min.css">

    <title>Pesquisa</title>
  </head>
  <body>

  <?php
        
        $pesquisa = $_POST['busca'] ?? '';
        
        include "conexao.php";

        $sql = "SELECT * FROM ControleEstoque WHERE nome_produto LIKE '%$pesquisa%'";

        $dados = mysqli_query($conn, $sql);

    ?>

    <div class="container">
        <div class="row">
            <div class="col">
                <h1>Pesquisa de Produtos</h1>
                <nav class="navbar navbar-light bg-light">
                    <form class="form-inline" action="pesquisa.php" method="post">
                        <input class="form-control mr-sm-2" type="search" placeholder="Nome" aria-label="Pesquisar" name="busca" autofocus>
                        <button class="btn btn-primary" type="submit">Pesquisar</button>
                    </form>
                </nav>

                <table class="table table-hover">
                    <thead>
                        <tr>
                        <th scope="col">Nome Produto</th>
                        <th scope="col">Descrição</th>
                        <th scope="col">Preço Unitário</th>
                        <th scope="col">Qtd em Estoque</th>
                        <th scope="col">Valor Estoque</th>
                        <th scope="col">Funções</th>
                        </tr>
                    </thead>
                    <tbody>

                    <?php

                        while ($linha = mysqli_fetch_assoc($dados)) {
                            $cod_produto = $linha['cod_produto'];
                            $nome_produto = $linha['nome_produto'];
                            $descricao = $linha['descricao'];
                            $preco_unitario = $linha['preco_unitario'];
                            $qtd_estoque = $linha['qtd_estoque'];
                            $valor_estoque = $linha['valor_estoque'];

                            echo "<tr>
                                    <th scope='row'>$nome_produto</th>
                                    <td>$descricao</td>
                                    <td>$preco_unitario</td>
                                    <td>$qtd_estoque</td>
                                    <td>$valor_estoque</td>
                                    <td> <a href='cadastro_edit.php?id=$cod_produto' class='btn btn-success btn-sm'>Editar</a>
                                        <a href='#' class='btn btn-danger btn-sm' data-toggle='modal' data-target='#confirma' 
                                        onclick=" .'"' ."pegar_dados($cod_produto, '$nome_produto')" .'"' .">Excluir</a>
                                    </td>
                                </tr>";
                        }
                    ?>
                    
                    </tbody>
                    </table>
                
                <a href="index.php"><button type="button" class="btn btn-primary">Voltar para início</button></a>

                </div>
            </div>
        </div>

        <!-- Modal -->
        <div class="modal fade" id="confirma" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">Confirmação de Exclusão</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Fechar">
                <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div class="modal-body">
                <form action="excluir_script.php" method="post">
                        <p>Deseja realmente excluir? <strong id="nome_produto">Nome do produto</strong></p>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-dismiss="modal">Não</button>
                        <input type="hidden" name="nome_produto" id="nome_produto01" value="">
                        <input type="hidden" name="id" id="cod_produto" value="">
                        <input type="submit" class="btn btn-danger" value="Sim">
                </form>
            </div>
            </div>
        </div>
        </div>

        <script type="text/javascript">
            function pegar_dados(id, nome){
                document.getElementById('nome_produto').innerHTML = nome;
                document.getElementById('nome_produto01').value = nome;
                document.getElementById('cod_produto').value = id;
            }
        </script>

    <!-- JavaScript (Opcional) -->
    <!-- jQuery primeiro, depois Popper.js, depois Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
  </body>
</html>