# A Study in Overflows
This is a repo of scripts that could be useful when learning about and testing for buffer overflows.

README is a mix of notes from study material, books, courses, etc - see below for incomplete list of reference material.

## Scripts:
* overflow_test is from Georgia Weidman's book (ch16) and best used after purchasing via NoStarch and then with her BookUbuntu VM
* overflow_fuzz is to send and incremental number of "A"s to see how many it takes to overwrite EIP
* overflow_skeleton confirms the amount and lets you replace with unique bytes...pattern_create...pattern_offset...bad characters...payload

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
| **EIP** | **Instruction Pointer** | ... |
| **ESP** | **Stack Pointer** | Points to memory address of the next stack operation |
| **EBP** | **Base Pointer ( Frame Pointer )** | ... |
| ESI | Source Index | ... |
| EDI | Destination Index | ... |
| EAX | Accumulator | ... |
| EBX | Base | ... |
| ECX | Counter | ... |
| EDX | Data | ... |

### Stack...
* grows from high to low memory ( 4GB [ 0xffffffff ] is the hightest to 0GB [ 0x00000000 ] at the lowest )
* LIFO
* PUSH & POP ( unwound ) instructions

## Investigate
* Debugger: Immunity, gdb, x64gdb, etc.

### Common Stack-based Buffer Overflow Workflow
1. Fuzz Test & observe crash in debugger
2. Confirm the rough number of bytes to crash
3. Get Control of EIP, then confirm control
4. Check for bad characters
5. Redirect Execution Flow...find a naturally occuring jmp esp
6. Add Shellcode

#### Resources ( incomplete ):
* Coursera: University of Maryland, College Park - Software Security (Course 2 in Cybersecurity Specialization)
* Weidman, G. (2014). Penetration Testing. San Francisco, California. No Starch Press Inc.
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
...
