#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

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

def get_data():
    return True
 
class Parser(object):
    def __init__(self, _path):
        with open(_path, 'r') as f:
            self._data = json.load(f)
        self._actions = self._data['actions']
 
    def rule_parser(self, rule):
        for sub_rule in rule['rule']:
            source_data = get_data()
            if calc(source_data, sub_rule['op'], sub_rule[''])
    def rules_parser(self, rules):
        for rule in rules:
             
     
    def action_parser(self):
        for action in self._actions:
            self.rules_parser(action['condition'])
a = Parser("test.json")
a.parser()
