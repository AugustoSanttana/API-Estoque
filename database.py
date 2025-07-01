db = {
    "produtos": [
        {
            "id": 1,
            "nome": "Mouse Gamer",
            "descricao": "Mouse com RGB",
            "categoria": "Periférico",
            "preco_unitario": 150.00,
            "quantidade_estoque": 20,
            "id_fornecedor": 1
        },
        {
            "id": 2,
            "nome": "Monitor 24'",
            "descricao": "Full HD",
            "categoria": "Monitor",
            "preco_unitario": 800.00,
            "quantidade_estoque": 10,
            "id_fornecedor": 2
        }
    ],
    
    "fornecedores": [
        {
            "id": 1,
            "nome": "Tech Importações",
            "cnpj": "12.345.678/0001-99",
            "email": "contato@tech.com",
            "telefone": "(11) 99999-9999"
        },
        {
            "id": 2,
            "nome": "Distribuidora PC",
            "cnpj": "98.765.432/0001-11",
            "email": "vendas@pc.com",
            "telefone": "(21) 98888-8888"
        }
    ],
    
    "estoque": [
        {
            "id": 1,
            "id_produto": 1,
            "tipo": "entrada",
            "quantidade": 5,
            "data": "2025-06-17",
            "observacao": "Reforço de estoque"
        },
        {
            "id": 2,
            "id_produto": 2,
            "tipo": "saida",
            "quantidade": 2,
            "data": "2025-06-17",
            "observacao": "Venda"
        }
    ]
}
