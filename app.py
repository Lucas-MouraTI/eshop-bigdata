import streamlit as st
from pymongo import MongoClient
import pandas as pd
import plotly.express as px

# conexão com MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["eshop"]
colecao = db["produtos"]
clientes = db["clientes"]
pedidos = db["pedidos"]

st.title("📦 Sistema E-Shop Brasil")

menu = st.sidebar.selectbox("Menu", [
    "Dashboard",
    "Cadastrar Produto",
    "Ver Produtos",
    "Cadastrar Cliente",
    "Criar Pedido",
    "Ver Pedidos"
])

# dashboard
if menu == "Dashboard":
    st.subheader("📊 Dashboard")
    
    # total de produtos
    total_produtos = colecao.count_documents({})
    st.metric("📦 Total de Produtos", total_produtos)
    
    # soma de preços
    produtos = list(colecao.find({}, {"preco": 1}))
    soma_precos = sum([p.get("preco", 0) for p in produtos])
    st.metric("💰 Soma de Preços", f"R$ {soma_precos:.2f}")
    
    # produtos por categoria
    st.subheader("📦 Produtos por Categoria")
    
    dados = list(colecao.find({}, {"_id": 0}))
    
    if dados:
        df = pd.DataFrame(dados)
        
        if "categoria" in df.columns:
            grafico = df["categoria"].value_counts().reset_index()
            grafico.columns = ["Categoria", "Quantidade"]
            
            fig = px.bar(grafico, x="Categoria", y="Quantidade")
            st.plotly_chart(fig)

        pedidos_df = pd.DataFrame(list(pedidos.find({}, {"_id": 0})))

        if not pedidos_df.empty:
            st.subheader("📊 Pedidos por Cliente")
            grafico = pedidos_df["cliente"].value_counts().reset_index()
            grafico.columns = ["Cliente", "Pedidos"]

            fig = px.bar(grafico, x="Cliente", y="Pedidos")
            st.plotly_chart(fig)
        
        # produtos mais caros
        st.subheader("🔥 Produtos Mais Caros")
        top = df.sort_values(by="preco", ascending=False).head(5)
        st.dataframe(top)
        
        # produtos mais baratos
        st.subheader("💸 Produtos Mais Baratos")
        baratos = df.sort_values(by="preco").head(5)
        st.dataframe(baratos)
    else:
        st.warning("Nenhum produto cadastrado.")

# cadastrar
if menu == "Cadastrar Produto":
    st.subheader("Cadastrar Produto")

    nome = st.text_input("Nome do Produto")
    preco = st.number_input("Preço", min_value=0.0)
    categoria = st.text_input("Categoria")

    if st.button("Salvar"):
        produto = {
            "nome": nome,
            "preco": preco,
            "categoria": categoria
        }
        colecao.insert_one(produto)
        st.success("Produto cadastrado!")

# visualizar
elif menu == "Ver Produtos":
    st.subheader("Lista de Produtos")

    dados = list(colecao.find())
    
    if dados:
        for item in dados:
            st.write(f"📦 {item['nome']} | R$ {item['preco']} | {item['categoria']}")

            col1, col2 = st.columns(2)

            # deletar
            with col1:
                if st.button(f"Excluir {item['_id']}"):
                    colecao.delete_one({"_id": item["_id"]})
                    st.warning("Produto excluído!")
                    st.rerun()
    else:
        st.warning("Nenhum produto cadastrado.")

elif menu == "Cadastrar Cliente":
    st.subheader("Cadastrar Cliente")

    nome = st.text_input("Nome do Cliente")
    email = st.text_input("Email")

    if st.button("Salvar Cliente"):
        clientes.insert_one({
            "nome": nome,
            "email": email
        })
        st.success("Cliente cadastrado!")

elif menu == "Criar Pedido":
    st.subheader("🛒 Criar Pedido")

    lista_clientes = list(clientes.find())
    lista_produtos = list(colecao.find())

    if lista_clientes and lista_produtos:
        cliente_nome = st.selectbox(
            "Cliente",
            [c["nome"] for c in lista_clientes]
        )

        produto_nome = st.selectbox(
            "Produto",
            [p["nome"] for p in lista_produtos]
        )

        if st.button("Finalizar Pedido"):
            pedidos.insert_one({
                "cliente": cliente_nome,
                "produto": produto_nome
            })
            st.success("Pedido criado!")
    else:
        st.warning("Cadastre clientes e produtos primeiro.")

elif menu == "Ver Pedidos":
    st.subheader("📦 Lista de Pedidos")

    dados = list(pedidos.find({}, {"_id": 0}))

    if dados:
        df = pd.DataFrame(dados)
        st.dataframe(df)
    else:
        st.warning("Nenhum pedido encontrado.")
