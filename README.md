# A Study in Overflows
This is a repo of scripts that could be useful when learning about and testing for buffer overflows.

Repository is a mix of notes on study material, books, and courses - see below for incomplete list of reference material.

## Scripts:
* overflow_test is from Georgia Weidman's book (ch16) and best used after purchasing via NoStarch and then with her BookUbuntu VM
* overflow_fuzz is to send and incremental number of "A"s to see how many it takes to overwrite EIP
* overflow_skeleton confirms the amount and lets you replace with unique bytes...pattern_create...pattern_offset

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

All Programs are stored in memory

### Modern Buffer overflow protections:
* DEP:  Data Execution Prevention
* ASLR:  Address Space Layout Randomization

### Registers are manipulated via Assembly language and is specific to the processor - Intel 32-bit = IA32 processor
IA32 Register Categories:
* General purpose (32-bit):  Mathematical operations
* Segment (16-bit):  
* Control (32-bit):  
* Other (32-bit):  

### General Purpose Registers (Linux x86 (32-bit)/IA32)
*NOTE:  "E" is for "extended" from 16-bit to 32-bit*

| Register | Description |
| -------- | ----------- |
| **EIP** | **Extended Instruction Pointer** |
| **ESP** | **Stack Pointer** |
| **EBP** | **Base Pointer ( Frame Pointer )** |
| ESI | Source Index |
| EDI | Destination Index |
| EAX | Accumulator |
| EBX | Base |
| ECX | Counter |
| EDX | Data |

### Stack...
* grows from high to low memory ( 4GB [ 0xffffffff ] is the hightest to 0GB [ 0x00000000 ] at the lowest )
* LIFO
* PUSH & POP ( unwound ) instructions

#### Resources ( incomplete ):
* Coursera: University of Maryland, College Park - Software Security (Course 2 in Cybersecurity Specialization)
* Weidman, G. (2014). Penetration Testing. San Francisco, California. No Starch Press Inc.
* Bowne, S. (2019). CNIT 127: Exploit Development. samsclass.info
* Anley, C., Heasman, J., Linder, F., Richarte, G. (2007). The Shellcoder's Handbook: Discovering and Exploiting Security Holes. indianapolis, indiana. Wiley Publishing, Inc.
* https://en.wikipedia.org/wiki/Shellcode
* ...
