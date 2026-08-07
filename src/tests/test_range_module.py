"""Tests unitarios para RangeModule — LeetCode 715."""

import pytest

from src.range_module import RangeModule


class TestAddRange:
    """Tests para el método addRange."""

    def test_add_to_empty(self) -> None:
        """Agregar intervalo a lista vacía."""
        rm = RangeModule()
        rm.addRange(5, 10)
        assert rm.queryRange(5, 10) is True
        assert rm.queryRange(4, 10) is False
        assert rm.queryRange(5, 11) is False

    def test_add_merges_overlapping(self) -> None:
        """Agregar intervalo que fusiona dos existentes superpuestos."""
        rm = RangeModule()
        rm.addRange(1, 5)
        rm.addRange(3, 8)
        assert rm.queryRange(1, 8) is True
        assert rm.queryRange(0, 1) is False
        assert rm.queryRange(8, 9) is False

    def test_add_merges_adjacent(self) -> None:
        """Agregar intervalo adyacente (sin gaps)."""
        rm = RangeModule()
        rm.addRange(1, 5)
        rm.addRange(5, 10)
        assert rm.queryRange(1, 10) is True

    def test_add_already_covered(self) -> None:
        """Agregar intervalo ya completamente cubierto."""
        rm = RangeModule()
        rm.addRange(1, 10)
        rm.addRange(3, 7)
        assert rm.queryRange(1, 10) is True

    def test_add_multiple_disjoint(self) -> None:
        """Agregar múltiples intervalos disjuntos."""
        rm = RangeModule()
        rm.addRange(1, 3)
        rm.addRange(5, 7)
        rm.addRange(9, 11)
        assert rm.queryRange(1, 3) is True
        assert rm.queryRange(5, 7) is True
        assert rm.queryRange(9, 11) is True
        assert rm.queryRange(3, 5) is False


class TestRemoveRange:
    """Tests para el método removeRange."""

    def test_remove_splits_interval(self) -> None:
        """Eliminar porción de un intervalo (dividir en dos)."""
        rm = RangeModule()
        rm.addRange(1, 10)
        rm.removeRange(4, 7)
        assert rm.queryRange(1, 4) is True
        assert rm.queryRange(7, 10) is True
        assert rm.queryRange(4, 7) is False

    def test_remove_complete(self) -> None:
        """Eliminar intervalo completo."""
        rm = RangeModule()
        rm.addRange(1, 10)
        rm.removeRange(1, 10)
        assert rm.queryRange(1, 10) is False

    def test_remove_union_of_multiple(self) -> None:
        """Eliminar unión de varios intervalos."""
        rm = RangeModule()
        rm.addRange(1, 5)
        rm.addRange(7, 10)
        rm.addRange(12, 15)
        rm.removeRange(3, 13)
        assert rm.queryRange(1, 3) is True
        assert rm.queryRange(13, 15) is True
        assert rm.queryRange(3, 5) is False
        assert rm.queryRange(7, 10) is False
        assert rm.queryRange(12, 13) is False

    def test_remove_nonexistent(self) -> None:
        """Eliminar de intervalo no existente."""
        rm = RangeModule()
        rm.addRange(1, 5)
        rm.removeRange(10, 20)
        assert rm.queryRange(1, 5) is True

    def test_remove_left_edge(self) -> None:
        """Eliminar desde el borde izquierdo."""
        rm = RangeModule()
        rm.addRange(1, 10)
        rm.removeRange(1, 5)
        assert rm.queryRange(1, 5) is False
        assert rm.queryRange(5, 10) is True

    def test_remove_right_edge(self) -> None:
        """Eliminar hasta el borde derecho."""
        rm = RangeModule()
        rm.addRange(1, 10)
        rm.removeRange(7, 10)
        assert rm.queryRange(1, 7) is True
        assert rm.queryRange(7, 10) is False


class TestQueryRange:
    """Tests para el método queryRange."""

    def test_query_covered(self) -> None:
        """Consulta cubierta completamente."""
        rm = RangeModule()
        rm.addRange(1, 10)
        assert rm.queryRange(2, 8) is True

    def test_query_not_covered(self) -> None:
        """Consulta no cubierta."""
        rm = RangeModule()
        rm.addRange(1, 5)
        assert rm.queryRange(6, 10) is False

    def test_query_partially_covered(self) -> None:
        """Consulta parcialmente cubierta."""
        rm = RangeModule()
        rm.addRange(1, 5)
        assert rm.queryRange(3, 8) is False

    def test_query_empty_left_equals_right(self) -> None:
        """Consulta con left == right (debe ser True)."""
        rm = RangeModule()
        assert rm.queryRange(5, 5) is True

    def test_query_empty_state(self) -> None:
        """Consulta en lista vacía (debe ser False)."""
        rm = RangeModule()
        assert rm.queryRange(0, 10) is False


class TestLeetCodeExample:
    """Test del ejemplo completo de LeetCode 715."""

    def test_leetcode_715(self) -> None:
        """Caso de ejemplo del problema."""
        rm = RangeModule()
        rm.addRange(10, 20)
        rm.removeRange(14, 16)
        assert rm.queryRange(10, 14) is True
        assert rm.queryRange(13, 15) is False
        assert rm.queryRange(16, 17) is True


class TestEdgeCases:
    """Tests de casos edge."""

    def test_sequential_add_remove(self) -> None:
        """Múltiples add/remove secuenciales."""
        rm = RangeModule()
        rm.addRange(1, 10)
        rm.removeRange(2, 3)
        rm.removeRange(5, 6)
        rm.removeRange(8, 9)
        assert rm.queryRange(1, 2) is True
        assert rm.queryRange(2, 3) is False
        assert rm.queryRange(3, 5) is True
        assert rm.queryRange(5, 6) is False
        assert rm.queryRange(6, 8) is True
        assert rm.queryRange(8, 9) is False
        assert rm.queryRange(9, 10) is True

    def test_contiguous_intervals(self) -> None:
        """Intervalos contiguos sin superposición."""
        rm = RangeModule()
        rm.addRange(1, 3)
        rm.addRange(3, 5)
        rm.addRange(5, 7)
        assert rm.queryRange(1, 7) is True

    def test_add_remove_re_add(self) -> None:
        """Agregar, eliminar y volver a agregar."""
        rm = RangeModule()
        rm.addRange(1, 10)
        rm.removeRange(5, 8)
        rm.addRange(5, 8)
        assert rm.queryRange(1, 10) is True

    def test_large_values(self) -> None:
        """Valores grandes del dominio."""
        rm = RangeModule()
        rm.addRange(0, 10**9)
        assert rm.queryRange(0, 10**9) is True
        rm.removeRange(10**9 - 1, 10**9)
        assert rm.queryRange(0, 10**9) is False
        assert rm.queryRange(0, 10**9 - 1) is True
