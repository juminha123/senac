print("=== Padaria do Bairro ===")
cliente = input("Nome do cliente: ")
produto = input("Nome do produto: ")
 
valor = float(input("valor unitário do produto (R$): "))
quantidade = int(input("Quantidade: "))
 
total = valor * quantidade
print("\n--- Resumo do Pedido ---")
print(f"Cliente: {cliente}")
print(f"Produto: {produto}")
print(f"valor unitário: R$ {valor:.2f}")
print(f"Quantidade: {quantidade}")
print(f"Total a pagar: R$ {total:.2f}")
 
 