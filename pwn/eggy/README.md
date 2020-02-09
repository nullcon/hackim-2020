#### eggy

##### Description

The binary is spidermonkey with some features disabled. This is the build information.

```
$ hg id 
6d3a96d7f2f4+ FIREFOX_NIGHTLY_72_END
$ hg paths
default = https://hg.mozilla.org/mozilla-central
```

You might need some eggs for this one
##### Points

200/250

##### Flag

hackim20{did_y0u_get_that_egg_finally}

##### Solution
Lets just hope there are no unintended solutions

##### Build
```shell
docker build -t eggy .
```
##### Run:
```shell
docker run -p 8000:8000 eggy
```