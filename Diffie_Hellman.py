p= 23
g= 21

alice_k= 51
bob_k= 40

alice_send= pow(g,alice_k,p)
bob_send = pow(g,bob_k,p)

alice_get= pow(bob_send,alice_k,p)

bob_get= pow(alice_send,bob_k, p)

print(alice_get, bob_get)