# SoundMoneyCoin Miner Python

SoundMoneyCoin CLI miner. Requires an Ethereum node to connect to. It should work with a geth light node. Run geth with rpc enabled:

```
$ geth --syncmode light --rpc
```

It might take a while for geth to fully sync. You also need to [create a wallet and nlock it](https://github.com/ethereum/go-ethereum/wiki/Managing-your-accounts). The address of that wallet needs to be entered into `config.ini`. Don't forget to send a little bit of ETH to the wallet for transaction fees.

## Fair Mining 

You can configure this miner to mine at a rapid pace. Yes, this will get you a lot of SOV - but it will also diminish the value of SOV besides clogging the Ethereum network. We keeping the default of 1 transaction per 5 minutes. Remember, you'll be better off holding 1 SOV that's worth $10,000 than holding 10,000 SOV that are worth $0 because of your actions. 

## Installation

```
$ git clone https://github.com/soundmoneycoin/sovminer-python/
$ cd sovminer-python
$ pip install -r requirements.txt
$ cp config.ini.example config.ini
```

Edit the config file to match your environment.

## Usage

```
$ python sovminer.py 
"The first requisite for a better social order is the return to unrestricted freedom of thought and speech."
Txhash: 0x8e60f11e3ad047e8c082ce35baa26f6f03337630dd7fdeb6901f3d127b907821
```
