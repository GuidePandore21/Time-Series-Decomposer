class TimeSeriesDecomposer:
    def __init__(self, datas, type, window) -> None:
        """Constructeur de la classe TimeSeriesDecomposer

        Args:
            datas ([float]): données sur lesquels s'appuie la classe pour faire les calculs
            type ([string]): Est le type de Decomposition que l'on veut faire doit prendre une de ces deux valeurs : additive ou multiplicative
            window ([int]): [fenêtre dans lequel les calculs se font
        """
        self.datas = datas
        self.type = type
        self.window = window