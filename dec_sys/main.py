#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")
import logging
from cmq.account import Account
from cmq.queue import QueueMeta, Message
from cmq.cmq_exception import CMQExceptionBase


def calc(lnum, op, rnum):
    if op == "<":
        return lnum < rnum
    elif op == "<=":
        return lnum <= rnum
    elif op == ">":
        return lnum > rnum
    elif op == ">=":
        return lnum >= rnum
    elif op == "==":
        return lnum == rnum
    elif op == "!=":
        return lnum != rnum





class Parser(object):
    def __init__(self, _path):
        with open(_path, 'r') as f:
            self._data = json.load(f)
        self._actions = self._data['actions']
        secretId = ''
        secretKey = ''
        # 使用广州地域的消息服务
        endpoint = 'http://cmq-queue-gz.api.qcloud.com'
        # 初始化 my_account, my_queue
        # Account类对象不是线程安全的，如果多线程使用，需要每个线程单独初始化Account类对象
        my_account = Account(endpoint, secretId, secretKey, debug=True)
        my_account.set_log_level(logging.DEBUG)
        queue_name = sys.argv[1] if len(sys.argv) > 1 else "MySampleQueue"
        self.my_queue = my_account.get_queue(queue_name)
        queue_meta = QueueMeta()
        queue_meta.queueName = queue_name
        queue_meta.pollingWaitSeconds = 10
        queue_meta.visibilityTimeout = 10
        queue_meta.maxMsgSize = 1024
        queue_meta.msgRetentionSeconds = 3600

    def get_data(self, dict):
        wait_seconds=3
        recv_msg = self.my_queue.receive_message(wait_seconds)
        print "Receive Message Succeed! ReceiptHandle:%s MessageBody:%s MessageID:%s" % (recv_msg.receiptHandle, recv_msg.msgBody, recv_msg.msgId)
        self.my_queue.delete_message(recv_msg.receiptHandle)
         
        msg_count=3
        messages=[]
        for i in range(msg_count):
            msg_body = "I am test message %s." % i
            msg = Message(msg_body)
            messages.append(msg)
        return True

    def rule_parser(self, rule):
        for sub_rule in rule['rule']:
            source_data = get_data()
            if calc(get_data(sub_rule), sub_rule['op'], sub_rule['data']):
                pass

    def rules_parser(self, rules):
        for rule in rules:
            if self.rule_parser(rule) is False:
                return False
        return True

    def action_parser(self):
        for action in self._actions:
            if self.rules_parser(action['condition']):
                return True
        return False

a = Parser("test.json")

a.parser()
