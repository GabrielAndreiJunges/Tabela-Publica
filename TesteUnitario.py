import unittest
from unittest import TestCase
from TabelaPublica import df


class TestVerificarInput(TestCase):
    def test_retorna_true_quando_ultimo_valor_do_placar_for_maior_que_0_e_menor_que_1000(self):
        placar = df['Placar'].iloc[-1]

        resultado = placar
        self.assertEqual(resultado, 0 <= placar <= 1000)

