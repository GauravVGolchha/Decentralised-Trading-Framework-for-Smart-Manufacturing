# Decentralised Trading Framework for Smart Manufacturing

This repository contains a decentralized trading framework for smart manufacturing using Ethereum smart contracts. The framework allows for secure and transparent trading transactions between parties.

## Overview

The system uses a smart contract to store trading data securely on the Ethereum blockchain. The data includes trade licenses, Importer Exporter Code (IEC), Registration Cum Membership Certificate (RCMC), Quality Council of India (QCI) certification, Goods and Services Tax (GST) details, invoice number, bank account details, and IFSC code.

## Smart Contract

The smart contract (`contract.sol`) is written in Solidity and deployed on the Ethereum blockchain. It includes functions to set and get the trading data. Only the owner of the contract can call these functions.

## Python Application

The Python application (`app.py`) interacts with the smart contract using the Web3 library. It fetches data from a local API, checks the validity of the data, and sends the data to the smart contract.

## Local Server

The local server (`server.py`) is a Flask application that serves as a mock database for the trading data. It provides endpoints to check the validity of the trade license, IEC, RCMC, QCI, GST, and bank account details.

## Docker

A Dockerfile is provided to containerize the application. The Dockerfile is based on the `node:alpine` image and installs `ganache-cli` globally. Ganache CLI is a fast and customizable blockchain emulator. It allows you to make calls to the blockchain without the overheads of running an actual Ethereum node.

## Setup

1. Clone the repository.
2. Deploy the smart contract on your Ethereum network and note down the contract address.
3. Replace the `contract_abi` and `contract_address` variables in `app.py` with your contract's ABI and address.
4. Run the local server (`server.py`).
5. Run the Python application (`app.py`).
6. To build and run the Docker container, use the following commands:
   ```bash
   docker build -t ganache-cli .
   docker run -p 8545:8545 ganache-cli
   ```

## Usage

1. Enter the trading details when prompted by the Python application.
2. The application will check the validity of the details using the local server.
3. If all details are valid, the application will send the data to the smart contract.
4. The transaction hash will be printed if the data is successfully sent to the smart contract.
