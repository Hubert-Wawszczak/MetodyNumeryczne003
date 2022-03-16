
class lag():
    def __init__(self):
        self.lx = 0.5
        self.x0x = 0.1
        self.y0y = 4.77
        self.x1x = 0.2
        self.y1y = 3.05
        self.x2x = 0.3
        self.y2y = 2.18
        self.x3x = 0.4
        self.y3y = 1.65
        self.x0x0_xi = (self.x0x - self.x0x)
        self.x0x1_xi = self.x1x - self.x0x
        self.x0x2_xi = self.x2x - self.x0x
        self.x0x3_xi = self.x3x - self.x0x
        self.x1x0_xi = self.x0x - self.x1x
        self.x1x1_xi = self.x1x - self.x1x
        self.x1x2_xi = self.x2x - self.x1x
        self.x1x3_xi = self.x3x - self.x1x
        self.x2x0_xi = self.x0x - self.x2x
        self.x2x1_xi = self.x1x - self.x2x
        self.x2x2_xi = self.x2x - self.x2x
        self.x2x3_xi = self.x3x - self.x2x
        self.x3x0_xi = self.x0x - self.x3x
        self.x3x1_xi = self.x1x - self.x3x
        self.x3x2_xi = self.x2x - self.x3x
        self.x3x3_xi = self.x3x - self.x3x
        self.lx_x0 = self.lx - self.x0x
        self.lx_x1 = self.lx - self.x1x
        self.lx_x2 = self.lx - self.x2x
        self.lx_x3 = self.lx - self.x3x

    def get_lagrangea(self):
        #=C2*(H3*H4*H5)/(D3*D4*D5)+C3*(H2*H4*H5)/(E2*E4*E5)+C4*(H2*H3*H5)/(F2*F3*F5)+C5*(H2*H3*H4)/(G2*G3*G4)
        try:
            return (self.y0y * (self.lx_x1 * self.lx_x2 * self.lx_x3) / (self.x0x1_xi * self.x0x2_xi * self.x0x3_xi) + self.y1y * (self.lx_x0 * self.lx_x2 * self.lx_x3) / (self.x1x0_xi * self.x1x2_xi * self.x1x3_xi) + self.y2y * (self.lx_x0 * self.lx_x1 * self.lx_x3) / (self.x2x0_xi * self.x2x1_xi * self.x2x3_xi) + self.y3y * (self.lx_x0 * self.lx_x1 * self.lx_x2) / (self.x3x0_xi * self.x3x1_xi * self.x3x2_xi) )*(-1)
        except ZeroDivisionError:
            print("dzeilenie przez zero")

class newton():
    def __init__(self):
        self.lx = 0.5
        self.x0x = 0.0
        self.y0y = 0.0
        self.x1x = 1.0
        self.y1y = 1.0
        self.x2x = 2.0
        self.y2y = 4.0
        self.x3x = 3.0
        self.y3y = 10.0
        self.x0_xi_1 = (self.y1y - self.y0y) / (self.x1x - self.x0x)
        self.x1_xi_1 = (self.y2y - self.y1y) / (self.x2x - self.x1x)
        self.x2_xi_1 = (self.y3y - self.y2y) / (self.x3x - self.x2x)
        self.x0_xi_2 = (self.x1_xi_1 - self.x0_xi_1) / (self.x2x - self.x0x)
        self.x1_xi_2 = (self.x2_xi_1 - self.x1_xi_1) / (self.x3x - self.x1x)
        self.x0_xi_3 = (self.x1_xi_2 - self.x0_xi_2) / (self.x3x - self.x0x)
        self.x0_xi = self.lx - self.x0x
        self.x1_xi = self.lx - self.x1x
        self.x2_xi = self.lx - self.x2x
        self.x3_xi = self.lx - self.x3x

    def get_newton(self):
        #=C2+D2*H2+E2*H2*H3+F2*H2*H3*H4
        return self.y0y + self.x0_xi_1 * self.x0_xi + self.x0_xi_2 * self.x0_xi  * self.x1_xi + self.x0_xi_3 * self.x0_xi * self.x1_xi * self.x2_xi

if __name__ == '__main__':
    p = lag()
    n = newton()
    print(p.get_lagrangea())
    print(n.get_newton())

