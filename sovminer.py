#!/usr/bin/env python

import os
import sys
from web3 import Web3, HTTPProvider
from configparser import ConfigParser
import time
import random


vanmisesquotes = [
    "Many who are self-taught far excel the doctors, masters, and bachelors of the most renowned universities.",
    "All rational action is in the first place individual action. Only the individual thinks. Only the individual reasons. Only the individual acts.",
    "Everyone carries a part of society on his shoulders; no one is relieved of his share of responsibility by others.",
    " Whether he chooses or not, every man is drawn into the great historical struggle, the decisive battle into which our epoch has plunged us.",
    "Once the principle is admitted that it is the duty of the government to protect the individual against his own foolishness, no serious objections can be advanced against further encroachments.",
    "If history could teach us anything, it would be that private property is inextricably linked with civilization",
    "He who is unfit to serve his fellow citizens wants to rule them.",
    "The Marxians love of democratic institutions was a stratagem only, a pious fraud for the deception of the masses. Within a socialist community there is no room left for freedom.",
    "The masses do not like those who surpass them in any regard. The average man envies and hates those who are different.",
    "He who only wishes and hopes does not interfere actively with the course of events and with the shaping of his own destiny.",
    "The worship of the state is the worship of force.",
    "There is no more dangerous menace to civilization than a government of incompetent, corrupt, or vile men.",
    "The state can be and has often been in the course of history the main source of mischief and disaster.",
    "It is vain to fight totalitarianism by adopting totalitarian methods.",
    "The first requisite for a better social order is the return to unrestricted freedom of thought and speech.",
    "Nobody ever recommended a dictatorship aiming at ends other than those he himself approved.",
    "He who advocates dictatorship always advocates the unrestricted rule of his own will.",
    "The entrepreneur does not make greater profits in selling bad things than in selling good things.",
    "The champions of socialism call themselves progressives, but they recommend a system which is characterized by rigid observance of routine and by a resistance to every kind of improvement.",
    "Every socialist is a disguised dictator.",
    "The average man is both better informed and less corruptible in the decisions he makes as a consumer than as a voter at political elections.",
    "A society that chooses between capitalism and socialism does not choose between two social systems; it chooses between social cooperation and the disintegration of society.",
    "Every step which leads from capitalism toward planning is necessarily a step nearer to absolutism and dictatorship",
]


SOV_MAINNET = Web3.toChecksumAddress("0x010589b7c33034b802f7dba2c88cc9cec0f46673")


def critical(message):
    print(message)
    sys.exit()


def web3_request_blocking(sender, receiver, value, data, gasprice):
    tx_hash = w3.eth.sendTransaction(
        {"to": receiver, "from": sender, "data": data, "value": value, "gas": 700000, "gasPrice": gasprice}
    )
    print(
        "Txhash: %s"
        % tx_hash.hex()
    )
    w3.eth.waitForTransactionReceipt(tx_hash, timeout=120)

    return tx_hash


def mine(coinbase, gasprice):

    print('"%s"' % random.choice(vanmisesquotes))
    try:
        tx_hash = web3_request_blocking(coinbase, SOV_MAINNET, 0, "0x1249c58b", gasprice)

        print(tx_hash)
    except Exception as e:
        print("Error sending transaction: %s" % str(e))

config_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "config.ini")

try:
    config = ConfigParser()
    config.optionxform = str
    config.read(config_path, "utf-8")

    rpc = config["settings"]["rpc"]
    coinbase = Web3.toChecksumAddress(config["settings"]["coinbase"])
    delay = int(config["settings"]["delay"])
    gasprice = int(config["settings"]["gasprice"])
except KeyError as e:
    critical("Missing or invalid configuration file. See config.ini.example. " + str(e))
except ValueError as e:
    critical("Invalid Ethereum address: " + config["settings"]["sender"])

w3 = Web3(HTTPProvider(rpc))

while (1):
    mine(coinbase, gasprice)
    time.sleep(delay)
