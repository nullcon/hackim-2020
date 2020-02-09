#include <stdint.h>

typedef struct {
    uint64_t seed;
} rand_t;

void set_seed(rand_t *r, uint64_t seed);
uint32_t next_int(rand_t *r);
