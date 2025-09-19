import time
import matplotlib.pyplot as plt


TARGETS = ["123", "abc", "XYZ", "456", "pass"]  # las 5 contraseñas
ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_+=[]{};:'\",.<>/?\\|`~"
MAX_LEN = max(len(p) for p in TARGETS)
SHOW_EVERY = 0


def brute_force_multiple(targets, alphabet, max_len, show_every=0):
    start = time.time()
    attempts = 0
    found = 0
    targets_left = targets.copy()

    times_list = []
    attempts_list = []

    while found < len(targets):
        for length in range(1, max_len + 1):
            base = len(alphabet)
            space = base ** length
            chars = [''] * length

            for n in range(space):
                attempts += 1
                x = n
                for i in range(length - 1, -1, -1):
                    x, rem = divmod(x, base)
                    chars[i] = alphabet[rem]
                candidate = ''.join(chars)

                elapsed = time.time() - start
                times_list.append(elapsed)
                attempts_list.append(attempts)

                if show_every and attempts % show_every == 0:
                    rate = attempts / elapsed if elapsed > 0 else 0
                    print(f"{attempts} intentos — prueba: '{candidate}' — {elapsed:.2f}s — {rate:.0f} tries/s")

                if candidate in targets_left:
                    print(f"Contraseña encontrada: {candidate}")
                    print(f"Intentos: {attempts}")
                    print(f"Tiempo: {elapsed:.6f} s")
                    found += 1
                    targets_left.remove(candidate)

                    # Graficos
                    plt.plot(attempts_list, times_list, color='blue')
                    plt.xscale('log')
                    plt.xlabel("Intentos")
                    plt.ylabel("Tiempo (s)")
                    plt.title(f"Tiempo vs Intentos — Contraseñas encontradas: {found}")
                    plt.grid(True)
                    plt.show()

                if found >= len(targets):
                    break
            if found >= len(targets):
                break

    return attempts_list, times_list

if __name__ == "__main__":
    print("Brute-force mejorado para 5 contraseñas.")
    brute_force_multiple(TARGETS, ALPHABET, MAX_LEN, SHOW_EVERY)
