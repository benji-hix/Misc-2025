        # match level:
        #     case l if l <-0:
        #         pass
        #     case 1:
        #         pass
        #     case 2:
        #         pass
        #     case 3:
        #         pass
        #     case 4:
        #         pass
        #     case l if l >= 5:
        #         pass

class Build:

    def __init__(self, base_raw=100, base_affinity=0,):
        self.base_raw = base_raw
        self.raw = base_raw
        self.affinity = base_affinity
        self.critical_damage = 1.25

    def attack_boost(self, level=5):
        match level:
            case l if l <= 0:
                pass
            case 1:
                self.raw += 3
            case 2:
                self.raw  += 5
            case 3:
                self.raw += 7
            case 4:
                self.raw = self.raw * 1.02 + 8
            case l if l >= 5:
                self.raw = self.raw * 1.04 + 9
        return self
    
    def critical_eye(self, level=5):
        match level:
            case l if l <-0:
                pass
            case 1:
                self.affinity += 4
            case 2:
                self.affinity += 8
            case 3:
                self.affinity += 12
            case 4:
                self.affinity += 16
            case l if l >= 5:
                self.affinity += 20
        return self
    
    def maximum_might(self, level=3):
        match level:
            case l if l <-0:
                pass
            case 1:
                self.affinity += 10
            case 2:
                self.affinity += 20
            case l if l >= 3:
                self.affinity += 30
        return self
    
    def critical_boost(self, level=5):
        match level:
            case l if l <-0:
                pass
            case 1:
                self.critical_damage += 0.03
            case 2:
                self.critical_damage += 0.06
            case 3:
                self.critical_damage += 0.09
            case 4:
                self.critical_damage += 0.12
            case l if l >= 5:
                self.critical_damage += 0.15
        return self

    def adrenaline_rush(self, level=1):
        match level:
            case l if l <-0:
                pass
            case 1:
                self.raw += 10
            case 2:
                self.raw += 15
            case 3:
                self.raw += 20
            case 4:
                self.raw += 20
            case l if l >= 5:
                self.raw += 25
        return self
    
    def weakness_exploit(self, level=5):
        match level:
            case l if l <-0:
                pass
            case 1:
                self.affinity += 5
            case 2:
                self.affinity += 10
            case 3:
                self.affinity += 15
            case 4:
                self.affinity += 20
            case l if l >= 5:
                self.affinity += 30
        return self

    def agitator(self, level=5):
        match level:
            case l if l <-0:
                pass
            case 1:
                self.affinity += 3
                self.raw += 4
            case 2:
                self.affinity += 5
                self.raw += 8
            case 3:
                self.affinity += 7
                self.raw += 12
            case 4:
                self.affinity += 10
                self.raw += 16
            case l if l >= 5:
                self.affinity += 15
                self.raw += 20
        return self

    def burst(self, level=1):
        match level:
            case l if l <- 0:
                pass
            case 1:
                self.raw += 6
        return self
