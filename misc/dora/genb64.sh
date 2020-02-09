#!/bin/bash

cd out

get_quad() {
    cd $1
    for i in *.png; do
        (
            echo -ne $(base64 -w 0 $i)
            echo .$1
        ) >>../../b64
    done
    cd ..
}

get_quad 1
get_quad 2
get_quad 3
get_quad 4
