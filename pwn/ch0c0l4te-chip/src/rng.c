#include "rng.h"

void set_seed(rand_t *r, uint64_t seed) {
    r->seed = (seed ^ 0x5deece66d) & ((1 << 48) - 1);
}

uint32_t next_int(rand_t *r) {
    r->seed = (r->seed * 0x5deece66d + 0xb) & ((1 << 48) - 1);
    return (uint32_t)(r->seed >> 16);
}
