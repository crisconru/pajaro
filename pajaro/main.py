import time
from typing import Any, List

from pynput.keyboard import Key, Controller
import typer


def check_keys(keys: List[str]) -> List[Any]:
    aux_keys = []
    for key in keys:
        aux_keys = key if key.lower() != 'cmd' else Key.cmd
    return aux_keys


def pajaro(
    keys: List[str] = typer.Argument(default=['cmd'], help="List of keys"),
    interval: int = typer.Option(default=5, param_decls="-i", help="time interval in seconds")
) -> None:
    teclado = Controller()
    new_keys = check_keys(keys)
    try:
        while True:
            [teclado.press(i) for i in new_keys]
            time.sleep(interval / 2)
            [teclado.release(i) for i in new_keys]
            time.sleep(interval / 2)
    except (Exception, KeyboardInterrupt) as err:
        print(f'Capachao -> {err}')
    print('Esto es todo hamijos')


if __name__ == '__main__':
    typer.run(pajaro)
