
import json
import hashlib
from time import time

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def new_block(self, proof, previous_hash = None):
        """
        블록체인에 새로운 블록을 생성
        :param proof: <int> 작업증명(POW) 알로리즘으로 증명된 증거
        :param previous_hash: (Optional) <str> 이전 블록의 해쉬
        :return: <dict> 새 블록
        """

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        
        reutrn 

    def new_transaction(self, sender, re록ipient, amount):
        """
        Creates a new transaction to go into the next mined Block
        :param sender: <str> Address of the Sender
        :param recipient: <str> Address of the Recipient
        :param amount: <int> Amount
        :return: <int> 이 생성된 트랜잭션을 소유하고 있는 블록의 Index를 리턴
        """
        self.current_transactions.append( {
            'sender': sender,
            "recipient": recipient,
            'amount': amount
        })
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        """
        SHA-256 hash of a block 
        :param block: <dict> Block
        :return: <str>
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]
