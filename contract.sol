// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DataStorageContract {
    address public owner;
    string private tradeLicense;
    string private IEC;
    string private RCMC;
    string private QCI;
    string private GST;
    string private Account;
    string private IFSC;
    string private invoiceNumber;
    string private clientTradeLicense;
    constructor() {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    function setTradeLicense(string memory _tradeLicense) internal{
        tradeLicense = _tradeLicense;
    }
    
    function setClientTradeLicense(string memory _clientTradeLicense) internal{
        clientTradeLicense = _clientTradeLicense;
    }

    function setIEC(string memory _IEC) internal{
        IEC = _IEC;
    }

    function setRCMC(string memory _RCMC) internal{
        RCMC = _RCMC;
    }

    function setGST(string memory _GST,string memory _invoiceNumber) internal{
        GST = _GST;
        invoiceNumber = _invoiceNumber;
    }

    function setBankDetails(string memory _Account,string memory _IFSC) internal{
        Account = _Account;
        IFSC = _IFSC;
    }

    function setData(string memory _tradeLicense,string memory _clientTradeLicense,string memory _IEC,string memory _RCMC,string memory _GST,string memory _invoiceNumber,string memory _Account,string memory _IFSC) public payable  {
        setTradeLicense(_tradeLicense);
        setClientTradeLicense(_clientTradeLicense);
        setIEC(_IEC);
        setRCMC(_RCMC);
        setGST(_GST, _invoiceNumber);
        setBankDetails(_Account, _IFSC);
    }
}
