try:   # se um dia vc tiver algum erro em alguma importação de pacotes, use isso.
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../'    # '../' isso significa a pasta de nível maior que a atual
            )
        )
    )
except ImportError:
    raise
