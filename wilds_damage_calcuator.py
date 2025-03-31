class Build:

    def __init__(self, base_raw=100, base_affinity=0,):
        self.base_raw = base_raw
        self.base_affinity = base_affinity

    def attack_boost(self, level):
        match level:
            case <= 0
        return self