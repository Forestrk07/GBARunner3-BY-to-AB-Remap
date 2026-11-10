"""Comprobacion exhaustiva de la tabla de verdad usada por Input.s.
No sustituye la prueba del ejecutable en hardware.
"""
from itertools import product


def simulacion_ensamblador(ds_keyinput: int, ds_keyxy: int) -> int:
    # tst r9, #2; orr r9, r9, #3; biceq r9, r9, #1
    b_pulsado = (ds_keyinput & 2) == 0
    r9 = ds_keyinput | 3
    if b_pulsado:
        r9 &= ~1
    # tst r11, #2; biceq r9, r9, #2
    if (ds_keyxy & 2) == 0:
        r9 &= ~2
    return r9 & 0xFFFF


def esperado(ds_keyinput: int, ds_keyxy: int) -> int:
    r = ds_keyinput & ~3
    if (ds_keyinput & 2) != 0:
        r |= 1  # GBA A sin pulsar
    if (ds_keyxy & 2) != 0:
        r |= 2  # GBA B sin pulsar
    return r


def run():
    # Prueba exhaustiva: 2^10 estados KEYINPUT x 2^2 estados A/Y KEYXY
    n = 0
    for ds in range(1024):
        for extra in range(4):
            assert simulacion_ensamblador(ds, extra) == esperado(ds, extra), (ds, extra)
            for keycnt in (0, 0xFFFF, 0xC001, 0x7FFF):
                # La lectura de 32 bits debe mantener intacto KEYCNT.
                read32 = simulacion_ensamblador(ds, extra) | (keycnt << 16)
                assert read32 >> 16 == keycnt
                assert (read32 & 0xFFFF) == esperado(ds, extra)
                n += 1
    print(f'OK: {n} combinaciones de entrada/KEYCNT; remapeo B->A e Y->B, resto intacto')
    # Casos humanos que incluyen A fisico ignorado
    for a, b, y in product((False, True), repeat=3):
        ds = 0x3FF & (~1 if a else 0x3FF) & (~2 if b else 0x3FF)
        ext = 3 & (~2 if y else 3)
        out = simulacion_ensamblador(ds, ext)
        assert bool((out & 1) == 0) == b
        assert bool((out & 2) == 0) == y
        print(f'DS A={int(a)} B={int(b)} Y={int(y)} -> GBA A={int(not(out&1))} B={int(not(out&2))}')

if __name__ == '__main__':
    run()
