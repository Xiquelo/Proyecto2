#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def factorial(rec=0):
	if (m!=0 or m!=1):
		if rec < m:
			result = n * (n-1)
			rec += 1
			n -= 1
			factorial(rec)
		else:
			print result
	else:
		print 1


print "Bienvenido a tu calculadora de Factoriales"
n = input("Ingresa el número a calcular: ")
m = n

factorial()