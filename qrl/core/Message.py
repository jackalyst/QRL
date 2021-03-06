# coding=utf-8
# Distributed under the MIT software license, see the accompanying
# file LICENSE or http://www.opensource.org/licenses/mit-license.php.

class Message:
    def __init__(self):
        self.msg = None
        self.msg_type = None

    def create(self, msg, msg_type):
        self.msg = msg
        self.msg_type = msg_type
        return self

    def add_peer(self, msg_type):
        self.msg_type = msg_type

        return self