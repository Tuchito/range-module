"""Range Module — Clase pública para el problema LeetCode 715."""

from src.interval_manager import IntervalManager


class RangeModule:
    """Rastrea rangos de números representados como intervalos semiabiertos [left, right).

    Proporciona métodos para agregar, eliminar y consultar intervalos.
    Delega toda la lógica de manipulación a IntervalManager.
    """

    def __init__(self) -> None:
        """Inicializa el RangeModule con un IntervalManager vacío."""
        self._interval_manager = IntervalManager()

    def addRange(self, left: int, right: int) -> None:
        """Agrega el intervalo [left, right), fusionándolo con intervalos existentes.

        Args:
            left: Extremo izquierdo del intervalo (inclusivo).
            right: Extremo derecho del intervalo (exclusivo).
        """
        self._interval_manager._add_interval(left, right)

    def removeRange(self, left: int, right: int) -> None:
        """Elimina el intervalo [left, right) de los rangos rastreados.

        Divide intervalos existentes si es necesario.

        Args:
            left: Extremo izquierdo del intervalo a eliminar (inclusivo).
            right: Extremo derecho del intervalo a eliminar (exclusivo).
        """
        self._interval_manager._remove_interval(left, right)

    def queryRange(self, left: int, right: int) -> bool:
        """Devuelve True si todo el intervalo [left, right) está completamente rastreado.

        Args:
            left: Extremo izquierdo del intervalo a consultar (inclusivo).
            right: Extremo derecho del intervalo a consultar (exclusivo).

        Returns:
            True si el intervalo está completamente cubierto, False en caso contrario.
        """
        return self._interval_manager._query_interval(left, right)
