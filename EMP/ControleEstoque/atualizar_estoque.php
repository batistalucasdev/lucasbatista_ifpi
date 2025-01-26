<?php
header('Content-Type: application/json');
include 'conexao.php';

// Decodificar JSON enviado pela requisição
$input = json_decode(file_get_contents('php://input'), true);

if (isset($input['id']) && isset($input['novaQtd'])) {
    $id = $input['id'];
    $novaQtd = $input['novaQtd'];

    // Atualizar no banco de dados
    $sql = "UPDATE ControleEstoque SET qtd_estoque = ? WHERE cod_produto = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param('ii', $novaQtd, $id);

    if ($stmt->execute()) {
        echo json_encode(['sucesso' => true]);
    } else {
        echo json_encode(['sucesso' => false, 'erro' => 'Erro ao atualizar banco de dados']);
    }

    $stmt->close();
} else {
    echo json_encode(['sucesso' => false, 'erro' => 'Dados inválidos enviados']);
}

$conn->close();
