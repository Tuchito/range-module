"""Interval Manager — Lógica de manipulación de intervalos semiabiertos [left, right)."""

from bisect import bisect_left, bisect_right
from typing import List, Tuple


class IntervalManager:
    """Gestiona una lista de intervalos semiabiertos activos.

    Los intervalos se mantienen ordenados por su extremo izquierdo y sin
    superposiciones. Soporta agregar, eliminar y consultar intervalos.
    """

    def __init__(self) -> None:
        """Inicializa el manager con una lista de intervalos vacía."""
        self._intervals: List[Tuple[int, int]] = []

    def _add_interval(self, left: int, right: int) -> None:
        """Agrega un intervalo [left, right) y fusiona si es necesario.

        Inserta el intervalo en la posición correcta y fusiona con
        intervalos existentes que se superpongan o sean adyacentes.

        Args:
            left: Extremo izquierdo del intervalo (inclusivo).
            right: Extremo derecho del intervalo (exclusivo).
        """
        new_intervals: List[Tuple[int, int]] = []
        added = False

        for interval_left, interval_right in self._intervals:
            if interval_right < left:
                new_intervals.append((interval_left, interval_right))
            elif interval_left > right:
                if not added:
                    new_intervals.append((left, right))
                    added = True
                new_intervals.append((interval_left, interval_right))
            else:
                left = min(left, interval_left)
                right = max(right, interval_right)

        if not added:
            new_intervals.append((left, right))

        self._intervals = new_intervals

    def _remove_interval(self, left: int, right: int) -> None:
        """Elimina el intervalo [left, right) de los intervalos activos.

        Divide intervalos existentes si es necesario para remover la
        porción especificada.

        Args:
            left: Extremo izquierdo del intervalo a eliminar (inclusivo).
            right: Extremo derecho del intervalo a eliminar (exclusivo).
        """
        new_intervals: List[Tuple[int, int]] = []

        for interval_left, interval_right in self._intervals:
            if interval_right <= left or interval_left >= right:
                new_intervals.append((interval_left, interval_right))
            else:
                if interval_left < left:
                    new_intervals.append((interval_left, left))
                if interval_right > right:
                    new_intervals.append((right, interval_right))

        self._intervals = new_intervals

    def _query_interval(self, left: int, right: int) -> bool:
        """Verifica si el intervalo [left, right) está completamente cubierto.

        Args:
            left: Extremo izquierdo del intervalo a consultar (inclusivo).
            right: Extremo derecho del intervalo a consultar (exclusivo).

        Returns:
            True si todo el intervalo está cubierto, False en caso contrario.
        """
        if left >= right:
            return True

        idx = bisect_right(self._intervals, (left, float("inf")))
        if idx == 0:
            return False

        covered_right = self._intervals[idx - 1][1]
        return covered_right >= right
