import streamlit as st
import requests

# Function to interact with the Tez_Bytes contract
def mint_tezy_bytes(contract_address, image, description, name, symbol, amount):
    payload = {
        "image": image,
        "description": description,
        "name": name,
        "symbol": symbol,
        "amount": amount,
    }
    response = requests.post(f"{contract_address}/minter_entry", json=payload)
    return response.json()

# Function to interact with the Minter contract
def buy_token(contract_address, token_id, amount):
    payload = {"token_id": token_id, "amount": amount}
    response = requests.post(f"{contract_address}/buy", json=payload)
    return response.json()

# Streamlit app
def main():
    st.title("Tez_Bytes NFT Marketplace")

    # Input contract addresses
    tez_bytes_contract_address = st.text_input("Tez_Bytes Contract Address:")
    minter_contract_address = st.text_input("Minter Contract Address:")

    # Mint Tez_Bytes section
    st.header("Mint Tez_Bytes")
    image = st.text_input("Image URL:")
    description = st.text_input("Description:")
    name = st.text_input("Name:")
    symbol = st.text_input("Symbol:")
    amount = st.number_input("Amount:", min_value=1, step=1, value=1)

    if st.button("Mint Tez_Bytes"):
        mint_result = mint_tezy_bytes(tez_bytes_contract_address, image, description, name, symbol, amount)
        st.success(f"Tez_Bytes minted successfully! Result: {mint_result}")

    # Buy Token section
    st.header("Buy Token")
    token_id = st.number_input("Token ID:", min_value=0, step=1, value=0)
    purchase_amount = st.number_input("Purchase Amount:", min_value=1, step=1, value=1)

    if st.button("Buy Token"):
        buy_result = buy_token(minter_contract_address, token_id, purchase_amount)
        st.success(f"Token purchased successfully! Result: {buy_result}")

if __name__ == "__main__":
    main()
