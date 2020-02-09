#### year3000

##### Description

TBD

##### Points

200/250

##### Flag

`hackim20{h3_sa1d_1v3_b3en_t0_th3_ye4R_3O0O}`

##### Solution

Must be solved with static analysis. A generic script will work for all the binaries.

Solution will be something similar to (https://blog.trailofbits.com/2016/06/03/2000-cuts-with-binary-ninja/)[https://blog.trailofbits.com/2016/06/03/2000-cuts-with-binary-ninja/]

##### Deploy
Extract `dist.tar.gz` and serve with `socat tcp-listen:1234,reuseaddr,fork exec:"python -u deploy.py"`

**Only dist.tar.gz should be distributed!!**

##### Note

To serve, run the following:

```sh
$ python gen.py
$ for i in {0..2999}; do strip $i.bin; done
$ mkdir out
$ mv *.bin out/
$ tar -czvf year3000.tar.gz out/
```

This will create **3000 x3** files in your working directory!!

To verify the solutions for sanity, run the following:

```sh
for i in {0..2999} ; do python3 sol_$i.py | ./$i.bin ; done | grep failed
```
