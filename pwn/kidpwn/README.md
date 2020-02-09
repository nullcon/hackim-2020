KiDPwN

##### Description

TBD

##### Points

200/250

##### Flag

hackim20{kids_say_the_darndest_things_its_time_we_pwn_them}

##### Solution

Use alloca -ve overlapping stack frame to partial overwrite return address to run the main twice, use fmt string to leak elf and libc base. Then in second iteration overwrite malloc hook with one_gadget. And trigger malloc hook using printf.
