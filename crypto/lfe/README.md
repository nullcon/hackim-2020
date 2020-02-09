SecureLinearFunctionEvaluation

##### Description

In this challenge we provide a ssytem that calculates a * x + c in F_2^128 , where a and b are server supplied and x is client supplied. To get the flag you have to find a and b. Server runs at:

lfe.py

##### Points

200/250

##### Flag

hackim20{this_was_the_most_fun_way_to_include_curveball_that_i_could_find}

##### Solution

This challenge uses a oblivous transfer that is derived from el gamal however, similar to curveball when the client is able to supply the generator it can break the scheme.
