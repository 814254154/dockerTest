#!/bin/bash

function ParseFlag(){
    for i in "$*"
    do
        echo $i
    done

}
ParseFlag()