from correios import Correios

__author__ = 'Andreas'


encomenda = Correios.encomenda("PE129381952BR")
ultimo = encomenda.ultimo_status_disponivel()
print "%s, %s, %s" % (ultimo.data, ultimo.local, ultimo.situacao)