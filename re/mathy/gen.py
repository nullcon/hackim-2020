
def genf(a,b,i):
    stub = '''int f%d(){ // %c - %c
        OBF_BEGIN
        int m = ((int)(flag[N(%d)])*(int)(flag[N(%d)]) - N(%d) * (int)(flag[N(%d)]) + N(%d));
        int n = ((int)(flag[N(%d)])*(int)(flag[N(%d)]) - N(%d) * (int)(flag[N(%d)]) + N(%d));
        IF( V(m) != N(0) || V(n) != N(0) )
            // puts("Yo");
            V(fin) |= N(1);
        ELSE
            // printf("%%d:%%d:", m, n);
            // puts("No");
            V(fin) |= N(0);
        ENDIF
        return 0;
        OBF_END
    }'''
    print stub % ( i, chr(a), chr(b), i, i, (a+b), i, (a*b), i+2, i+2, (a+b), i+2, (a*b))

flag = raw_input().strip()

print '''#include <stdio.h>
#include <string.h>
#include "instr.h"
int fin = 0;
char flag[%d] ;//%s;
''' % (len(flag), flag)

for i in xrange(0, len(flag) - 2):
    genf(ord(flag[i]),ord(flag[i+2]),i)

print '''int main(int argc, char **argv)
{
    scanf("%s", flag);
    if(memcmp(flag, "hackim20{", 9)!=0){
        return -1;
    }
'''

for i in xrange(len(flag)-2):
    print "    f%d();" % (i)
print '''   printf("%d",fin);
    return 0;
}'''
