import requests
from web3 import Web3
import json
from hexbytes import HexBytes
# Initialize Web3 with your Ethereum network configuration
web3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

# Replace with the contract ABI and address
contract_abi = [
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"inputs": [],
		"name": "owner",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_tradeLicense",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_clientTradeLicense",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_IEC",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_RCMC",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_GST",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_invoiceNumber",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_Account",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_IFSC",
				"type": "string"
			}
		],
		"name": "setData",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	}
]
contract_address = '0x9EA91149E4bDDCde567C444FaAa1f90e23326CE8'
# 
# Import your contract
contract = web3.eth.contract(abi=contract_abi, address=contract_address)
web3.eth.defaultAccount=web3.eth.accounts[0]
server_url = "http://localhost:49154/tradeLicense"

def checkTradeLicense(_tradeLicense):
    try:
        api_url = server_url+"/" + _tradeLicense
        response = requests.get(api_url)
        return response.text
    except Exception as e:
        return e    

def checkIEC(_tradeLicense,_IEC):
    try:
        api_url = server_url+"/" + _tradeLicense + "/iec/" + _IEC 
        response = requests.get(api_url)
        return response.text
    except Exception as e:
        return e    

def checkRCMC(_tradeLicense,_RCMC):
    try:
        api_url = server_url+"/" + _tradeLicense + "/rcmc/" + _RCMC 
        response = requests.get(api_url)
        return response.text
    except Exception as e:
        return e    

def checkQCI(_tradeLicense,_QCI):
    try:
        api_url = server_url+"/" + _tradeLicense + "/qci/" + _QCI 
        response = requests.get(api_url)
        return response.text
    except Exception as e:
        return e    

def checkGST(_tradeLicense,_GST):
    try:
        api_url = server_url+"/" + _tradeLicense + "/gst/" + _GST 
        response = requests.get(api_url)
        return response.text
    except Exception as e:
        return e

def checkAccount(_tradeLicense,_Account,_IFSC):
    try:
        api_url = server_url+"/" + _tradeLicense + "/account/" + _Account + "/ifsc/" + _IFSC 
        response = requests.get(api_url)
        return response.text
    except Exception as e:
        return e

# Function to fetch data from the local API
def fetch_data_from_local_api():
    try:
        # Replace with the actual URL of your local API
        api_url = 'http://localhost:8080/data'

        response = requests.get(api_url)
        data = response.json()

        # Modify the keys as needed
        iec = data.get('IEC', '')
        rcmc = data.get('RCMC', '')
        gst = data.get('GST', '')

        return {'IEC': iec, 'RCMC': rcmc, 'GST': gst}
    except Exception as e:
        print('Error fetching data from the local API:', str(e))
        return {'IEC': '', 'RCMC': '', 'GST': ''}

# Function to send data to the smart contract
def send_data_to_contract(data):
    try:
        sender_address = '0x8cAFD42737fC62ff7E5361b235F27fBe7571117a'
        sender_private_key = "0x9af177a4d769ac778e208b99efc77b2f2e23f156374d8105b61c3c178fb47b0e"
        transaction = contract.functions.setData(data['tradeLicense'],data['clientTradeLicense'],data['IEC'],data['RCMC'],data['GST'],data['invoiceNumber'],data['Account'],data['IFSC']).transact({"from":sender_address})
        tx_receipt = web3.eth.wait_for_transaction_receipt(transaction)
        return tx_receipt
    except Exception as e:
        print('Error sending data to the smart contract:', str(e))
        return ''

if __name__ == '__main__':
    print("Enter the below details")
    print("1) Trade License : ",end="")
    tradeLicense = input()
    print("2) IEC : ",end="")
    IEC = input()
    print("3) RCMC : ",end="")
    RCMC = input()
    print("4) QCI : ",end="")
    QCI = input()
    print("5) GST : ",end="")
    GST = input()
    print("*) Invoice Number : ",end="")
    invoiceNumber=input()	
    print("6) International bank account number : ",end="")
    Account = input()
    print("7) IFSC : ",end="")
    IFSC = input()
    print("8) Receiver trade License : ",end="")
    clientTradeLicense=input()
    ok = checkTradeLicense(tradeLicense)
    if ok == "True":
        ok = checkIEC(tradeLicense,IEC)
        if ok == "True":
            ok = checkRCMC(tradeLicense,RCMC)
            if ok == "True":
                ok = checkQCI(tradeLicense,QCI)
                if ok == "True":
                    ok = checkGST(tradeLicense,GST)
                    if ok == "True":
                        ok = checkAccount(tradeLicense,Account,IFSC)
                        if ok == "True":
                            ok = checkTradeLicense(clientTradeLicense)
                            if ok == "True":
                                data = {
									"tradeLicense":tradeLicense,
									"IEC":IEC,
									"RCMC":RCMC,
									"GST":GST,
                                    "invoiceNumber":invoiceNumber,
									"Account":Account,
									"IFSC":IFSC,
									"clientTradeLicense":clientTradeLicense
								}
                                transaction_hash = send_data_to_contract(data)
                                if transaction_hash:
                                      print('Data sent to the smart contract. Transaction Hash:', transaction_hash)
                                      print("----------------------------------------------")
                                      print("Accounts available")
                                      print(web3.eth.accounts)
                                else:
                                      print('Failed to send data to the smart contract.')
                            else:
                                print("Invalid Client Trade License")
                        else:
                            print("Invalid Bank Details")
                    else:
                        print("Invalid GST")
                else:
                    print("Invalid QCI")
            else:
                print("Invalid RCMC")
        else:
            print("Invalid IEC")    
    else:
        print("Invalid trade license")    
    
    
    