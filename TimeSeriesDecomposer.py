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
    
    def trend(self):
        """Calcul la Trend sur la liste des données de la classe et la renvoie

        Returns:
            [[float]]: Trend liste
        """
        result = []       
        if self.window % 2 == 0:
            if len(self.datas) % 2 == 1:
                symetric = False
            else:
                symetric = True
            k = (self.window-1)//2
            if k == 0:
                k = 1
            k_min = k # k_min = -k
            k_max = (self.window-k)-1
            for i in range(len(self.datas)):
                _sum = 0
                if i+1 > k_min and len(self.datas) > i+k_max:
                    for j in range(i-k_min, i+k_max+1):
                        if self.datas[j] is None:
                            _sum = None
                            break
                        _sum += self.datas[j]
                    if _sum is not None:
                        result.append(_sum/self.window)
                    else:
                        result.append(None)
                else:
                    result.append(None)
            if symetric and self.window != 2:
                result = self.trend()
        else:
            k = self.window//2
            for i in range(len(self.datas)):
                _sum = 0
                if i+1 > k and i+k < len(self.datas):
                    for j in range(i-k, i+k+1):
                        _sum += self.datas[j]
                    result.append(_sum/self.window)
                else:
                    result.append(None)
        return result