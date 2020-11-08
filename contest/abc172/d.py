#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is a test program."""

N = int(input())

ANS = 1
DIV = [2 for i in range(N + 1)]

for i in range(2, N + 1):
    ANS += i * DIV[i]
    for j in range(i * 2, N + 1, i):
        DIV[j] += 1

print(ANS)
