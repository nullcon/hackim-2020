KiDPwN

##### Description

TBD

##### Points

200/250

##### Flag

hackim20{kids_say_the_darndest_things_its_time_we_pwn_them}

##### Solution

Use alloca -ve overlapping stack frame to partial overwrite return address to run the main twice, use fmt string to leak elf and libc base. Then in second iteration overwrite last 2 bytes of read GOT with one gadget to get the shell.
